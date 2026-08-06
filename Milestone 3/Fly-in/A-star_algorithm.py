from infrastructure import base_structure, Drone, HubStruct, Connection
from parser import parser_main
from output import sim_state
import pygame
import time
import sys


def get_connect(current: HubStruct, next: HubStruct) -> Connection:
    current_name: str = f'{current.name}-{next.name}'
    reverse_name: str = f'{next.name}-{current.name}'

    for link in current.connections:
        if link.name == current_name or link.name == reverse_name:
            return link


def path_setter(walked: list, attempt: dict) -> dict:
    exclude_hubs: list = []

    for hub in attempt['hubs']:
        for previous in walked:
            if hub == previous:
                exclude_hubs.append(hub)

    for hub in exclude_hubs:
        try:
            attempt['hubs'].pop(attempt['hubs'].index(hub))
            if hub.type == 'restricted':
                attempt['cost'] -= 2
            else:
                attempt['cost'] -= 1
        except ValueError:
            continue
    if attempt['cost'] == 0 or len(attempt['hubs']) == 0:
        attempt['cost'] = -1

    return attempt


def hub_checker(walked: list, current: HubStruct) -> bool:
    if current.current_usage >= current.capacity:
        return True

    for hub in walked:
        if hub.name == current.name:
            return True

    return False


def goal_chaser(current: HubStruct, walked: list) -> bool:
    goal_found: int = False
    bad_found: int = False
    previous_hub: HubStruct = walked[len(walked) - 1]

    while goal_found is False and bad_found is False:
        if len(current.linked_hubs) == 2:
            if current.linked_hubs[0].name == 'goal':
                goal_found = True
                break
            elif current.linked_hubs[1].name == 'goal':
                goal_found = True
                break
            for hub in walked:
                if hub.name == current.linked_hubs[0]:
                    if hub.name != previous_hub.name:
                        bad_found = True
                elif hub.name != current.linked_hubs[1]:
                    if hub.name != previous_hub.name:
                        bad_found = True
                if bad_found is True:
                    break
            if goal_found is False and bad_found is False:
                if current.linked_hubs[0].name == previous_hub.name:
                    previous_hub = current
                    current = current.linked_hubs[1]
                else:
                    previous_hub = current
                    current = current.linked_hubs[0]
        else:
            bad_found = True

    if goal_found is True:
        return True
    else:
        return False


def compare_best_paths(best_path: dict, path_attempt: list,
                       current: list) -> dict:
    if path_attempt['cost'] != -1:
        if best_path['cost'] == -1:
            best_path = path_setter(current, path_attempt)
        elif best_path['cost'] >= path_attempt['cost']:
            if path_attempt['priority'] == 0:
                if best_path['priority'] == 0:
                    if best_path['cost'] > path_attempt['cost']:
                        best_path = path_setter(current, path_attempt)
                elif best_path['priority'] < 1:
                    if best_path['cost'] > path_attempt['cost']:
                        best_path = path_setter(current, path_attempt)
                elif best_path['priority'] != 1:
                    best_path = path_setter(current, path_attempt)
            elif best_path['priority'] < path_attempt['priority']:
                if best_path['priority'] != 1:
                    best_path = path_setter(current, path_attempt)
            elif path_attempt['priority'] == 1:
                best_path = path_setter(current, path_attempt)
    return best_path


def check_neighbor_costs(current: list, path_len: int, drone: Drone) -> list:
    best_path: dict = {'cost': -1, 'hubs': [], 'priority': 0}
    result_hubs: list = []
    link_check: Connection = None
    name_check: bool = False
    chase_check: bool = False

    for first_link in current[path_len - 1].linked_hubs:
        path_attempt: dict = {'cost': -1, 'hubs': [], 'priority': 0}
        second_hub: dict = {'cost': -1, 'hub': None}

        if first_link.name == 'goal':
            best_path = {'cost': 1, 'hubs': [first_link]}
            break

        num_links: int = 0
        for link in first_link.connections:
            num_links += 1
        if num_links < 2:
            if first_link.linked_hubs[0].name == 'goal':
                pass
            else:
                continue
        else:
            chase_check = goal_chaser(first_link, current)
            if chase_check is True:
                if first_link.current_usage < first_link.capacity:
                    best_path['cost'] = 0
                    best_path['priority'] = 1
                    best_path['hubs'].append(first_link)
                    best_path['hubs'].append(first_link.linked_hubs[0])
                    break

        name_check = hub_checker(current, first_link)
        if name_check is True:
            if isinstance(current, Connection):
                continue

        if first_link.type != 'restricted':
            if first_link.current_usage >= first_link.capacity:
                continue

        if first_link.type == 'blocked':
            continue
        elif first_link.type == 'restricted':
            link_check = get_connect(current[path_len - 1], first_link)
            if link_check is not None:
                if link_check.current_usage >= link_check.capacity:
                    continue
            path_attempt['cost'] = 2
        else:
            path_attempt['cost'] = 1
            if first_link.type == 'priority':
                path_attempt['priority'] = 2
        path_attempt['hubs'].append(first_link)

        for second_link in first_link.linked_hubs:
            if second_link.name == 'goal':
                second_hub['cost'] = -1
                path_attempt['hubs'].append(second_link)
                path_attempt['priority'] = 1
                break

            name_check = hub_checker(current, second_link)
            if name_check is True:
                continue

            if second_link.type == 'blocked':
                continue
            elif second_link.type == 'restricted':
                continue

            # avoid stepping into an immediate dead-end branch
            onward_hubs = [hub for hub in second_link.linked_hubs
                           if hub.name != first_link.name]
            if len(onward_hubs) == 0:
                onward_hubs = [hub for hub in first_link.linked_hubs
                               if hub.name != current[path_len - 1].name and
                               hub.name != second_link.name]
                if len(onward_hubs) == 0:
                    path_attempt = {'cost': -1, 'hubs': [], 'priority': 0}
                continue
            else:
                chase_check = goal_chaser(second_link, current)
                if chase_check is True:
                    if second_link.current_usage < second_link.capacity:
                        best_path['cost'] = 0
                        best_path['priority'] = 1
                        best_path['hubs'].append(second_link)
                        best_path['hubs'].append(second_link.linked_hubs[0])
                        break

            if second_hub['cost'] > 1:
                second_hub['cost'] = 1
                second_hub['hub'] = second_link

        if second_hub['cost'] != -1:
            path_attempt['cost'] += second_hub['cost']
            path_attempt['hubs'].append(second_hub['hub'])
        best_path = compare_best_paths(best_path, path_attempt, current)

    for hub in best_path['hubs']:
        result_hubs.append(hub)

    return result_hubs


def path_finder(drones: list, state: sim_state) -> None:
    searching_drones: int = len(drones)

    while searching_drones > 0:
        turn_result: dict = {}
        for drone in drones:

            # check at start of loop to allow pygame to be closed
            if state.output_type == 'both' or state.output_type == 'pygame':
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        state.output_type = 'default'
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            state.output_type = 'default'
                            pygame.quit()

            if drone.status == 'searching':
                prev_len: int = drone.path_len

                # finds the best next turns for the current drone
                if drone.next_hub is None:
                    temp: list = check_neighbor_costs(drone.current_path,
                                                      drone.path_len,
                                                      drone)
                else:
                    temp: list = [drone.next_hub]
                temp_len: int = len(temp) + prev_len

                # cleans out the second hub so turns print one at a time
                if temp_len - prev_len == 2:
                    temp.pop(1)
                    temp_len -= 1

                # goes through the previous hubs visited by the drone to clear
                # the space and make capacity available and also appends the
                # next hub it moves to in current turn
                if temp_len > prev_len:
                    for i in range(0, temp_len):
                        if i < prev_len:
                            if drone.current_path[i].occupants.count(
                                                            drone) != 0:
                                drone.current_path[i].remove_drone(drone)
                        else:
                            curr_i: int = i - prev_len
                            if temp[curr_i].type != 'restricted':
                                if temp[curr_i].name == 'goal':
                                    pass

                                drone.current_path.append(temp[curr_i])
                                temp[curr_i].add_drone(drone)
                            else:
                                if drone.next_hub is None:
                                    prev_i: int = prev_len - 1
                                    drone.next_hub = temp[curr_i]
                                    connection: Connection = get_connect(
                                        drone.current_path[prev_i],
                                        drone.next_hub
                                    )
                                    connection.add_drone(drone)
                                    drone.current_path.append(connection)
                                else:
                                    drone.current_path.append(drone.next_hub)
                                    drone.next_hub.add_drone(drone)
                                    drone.next_hub = None
                            local_name: str = drone.current_path[i].name
                            turn_result[f'D{drone.id}'] = local_name
                drone.path_len = temp_len
                if state.output_type == 'pygame':
                    time.sleep(0.4)
                if state.output_type == 'both':
                    time.sleep(0.4)
                time.sleep(0.1)

                # sets drone to no longer be looped
                if drone.current_path[drone.path_len - 1].name == 'goal':
                    drone.status = 'plotted'

            # sets drone count to reduce and eventually ending loop
            if drone.status == 'plotted':
                searching_drones -= 1
                drone.status = 'goal'

        # update state class with the new locations
        state.update_state(turn_result)

    state.produce_end()


def main() -> None:
    output_type: str = 'default'
    preplanned_outputs: list = ['terminal', 'pygame', 'neither', 'both']

    if len(sys.argv) < 2:
        print("Invalid command line input",
              "Please try: python3 fly-in.py ./maps/easy/01_linear_path.txt",
              sep='\n')
        return
    elif len(sys.argv) == 2 or len(sys.argv) == 3:
        try:
            test = open(sys.argv[1], 'r')
        except FileNotFoundError as alert:
            print(alert)
            quit()
        test.close()

        if len(sys.argv) == 3:
            if preplanned_outputs.count(f'{sys.argv[2]}') == 1:
                output_type = sys.argv[2]
            else:
                print('Invalid output type; using default output')
    else:
        print("Invalid command line input",
              "Please try: python3 fly-in.py ./maps/easy/01_linear_path.txt",
              sep='\n')
        quit()

    sim_config: dict = base_structure(parser_main(sys.argv[1]))

    state_saver: sim_state = sim_state(sim_config, output_type)
    path_finder(sim_config['drones'], state_saver)


main()

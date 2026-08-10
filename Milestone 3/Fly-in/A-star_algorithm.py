from infrastructure import base_structure, Drone, HubStruct, Connection
from parser import parser_main
from output import sim_state
import pygame
import time
import sys
import heapq
import itertools


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
    if current.name not in ('start', 'goal') and current.current_usage >= current.capacity:
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


# def start_search(current: HubStruct, walked: list) -> bool:
#     for hub in current.linked_hubs:
#         if hub.name == current.name:
#             continue
#         for prev in walked:
#             if prev.name == current.name:
#                 continue
#         if hub.name == 'goal':
#             return False
#         if hub.name == 'start':
#             return True
#     return False


# def start_avoider(current: HubStruct, walked: list, distance: int) -> bool:
#     while distance > 0:
#         for hub in current.linked_hubs:
#             if start_search(hub, walked) is False:
#                 distance -= 1
#                 if distance == 0:
#                     return True
#                 current = hub
#                 break
#         if distance > 0:
#             return False
#     return True


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


def check_neighbor_costs(current: list, path_len: int, drone: Drone,
                        goal_name: str) -> list:
    start_hub: HubStruct = current[path_len - 1]

    if start_hub.name == goal_name:
        return []

    def hub_cost(hub: HubStruct) -> int:
        if hub.type == 'restricted':
            return 2
        return 1

    def hub_priority(hub: HubStruct) -> int:
        return 1 if hub.type == 'priority' else 0

    def is_accessible(hub: HubStruct) -> bool:
        if hub.type == 'blocked':
            return False
        if hub.name == goal_name:
            return True
        if hub.name != 'start' and hub.current_usage >= hub.capacity:
            return False
        return True

    def connection_available(a: HubStruct, b: HubStruct) -> bool:
        link = get_connect(a, b)
        if link is None:
            return True
        return link.current_usage < link.capacity

    queue: list = []
    counter = itertools.count()
    heapq.heappush(queue, (0, 0, next(counter), [start_hub]))
    best_scores: dict = {start_hub.name: (0, 0)}

    while queue:
        cost, neg_priority, _, path = heapq.heappop(queue)
        current_hub: HubStruct = path[-1]
        if current_hub.name == goal_name:
            return [path[1]]

        for neighbor in current_hub.linked_hubs:
            if not is_accessible(neighbor):
                continue
            if not connection_available(current_hub, neighbor):
                continue
            if neighbor.name in [hub.name for hub in path]:
                continue

            next_cost = cost + hub_cost(neighbor)
            next_priority = -neg_priority + hub_priority(neighbor)
            prev = best_scores.get(neighbor.name)
            current_score = (next_cost, -next_priority)
            if prev is not None and prev <= current_score:
                continue

            best_scores[neighbor.name] = current_score
            heapq.heappush(queue, (next_cost, -next_priority,
                                   next(counter), path + [neighbor]))

    return []


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
                    temp: list = check_neighbor_costs(
                        drone.current_path,
                        drone.path_len,
                        drone,
                        state.goal_name
                    )
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
                                if temp[curr_i].name == state.goal_name:
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
                    time.sleep(0.1)
                if state.output_type == 'both':
                    time.sleep(0.1)
                time.sleep(0.1)

                # sets drone to no longer be looped
                if drone.current_path[drone.path_len - 1].name == state.goal_name:
                    drone.status = 'plotted'

            # sets drone count to reduce and eventually ending loop
            if drone.status == 'plotted':
                searching_drones -= 1
                drone.status = 'goal'

        # update state class with the new locations
        state.update_state(turn_result)

    state.produce_end()


# def pathway_prechecks(sim_config: sim_state) -> sim_state:
#     node_list: list = []

#     for hub in sim_config['hubs'][0].linked_hubs:
#         if hub.type != 'blocked':
#             node_list.append(hub)
#     sim_config['hubs'][0].checked = True

#     for node in node_list:
#         curr_node_count: int = 0
#         if node.name != 'goal':
#             node.checked = True
#         for hub in node.linked_hubs:
#             if hub.checked is False and hub.type != 'blocked':
#                 curr_node_count += 1
#                 node_list.append(hub)
#         if curr_node_count == 0:
#             if node.name != 'goal':
#                 hub.type = 'blocked'

#     for node in node_list:
#         print(f'{node.name} - {node.type}')

#     return sim_config


def main() -> None:
    output_type: str = 'default'
    preplanned_outputs: list = ['terminal', 'pygame', 'both']

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
    # sim_config = pathway_prechecks(sim_config)

    state_saver: sim_state = sim_state(sim_config, output_type)
    path_finder(sim_config['drones'], state_saver)


if __name__ == '__main__':
    main()

from infrastructure import base_structure, HubStruct, Drone
from parser import parser_main
from output import turn_print
import time


def path_setter(walked: list, attempt: dict) -> dict:
    exclude_hubs: list = []

    for hub in attempt['hubs']:
        for previous in walked:
            if hub == previous:
                exclude_hubs.append(hub)

    for hub in exclude_hubs:
        attempt['hubs'].pop(attempt['hubs'].index(hub))
        if hub.type == 'restriced':
            attempt['cost'] -= 2
        else:
            attempt['cost'] -= 1
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


def check_neighbor_costs(current: list, len: int) -> list:
    best_path: dict = {'cost': -1, 'hubs': [], 'priority': 0}
    result_hubs: list = []
    name_check: bool = False

    for first_link in current[len - 1].linked_hubs:
        path_attempt: dict = {'cost': -1, 'hubs': [], 'priority': 0}
        second_hub: dict = {'cost': -1, 'hub': None}

        if first_link.name == 'goal':
            best_path = {'cost': 1, 'hubs': [first_link]}
            break

        name_check = hub_checker(current, first_link)
        if name_check is True:
            continue

        if first_link.type == 'blocked':
            continue
        elif first_link.type == 'restricted':
            path_attempt['cost'] = 2
        else:
            path_attempt['cost'] = 1
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
                if second_hub['cost'] > 2 or second_hub['cost'] < 0:
                    second_hub['cost'] = 2
                    second_hub['hub'] = second_link
            else:
                if second_hub['cost'] > 1:
                    second_hub['cost'] = 1
                    second_hub['hub'] = second_link
        if second_hub['cost'] != -1:
            path_attempt['cost'] += second_hub['cost']
            path_attempt['hubs'].append(second_hub['hub'])
        if path_attempt['cost'] != -1:
            if best_path['cost'] == -1:
                best_path = path_setter(current, path_attempt)
            elif best_path['cost'] >= path_attempt['cost']:
                if path_attempt['priority'] == 0:
                    if best_path['priority'] == 0:
                        if best_path['cost'] > path_attempt['cost']:
                            best_path = path_setter(current, path_attempt)
                elif best_path['priority'] < path_attempt['priority']:
                    best_path = path_setter(current, path_attempt)

    # if best_path['cost'] < 1:
    #     print('waiting...')
    # else:
    for hub in best_path['hubs']:
        # print(f'~~~{hub.name}~~~>', end='')
        result_hubs.append(hub)
    # print('')

    return result_hubs


def finish_connection(current: list, first: HubStruct) -> list:
    result_hubs: list = [first]
    second_hub: dict = {'cost': -1, 'hub': None}
    name_check: bool = False

    for hub in first:
        # more code ya know what i mean
        continue

    return result_hubs


def path_finder(drones: list) -> None:
    searching_drones: int = len(drones)

    while searching_drones > 0:
        for drone in drones:
            if drone.status == 'searching':
                prev_len: int = drone.path_len
                # for hub in drone.current_path:
                #     print(f'-----{hub.name}->', end=' ')
                # print('')
                # finds the best next turns for the current drone
                if drone.local_type == 'hub':
                    temp: list = check_neighbor_costs(drone.current_path,
                                                      drone.path_len)
                elif drone.local_type == 'connection':
                    temp: list = finish_connection(drone.current_path,
                                                   drone.next_hub)
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
                            drone.current_path[i].remove_drone(drone)
                        else:
                            drone.current_path.append(temp[i - prev_len])
                            temp[i - prev_len].add_drone(drone)
                            turn_print(drone.id, temp[i - prev_len].name)
                drone.path_len = temp_len
                time.sleep(0.1)

                # sets drone to no longer be looped
                if drone.current_path[drone.path_len - 1].name == 'goal':
                    drone.status = 'plotted'

            # sets drone count to reduce and eventually ending loop
            if drone.status == 'plotted':
                # for hub in drone.current_path:
                #     print(f'-{hub.name}->', end=' ')
                # print('')
                searching_drones -= 1
                drone.status = 'goal'


def main() -> None:
    sim: dict = base_structure(parser_main("./maps/easy/test.txt"))
    path_finder(sim['drones'])


main()

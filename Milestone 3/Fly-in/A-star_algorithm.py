from infrastructure import base_structure, HubStruct, Drone
from parser import parser_main
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


def hub_name_checker(walked: list, current: HubStruct) -> bool:
    for hub in walked:
        if hub.name == current.name:
            return True

    return False


def check_neighbor_costs(current: list, len: int) -> list:
    best_path: dict = {'cost': -1, 'hubs': [], 'priority': 0}
    result_hubs: list = []
    name_check: bool = False

    # add checks so that they dont just repeatedly back track
    print(current[len - 1].name)
    for first_link in current[len - 1].linked_hubs:
        path_attempt: dict = {'cost': -1, 'hubs': [], 'priority': 0}
        second_hub: dict = {'cost': -1, 'hub': None}

        if first_link.name == 'goal':
            best_path = {'cost': 1, 'hubs': [first_link]}
            break

        name_check = hub_name_checker(current, first_link)
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

            name_check = hub_name_checker(current, second_link)
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
            if current[len - 1].name == 'waypointA':
                print(f' owowow = {second_hub['hub'].name}')
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

    for hub in best_path['hubs']:
        print(f'~~~{hub.name}~~~>', end='')
        result_hubs.append(hub)
    print('')

    return result_hubs


def path_finder(drone: Drone) -> None:
    current_path: list = [drone.location]
    path_len: int = 1

    while drone.status == 'searching':
        for hub in current_path:
            print(f'-----{hub.name}->', end=' ')
        print('')
        temp: list = check_neighbor_costs(current_path, path_len)
        for hub in temp:
            current_path.append(hub)
        path_len = len(current_path)
        time.sleep(0.1)
        if current_path[path_len - 1].name == 'goal':
            drone.status = 'plotted'
    for hub in current_path:
        print(f'-{hub.name}->', end=' ')
    print('')


def main() -> None:
    sim: dict = base_structure(parser_main("./maps/easy/test.txt"))
    path_finder(sim['drones'][0])


main()

from infrastructure import base_structure, HubStruct, Drone
from parser import parser_main
import time

def path_setter(walked: list, current: HubStruct) -> dict:
    path_walked: dict = {}
    return path_walked


def check_neighbor_costs(current: list, len: int) -> list:
    best_path: dict = {'cost': -1, 'hubs': []}
    result_hubs: list = []

    # add checks so that they dont just repeatedly back track
    for first_link in current[len - 1].linked_hubs:
        path_attempt: dict = {'cost': -1, 'hubs': []}
        if first_link.type == 'blocked':
            continue
        elif first_link.type == 'restriced':
            path_attempt['cost'] = 2
        else:
            path_attempt['cost'] = 1
        path_attempt['hubs'].append(first_link)
        if path_attempt['hubs'][0].name == 'goal':
            best_path = path_attempt
            break
        second_hub: dict = {'cost': -1, 'hub': None}
        for second_link in first_link.linked_hubs:
            if second_link.type == 'blocked':
                continue
            elif second_link.type == 'restriced':
                if second_hub['cost'] > 2 or second_hub['cost'] < 0:
                    second_hub['cost'] = 2
                    second_hub['hub'] = second_link
            else:
                if second_hub['cost'] > 1 or second_hub['cost'] < 0:
                    second_hub['cost'] = 1
                    second_hub['hub'] = second_link
        if second_hub['cost'] != -1:
            path_attempt['cost'] += second_hub['cost']
            path_attempt['hubs'].append(second_hub['hub'])
        if best_path['cost'] == -1 and path_attempt['cost'] != -1:
            best_path = path_attempt
        elif best_path['cost'] != -1 and path_attempt['cost'] != -1:
            if best_path['cost'] > path_attempt['cost']:
                best_path = path_attempt

    for hub in best_path['hubs']:
        result_hubs.append(hub)

    return result_hubs


def path_finder(drone: Drone) -> None:
    current_path: list = [drone.location]
    path_len: int = 1

    while drone.status == 'searching':
        temp: list = check_neighbor_costs(current_path, path_len)
        for hub in temp:
            current_path.append(hub)
        path_len = len(current_path)
        time.sleep(0.1)
        print(current_path)
        print(current_path[path_len - 1].name)
        if current_path[path_len - 1].name == 'goal':
            drone.status == 'plotted'
    print(current_path)


def main() -> None:
    sim: dict = base_structure(parser_main("./maps/easy/01_linear_path.txt"))
    path_finder(sim['drones'][0])


main()

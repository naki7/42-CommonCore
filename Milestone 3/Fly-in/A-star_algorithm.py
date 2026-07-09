from infrastructure import base_structure, HubStruct, Drone


def path_setter(walked: list, current: HubStruct) -> dict:
    path_walked: dict = {}
    return path_walked


def check_neighbor_costs(current: list, len: int) -> list:
    best_path: dict = {'cost': -1, 'hubs': []}
    result_hubs: list = []

    for first_links in current[len - 1].connections:
        path_attempt: dict = {'cost': -1, 'hubs': []}
        if first_links.type == 'blocked':
            continue
        elif first_links.type == 'restriced':
            path_attempt['cost'] = 2
        else:
            path_attempt['cost'] = 1
        path_attempt['hubs'].append(first_links)
        for second_links in first_links:
            continue
    return result_hubs


def path_finder(drone: Drone) -> None:
    current_path: list = [drone.location]
    path_len: int = 1

    while drone.status == 'searching':
        current_path.append(check_neighbor_costs(current_path, len))
        path_len = len(current_path)
        if current_path[path_len - 1].name == 'goal':
            drone.status == 'plotted'

from infrastructure import Hub, Connection
from typing import Any


def goal_chaser(current: Hub, walked: list[Any], goal_name: str) -> bool:
    goal_found: int = False
    bad_found: int = False
    previous_hub: Hub = walked[len(walked) - 1]

    while goal_found is False and bad_found is False:
        if len(current.linked_hubs) == 2:
            if current.linked_hubs[0].name == goal_name:
                goal_found = True
                break
            elif current.linked_hubs[1].name == goal_name:
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


def hub_checker(walked: list[Any], current: Hub) -> bool:
    if current.capacity is not None:
        if current.current_usage >= current.capacity:
            return True

    for hub in walked:
        if hub.name == current.name:
            return True

    return False


def path_setter(walked: list[Any], attempt: dict[Any, Any]) -> dict[Any, Any]:
    exclude_hubs: list[Any] = []

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


def compare_best_paths(best_path: dict[Any, Any], path_attempt: dict[Any, Any],
                       current: list[Any]) -> dict[Any, Any]:
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


def astar(current: list[Any], path_len: int, goal_name: str) -> list[Any]:
    best_path: dict[Any, Any] = {'cost': -1, 'hubs': [], 'priority': 0}
    result_hubs: list[Any] = []
    link_check: Connection | None = None
    name_check: bool = False
    chase_check: bool = False
    from fly_in import get_connect

    for first_link in current[path_len - 1].linked_hubs:
        path_attempt: dict[Any, Any] = {'cost': -1, 'hubs': [], 'priority': 0}
        second_hub: dict[Any, Any] = {'cost': -1, 'hub': None}

        if first_link.type == 'blocked':
            continue

        if first_link.name == goal_name:
            best_path = {'cost': 1, 'hubs': [first_link]}
            break

        num_links: int = 0
        for link in first_link.connections:
            num_links += 1
        if num_links < 2:
            if first_link.linked_hubs[0].name == goal_name:
                pass
            else:
                continue
        else:
            chase_check = goal_chaser(first_link, current, goal_name)
            if chase_check is True:
                if first_link.current_usage < first_link.capacity:
                    best_path['cost'] = 0
                    if first_link.type == 'priority':
                        best_path['priority'] = 1
                    else:
                        best_path['priority'] = 2
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

        if first_link.type == 'restricted':
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
            if second_link.type == 'blocked':
                continue
            elif second_link.type == 'restricted':
                continue

            if second_link.name == goal_name:
                second_hub['cost'] = -1
                path_attempt['hubs'].append(second_link)
                path_attempt['priority'] = 2
                break

            name_check = hub_checker(current, second_link)
            if name_check is True:
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
                chase_check = goal_chaser(second_link, current, goal_name)
                if chase_check is True:
                    if second_link.current_usage < second_link.capacity:
                        best_path['cost'] = 0
                        best_path['priority'] = 2
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

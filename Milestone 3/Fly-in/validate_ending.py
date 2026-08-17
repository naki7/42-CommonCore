from typing import Any


def recursive_check(current: Any, checked: list[Any], goal_name: str) -> bool:
    hub_checked: bool = False
    next_check: bool = False

    for hub in current.linked_hubs:
        if hub.name == goal_name:
            return True
        for name in checked:
            if name == hub.name:
                hub_checked = True
        if hub_checked is False:
            checked.append(hub.name)
            next_check = recursive_check(hub, checked, goal_name)
            if next_check is True:
                return next_check
        else:
            hub_checked = False

    return False


def validate_ending(start: Any, goal_name: str) -> bool:
    for hub in start.linked_hubs:
        if recursive_check(hub, [start.name], goal_name):
            return True

    return False

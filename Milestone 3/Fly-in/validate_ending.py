from typing import Any


def loop_closer(state: Any) -> None:
    exclude: list[Any] = [state.hubs[0].name]
    double_chain: list[Any] = []
    block: list[Any] = []

    for link in state.hubs[0].linked_hubs:
        exclude.append(link.name)
        for follow_up in link.linked_hubs:
            if len(follow_up.linked_hubs) == 2:
                if exclude.count(follow_up.name) == 0:
                    double_chain.append(follow_up.name)
            for deepest in follow_up.linked_hubs:
                if exclude.count(deepest.name) == 0:
                    if len(deepest.linked_hubs) == 2:
                        double_chain.append(deepest.name)

    for name in double_chain:
        if block.count(name) == 0:
            if double_chain.count(name) > 1:
                if name != state.goal_name and name != 'start':
                    block.append(name)

    for hub in state.hubs:
        if block.count(hub.name) != 0:
            if hub.type != 'restricted':
                hub.type = 'blocked'
                for link in hub.linked_hubs:
                    if double_chain.count(link.name):
                        if link.type != 'restricted':
                            link.type = 'blocked'


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

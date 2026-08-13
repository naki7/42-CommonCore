from infrastructure import Hub
from typing import Any
import heapq
import itertools


def dijkstra(current: list[Any], path_len: int, goal_name: str) -> list[Any]:
    start_hub: Hub = current[path_len - 1]
    from fly_in import get_connect

    if start_hub.name == goal_name:
        return []

    def hub_cost(hub: Hub) -> int:
        if hub.type == 'restricted':
            return 2
        return 1

    def hub_priority(hub: Hub) -> int:
        return 1 if hub.type == 'priority' else 0

    def is_accessible(hub: Hub) -> bool:
        if hub.type == 'blocked':
            return False
        if hub.name == goal_name:
            return True
        if hub.capacity is not None:
            if hub.name != 'start' and hub.current_usage >= hub.capacity:
                return False
        return True

    def connection_available(a: Hub, b: Hub) -> bool:
        link = get_connect(a, b)
        if link is None:
            return True
        if link.current_usage < link.capacity:
            return True
        else:
            return False

    queue: list[Any] = []
    counter = itertools.count()
    heapq.heappush(queue, (0, 0, next(counter), [start_hub]))
    best_scores: dict[Any, Any] = {start_hub.name: (0, 0)}

    while queue:
        cost, neg_priority, _, path = heapq.heappop(queue)
        current_hub: Hub = path[-1]
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

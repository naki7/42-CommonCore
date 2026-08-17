from parser import HubStruct
from typing import Any
from validate_ending import validate_ending


class Drone:
    def __init__(self, index: int, start: HubStruct):
        self.id: int = index
        self.location: HubStruct = start
        self.next_hub: HubStruct | None = None
        self.status: str = 'searching'
        self.current_path: list[Any] = [self.location]
        self.path_len: int = 1


class Hub:
    def __init__(self, config: HubStruct, connections: list[Any]):
        self.name: str = config.name
        self.x: int = config.x
        self.y: int = config.y
        self.type: str | None = config.zone
        self.color: str | None = config.color
        self.capacity: int | None = config.max_drones
        self.connections: list[Any] = []
        self.connect_names: list[Any] = self.get_links(connections)
        self.linked_hubs: list[Any] = []
        self.current_usage: int = 0
        self.occupants: list[Any] = []

    def get_links(self, connections: list[Any]) -> list[Any]:
        links_list: list[Any] = []
        for link in connections:
            if link.hubs[0] == self.name:
                links_list.append(link.hubs[1])
                self.connections.append(link)
            elif link.hubs[1] == self.name:
                links_list.append(link.hubs[0])
                self.connections.append(link)
        return links_list

    def link_hubs(self, hubs: list[Any]) -> None:
        for name in self.connect_names:
            for hub in hubs:
                if hub.name == name:
                    self.linked_hubs.append(hub)

    def add_drone(self, drone: Drone) -> bool:
        if self.name == 'start' or self.name == 'goal':
            self.current_usage += 1
            self.occupants.append(drone)
            return True
        elif self.capacity is not None:
            if self.current_usage < self.capacity:
                self.current_usage += 1
                self.occupants.append(drone)
                return True
        return False

    def remove_drone(self, drone: Drone) -> bool:
        if self.current_usage > 0:
            self.current_usage -= 1
            self.occupants.pop(self.occupants.index(drone))
            return True
        else:
            return False


class Connection:
    def __init__(self, index: int, config: list[Any]):
        self.id: int = index
        self.hubs: tuple[Any, Any] = (config[0], config[1])
        self.name: str = f'{config[0]}-{config[1]}'
        self.linked_hubs: list[Any] = []
        self.init_hub: HubStruct | None = None
        self.capacity: int = config[2]
        self.current_usage: int = 0
        self.occupants: list[Any] = []

    def add_drone(self, drone: Drone) -> bool:
        if self.current_usage < self.capacity:
            self.current_usage += 1
            self.occupants.append(drone)
            return True
        else:
            return False

    def remove_drone(self, drone: Drone) -> bool:
        if self.current_usage > 0:
            self.current_usage -= 1
            self.occupants.pop(self.occupants.index(drone))
            return True
        else:
            return False

    def find_hubs(self, hubs: list[Any]) -> None:
        for hub in hubs:
            if self.init_hub is None and hub.name == self.hubs[0]:
                self.init_hub = hub
            if hub.name == self.hubs[1]:
                self.linked_hubs.append(hub)


def base_structure(config: dict[Any, Any]) -> dict[Any, Any]:
    hubs: list[Any] = []
    total_hubs: int = 0
    connections: list[Any] = []
    drones: list[Any] = []

    for key in config['connections']:
        connections.append(Connection(key, config['connections'][key]))

    hubs.append(Hub(config['hubs']['start_hub'], connections))
    for key in config['hubs']:
        if key != 'start_hub' and key != 'end_hub':
            hubs.append(Hub(config['hubs'][key], connections))
    hubs.append(Hub(config['hubs']['end_hub'], connections))
    total_hubs = len(hubs) - 1

    for hub in hubs:
        hub.link_hubs(hubs)

    for link in connections:
        link.find_hubs(hubs)

    for i in range(0, config['nb_drones']):
        drones.append(Drone(i + 1, hubs[0]))
        hubs[0].add_drone(drones[i])

    end_check: bool = validate_ending(hubs[0], hubs[-1].name)

    if end_check is False:
        print('Error: No hubs and connections complete a path between the',
              'start and end hub')
        quit()

    return {
        'drones': drones,
        'connections': connections,
        'hubs': hubs,
        'goal_name': hubs[-1].name,
        'total_hubs': total_hubs
        }

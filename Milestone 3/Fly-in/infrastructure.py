from parser import HubStruct


class Drone:
    def __init__(self, index: int, start: HubStruct):
        self.id: int = index
        self.location: HubStruct = start
        self.next_hub: HubStruct | None = None
        self.status: str = 'searching'
        self.current_path: list = [self.location]
        self.path_len: int = 1


class Hub:
    def __init__(self, config: HubStruct, connections: list):
        self.name: str = config.name
        self.x: int = config.x
        self.y: int = config.y
        self.type: str | None = config.zone
        self.color: str | None = config.color
        self.capacity: int | None = config.max_drones
        self.connections: list = []
        self.connect_names: list = self.get_links(connections)
        self.linked_hubs: list = []
        self.current_usage: int = 0
        self.occupants: list = []
        # self.checked: bool = False

    def get_links(self, connections: list) -> list:
        links_list: list = []
        for link in connections:
            if link.hubs[0] == self.name:
                links_list.append(link.hubs[1])
                self.connections.append(link)
            elif link.hubs[1] == self.name:
                links_list.append(link.hubs[0])
                self.connections.append(link)
        return links_list

    def link_hubs(self, hubs: list) -> None:
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
    def __init__(self, index: int, config: list):
        self.id: int = index
        self.hubs: tuple = (config[0], config[1])
        self.name: str = f'{config[0]}-{config[1]}'
        self.linked_hubs: list = []
        self.init_hub: HubStruct | None = None
        self.capacity: int = config[2]
        self.current_usage: int = 0
        self.occupants: list = []

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

    def find_hubs(self, hubs: list) -> None:
        for hub in hubs:
            if self.init_hub is None and hub.name == self.hubs[0]:
                self.init_hub = hub
            if hub.name == self.hubs[1]:
                self.linked_hubs.append(hub)


def base_structure(config: dict) -> dict:
    hubs: list = []
    total_hubs: int = 0
    connections: list = []
    drones: list = []

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

    return {
        'drones': drones,
        'connections': connections,
        'hubs': hubs,
        'goal_name': hubs[-1].name,
        'total_hubs': total_hubs
        }

from parser import HubStruct, parser_main
# import random


class Hub:
    def __init__(self, config: HubStruct, connections: list):
        self.name: str = config.name
        self.location: tuple = (config.x, config.y)
        self.type: str = config.zone
        self.color: str = config.color
        self.capacity: int = config.max_drones
        self.connections: list = self.get_links(connections)
        self.linked_hubs: list = []

    def get_links(self, connections: list) -> list:
        links_list: list = []
        for link in connections:
            if link.hubs[0] == self.name:
                links_list.append(link.hubs[1])
            elif link.hubs[1] == self.name:
                links_list.append(link.hubs[0])
        return links_list

    def link_hubs(self, hubs: list) -> None:
        for name in self.connections:
            for hub in hubs:
                if hub.name == name:
                    self.linked_hubs.append(hub)


class Connection:
    def __init__(self, index: int, config: list):
        self.id: int = index
        self.hubs: tuple = (config[0], config[1])
        self.capacity: int = config[2]


class Drone:
    def __init__(self, index: int, start: HubStruct):
        self.id: int = index
        self.location: HubStruct = start
        self.status: str = 'searching'


def base_structure(config: dict) -> dict:
    hubs: list = []
    total_hubs: int = 0
    connections: list = []
    drones: list = []
    # completed_trips: list = []

    for key in config['connections']:
        connections.append(Connection(key, config['connections'][key]))

    for link in connections:
        print(f'{link.id}==={link.hubs[0]}-{link.hubs[1]}')

    hubs.append(Hub(config['hubs']['start_hub'], connections))
    for key in config['hubs']:
        if key != 'start_hub' and key != 'end_hub':
            hubs.append(Hub(config['hubs'][key], connections))
    hubs.append(Hub(config['hubs']['end_hub'], connections))
    total_hubs = len(hubs) - 1

    for hub in hubs:
        hub.link_hubs(hubs)
        print(f'{hub.name} @ {hub.location[0]}, {hub.location[1]}\n',
              f'    type:{hub.type}, color:{hub.color}, limit:{hub.capacity}',
              f'\n      {hub.connections}\n         {hub.linked_hubs}')

    for i in range(0, config['nb_drones']):
        drones.append(Drone(i + 1, hubs[0]))

    for drone in drones:
        print(f'{drone.id}-{drone.location.name}')

    return {
        'drones': drones,
        'connections': connections,
        'hubs': hubs,
        'total_hubs': total_hubs
        }

    # while len(completed_trips) != len(drones):
    #     print_arr: list = []
    #     for drone in drones:
    #         if drone.location != hubs[total_hubs]:
    #             connections_len: int = len(drone.location.connections)
    #             rand_i: int = random.randrange(0, connections_len)
    #             next_location: str = drone.location.connections[rand_i]
    #             for hub in hubs:
    #                 if hub.name == next_location:
    #                     drone.location = hub
    #                     break
    #             print_arr.append(f'D{drone.id}-{next_location}')
    #             if drone.location == hubs[total_hubs]:
    #                 completed_trips.append(drone)
    #     for i in range(0, len(print_arr)):
    #         print(print_arr[i], end='')
    #         if i != len(print_arr) - 1:
    #             print(' ', end='')
    #         else:
    #             print('')


# base_structure(parser_main("./maps/easy/01_linear_path.txt"))

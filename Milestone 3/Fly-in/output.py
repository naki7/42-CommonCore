import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from infrastructure import HubStruct


class sim_state:
    def __init__(self, config: dict, output_type: str):
        self.num_hubs: int = config['total_hubs']
        self.hubs: dict = config['hubs']
        self.connections: list = config['connections']
        self.drones: list = [f'D{drone.id}' for drone in config['drones']]
        self.current_turn: int = 0
        self.output_type: str = output_type
        self.init_check: bool = False
        self.turn_saver: list = []
        self.display = None
        self.copy_display = None
        self.current_state: dict = self.setup_state()
        self.graph: list = None

    # pygame setup
    def sim_init(self) -> None:
        pygame.init()
        self.display = pygame.display.set_mode((1400, 1000))
        pygame.display.set_caption('Fly-in')
        self.display.fill((0, 0, 0))

        for x in self.graph:
            for y in self.graph[x]:
                pygame.draw.rect(self.display, (0, 0, 255),
                                 [x * 250, y * 250, 200, 75],
                                 0)

        for link in self.connections:
            hub1: HubStruct = link.init_hub
            for hub2 in link.linked_hubs:
                if hub1.x != hub2 and hub1.y != hub2.y:
                    pygame.draw.line(self.display, (255, 0, 0),
                                     [hub1.x * 250 + 100, hub1.y * 250 + 85],
                                     [hub2.x * 250 + 100, hub2.y * 250 - 10],
                                     3)
                else:
                    pygame.draw.line(self.display, (255, 0, 0),
                                     [hub1.x * 250 + 210, hub1.y * 250 + 40],
                                     [hub2.x * 250 - 10, hub2.y * 250 + 40],
                                     3)

        pygame.display.update()
        self.copy_display = self.display.copy()

    def sim_updater(self) -> None:
        self.display.blit(self.copy_display, (0, 0))
        pygame.display.update()
        for key in self.current_state:
            if key == 'turn':
                continue
            for hub in self.hubs:
                if self.current_state[key] == hub.name:
                    pygame.draw.circle(self.display, (0, 255, 0),
                                       [hub.x * 250 + 100, hub.y * 250 + 40],
                                       3.14)
        pygame.display.flip()

    def setup_state(self) -> None:
        setup_dict: dict = {'turn': self.current_turn}
        init_turn: dict = {}

        for drone in self.drones:
            setup_dict[drone] = 'start'
            if self.init_check is False:
                init_turn[drone] = 'start'
        if self.init_check is False:
            self.current_state.setup_dict
            self.init_check = True
        self.turn_saver.append(turn_print(init_turn, self.output_type))
        if self.output_type == 'pygame' or self.output_type == 'both':
            self.graph = create_graph(self.hubs, self.connections)
            self.sim_init()
            self.sim_updater()

        return setup_dict

    def update_state(self, turn_result: dict) -> None:
        self.current_turn += 1
        self.current_state['turn'] = self.current_turn

        for drone in turn_result:
            self.current_state[drone] = turn_result[drone]

        self.turn_saver.append(turn_print(turn_result, self.output_type))
        if self.output_type == 'pygame' or self.output_type == 'both':
            self.sim_updater()

    def produce_end(self) -> None:
        for turn in self.turn_saver:
            print(turn)


def create_graph(hubs: list, links: list) -> dict:
    row_track: dict = {}
    graph_track: dict = {}

    for hub in hubs:
        try:
            row_track.get(hub.x)
            row_track[hub.x].append(hub)
        except KeyError:
            row_track[hub.x] = [hub]

    for row in row_track:
        graph_track[row] = {}
        for hub in row_track[row]:
            try:
                graph_track[row].get(hub.y)
                graph_track[row][hub.y].append(hub)
            except KeyError:
                graph_track[row][hub.y] = hub

    return graph_track


def turn_print(turn_result: dict, out_type: str) -> str:
    num_moves: int = len(turn_result)
    turn_str: str = ''

    for movement in turn_result:
        turn_str += f'{movement}-{turn_result[movement]}'
        num_moves -= 1
        if num_moves != 0:
            turn_str += ' '

    if out_type == 'default' or out_type == 'neither':
        print(turn_str)
    else:
        return turn_str

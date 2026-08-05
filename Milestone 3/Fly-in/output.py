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
        self.display = pygame.display.set_mode((1800, 1000))
        pygame.display.set_caption('Fly-in')
        self.display.fill((0, 0, 0))

        font = pygame.font.Font(None, 20)

        for x in self.graph:
            for y in self.graph[x]:
                pygame.draw.rect(self.display, (0, 0, 255),
                                 [x * 180, y * 180, 100, 75],
                                 0)
                text = font.render(self.graph[x][y].name, True,
                                   (255, 255, 255))
                text_rect = text.get_rect()
                text_rect.center = (x * 180 + 50, y * 180 + 10)
                self.display.blit(text, text_rect)

        for link in self.connections:
            hub1: HubStruct = link.init_hub
            for hub2 in link.linked_hubs:
                if hub1.x > hub2.x:
                    if hub1.y == hub2.y:
                        pygame.draw.line(self.display, (255, 0, 0),
                                         [hub1.x * 180 - 10,
                                         hub1.y * 180 + 37],
                                         [hub2.x * 180 + 110,
                                         hub2.y * 180 + 37],
                                         3)
                    elif hub1.y < hub2.y:
                        pygame.draw.line(self.display, (255, 0, 0),
                                         [hub1.x * 180 - 110,
                                         hub1.y * 180 + 85],
                                         [hub2.x * 180 + 10,
                                         hub2.y * 180 - 10],
                                         3)
                    if hub1.y > hub2.y:
                        pygame.draw.line(self.display, (255, 0, 0),
                                         [hub1.x * 180 - 110,
                                         hub1.y * 180 - 10],
                                         [hub2.x * 180 + 10,
                                         hub2.y * 180 + 85],
                                         3)
                elif hub1.x < hub2.x:
                    if hub1.y == hub2.y:
                        pygame.draw.line(self.display, (255, 0, 0),
                                         [hub1.x * 180 + 110,
                                         hub1.y * 180 + 37],
                                         [hub2.x * 180 - 10,
                                         hub2.y * 180 + 37],
                                         3)
                    elif hub1.y < hub2.y:
                        pygame.draw.line(self.display, (255, 0, 0),
                                         [hub1.x * 180 + 110,
                                         hub1.y * 180 + 85],
                                         [hub2.x * 180 - 10,
                                         hub2.y * 180 - 10],
                                         3)
                    if hub1.y > hub2.y:
                        pygame.draw.line(self.display, (255, 0, 0),
                                         [hub1.x * 180 + 110,
                                         hub1.y * 180 - 10],
                                         [hub2.x * 180 - 10,
                                         hub2.y * 180 + 85],
                                         3)
                else:
                    if hub1.y == hub2.y:
                        pygame.draw.line(self.display, (255, 0, 0),
                                         [hub1.x * 180 + 50,
                                         hub1.y * 180 + 37],
                                         [hub2.x * 180 + 50,
                                         hub2.y * 180 + 37],
                                         3)
                    elif hub1.y < hub2.y:
                        pygame.draw.line(self.display, (255, 0, 0),
                                         [hub1.x * 180 + 50,
                                         hub1.y * 180 + 85],
                                         [hub2.x * 180 + 50,
                                         hub2.y * 180 - 10],
                                         3)
                    if hub1.y > hub2.y:
                        pygame.draw.line(self.display, (255, 0, 0),
                                         [hub1.x * 180 + 50,
                                         hub1.y * 180 - 10],
                                         [hub2.x * 180 + 50,
                                         hub2.y * 180 + 85],
                                         3)

        pygame.display.update()
        self.copy_display = self.display.copy()

    def sim_updater(self) -> None:
        self.display.blit(self.copy_display, (0, 0))
        pygame.display.update()
        font = pygame.font.Font(None, 15)
        offset: dict = {}
        for key in self.current_state:
            if key == 'turn':
                continue
            elif self.current_state[key].count('-') == 1:
                start_x, start_y = 0, 0
                end_x, end_y = 0, 0
                start_hub: str = self.current_state[key].split('-')[0]
                end_hub: str = self.current_state[key].split('-')[1]
                for hub in self.hubs:
                    if start_hub == hub.name:
                        start_x, start_y = hub.x, hub.y
                    elif end_hub == hub.name:
                        end_x, end_y = hub.x, hub.y
                mid_x, mid_y = (start_x + end_x) / 2, (start_y + end_y) / 2

                try:
                    offset.get(self.current_state[key])
                    offset[self.current_state[key]] += 10
                except KeyError:
                    offset[self.current_state[key]] = 40
                text = font.render(key, True,
                                   (0, 255, 0))
                text_rect = text.get_rect()
                text_rect.center = (mid_x * 180 + 60,
                                    mid_y * 180 + offset[
                                        self.current_state[key]])

                self.display.blit(text, text_rect)

                pygame.draw.circle(self.display, (0, 255, 0),
                                   [mid_x * 180 + 50, mid_y * 180 + 40],
                                   3.14)
            for hub in self.hubs:
                if self.current_state[key] == hub.name:
                    try:
                        offset.get(hub.name)
                        offset[hub.name] += 10
                    except KeyError:
                        offset[hub.name] = 40
                    text = font.render(key, True,
                                       (0, 255, 0))
                    text_rect = text.get_rect()
                    text_rect.center = (hub.x * 180 + 60,
                                        hub.y * 180 + offset[hub.name])
                    self.display.blit(text, text_rect)

                    pygame.draw.circle(self.display, (0, 255, 0),
                                       [hub.x * 180 + 50, hub.y * 180 + 40],
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
            self.current_state = setup_dict
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
    min_x: int = 1
    min_y: int = 1

    # normalize hub x & y co-ordinates to fit in window
    for hub in hubs:
        if hub.x < min_x:
            min_x = hub.x
        if hub.y < min_y:
            min_y = hub.y
    if min_x < 1:
        for hub in hubs:
            hub.x += (min_x * -1) + 0.1
    if min_y < 1:
        for hub in hubs:
            hub.y += (min_y * -1) + 0.1

    # setup dictionary structure for rows from x and columns from y
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

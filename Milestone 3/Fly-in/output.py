import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from infrastructure import HubStruct
from rich import print as rprint


class sim_state:
    def __init__(self, config: dict, output_type: str):
        self.num_hubs: int = config['total_hubs']
        self.hubs: dict = config['hubs']
        self.goal_name: str = config['goal_name']
        self.connections: list = config['connections']
        self.drones: list = [f'D{drone.id}' for drone in config['drones']]
        self.current_turn: int = 0
        self.total_cost: int = 0
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

        for i in self.graph:
            for j in self.graph[i]:
                x: int = i
                y: int = j
                if i > 9:
                    y += x - 9.5
                    x = 9
                config_color: str = self.graph[i][j].color
                if config_color == 'green':
                    hub_color = pygame.Color('green4')
                elif config_color == 'blue':
                    hub_color = pygame.Color('dodgerblue3')
                elif config_color == 'red':
                    hub_color = pygame.Color('red4')
                elif config_color == 'black':
                    hub_color = pygame.Color('white')
                elif config_color == 'rainbow':
                    hub_color = pygame.Color('violetred')
                else:
                    try:
                        hub_color = pygame.Color(self.graph[i][j].color)
                    except ValueError:
                        hub_color = pygame.Color('snow3')
                pygame.draw.rect(self.display, (hub_color),
                                 [x * 180, y * 180, 100, 75],
                                 0)
                text = font.render(self.graph[i][j].name, True,
                                   (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (x * 180 + 50, y * 180 + 10)
                self.display.blit(text, text_rect)

        link_color = pygame.Color('snow3')
        for link in self.connections:
            hub1: HubStruct = link.init_hub
            for hub2 in link.linked_hubs:
                x1: int = hub1.x
                y1: int = hub1.y
                x2: int = hub2.x
                y2: int = hub2.y
                if hub1.x > 9:
                    if hub2.x <= 9:
                        y1 += x1 - 9
                        x1 = 9
                    else:
                        y1 += x1 - 9.25
                        x1 = 8.625
                if hub2.x > 9:
                    if x1 == 8.625:
                        y2 += x2 - 9.75
                        x2 = 9.29
                    else:
                        y2 += x2 - 9.5
                        x2 = 9
                if hub1.x > hub2.x:
                    if hub1.y == hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 - 10,
                                         y1 * 180 + 37],
                                         [x2 * 180 + 110,
                                         y2 * 180 + 37],
                                         3)
                    elif hub1.y < hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 10,
                                         y1 * 180 + 85],
                                         [x2 * 180 + 110,
                                         y2 * 180 - 10],
                                         3)
                    if hub1.y > hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 - 10,
                                         y1 * 180 - 10],
                                         [x2 * 180 + 110,
                                         y2 * 180 + 85],
                                         3)
                elif hub1.x < hub2.x:
                    if hub1.y == hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 110,
                                         y1 * 180 + 37],
                                         [x2 * 180 - 10,
                                         y2 * 180 + 37],
                                         3)
                    elif hub1.y < hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 110,
                                         y1 * 180 + 85],
                                         [x2 * 180 - 10,
                                         y2 * 180 - 10],
                                         3)
                    if hub1.y > hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 110,
                                         y1 * 180 - 10],
                                         [x2 * 180 - 10,
                                         y2 * 180 + 85],
                                         3)
                else:
                    if hub1.y == hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 50,
                                         y1 * 180 + 37],
                                         [x2 * 180 + 50,
                                         y2 * 180 + 37],
                                         3)
                    elif hub1.y < hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 50,
                                         y1 * 180 + 85],
                                         [x2 * 180 + 50,
                                         y2 * 180 - 10],
                                         3)
                    if hub1.y > hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 50,
                                         y1 * 180 - 10],
                                         [x2 * 180 + 50,
                                         y2 * 180 + 85],
                                         3)

        pygame.display.update()
        self.copy_display = self.display.copy()

    def sim_updater(self) -> None:
        self.display.blit(self.copy_display, (0, 0))
        pygame.display.update()
        font = pygame.font.Font(None, 15)
        drone_color = pygame.Color('springgreen')
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
                if mid_x > 9:
                    mid_y += mid_x - 9.5
                    mid_x = 9

                try:
                    offset.get(self.current_state[key])
                    offset[self.current_state[key]] += 10
                except KeyError:
                    offset[self.current_state[key]] = 50
                text = font.render(key, True,
                                   (drone_color))
                text_rect = text.get_rect()
                text_rect.center = (mid_x * 180 + 60,
                                    mid_y * 180 + offset[
                                        self.current_state[key]])

                self.display.blit(text, text_rect)

                pygame.draw.circle(self.display, (drone_color),
                                   [mid_x * 180 + 50, mid_y * 180 + 50],
                                   3.14)
            for hub in self.hubs:
                if self.current_state[key] == hub.name:
                    try:
                        offset.get(hub.name)
                        offset[hub.name] += 10
                    except KeyError:
                        offset[hub.name] = 40
                    x: int = hub.x
                    y: int = hub.y
                    if x > 9:
                        y += x - 9.5
                        x = 9
                    text = font.render(key, True,
                                       (drone_color))
                    text_rect = text.get_rect()
                    text_rect.center = (x * 180 + 60,
                                        y * 180 + offset[hub.name])
                    self.display.blit(text, text_rect)

                    pygame.draw.circle(self.display, (drone_color),
                                       [x * 180 + 50, y * 180 + 40],
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
        self.turn_saver.append(turn_print(init_turn, self.output_type,
                                          self.hubs))
        if self.output_type == 'pygame' or self.output_type == 'both':
            self.graph = create_graph(self.hubs)
            self.sim_init()
            self.sim_updater()

        return setup_dict

    def update_state(self, turn_result: dict) -> None:
        self.current_turn += 1
        self.current_state['turn'] = self.current_turn

        for drone in turn_result:
            self.total_cost += 1
            self.current_state[drone] = turn_result[drone]

        self.turn_saver.append(turn_print(turn_result, self.output_type,
                                          self.hubs))
        if self.output_type == 'pygame' or self.output_type == 'both':
            self.sim_updater()

    def produce_end(self) -> None:
        num_drones: int = len(self.drones)

        if self.output_type == 'pygame' or self.output_type == 'both':
            for turn in self.turn_saver:
                rprint(turn)
        print('-' * 16)
        print(f"Turns to complete full sim: {self.current_turn}")
        print("Average number of drones moved per turn:",
              f"{self.total_cost / self.current_turn}")
        print(f"Average turns used per drone: {self.total_cost / num_drones}")
        print(f"Sum of turns taken by drones: {self.total_cost}")


def create_graph(hubs: list) -> dict:
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


def turn_print(turn_result: dict, out_type: str, hubs: list) -> str:
    num_moves: int = len(turn_result)
    turn_str: str = ''
    colour: str = ''

    for movement in turn_result:
        colour = ''
        for hub in hubs:
            if hub.name == turn_result[movement]:
                colour = hub.color
        if colour == '':
            colour = 'purple'
        turn_str += f'{movement}-[{colour}]{turn_result[movement]}[/{colour}]'
        num_moves -= 1
        if num_moves != 0:
            turn_str += ' '

    if out_type != 'pygame':
        rprint(turn_str)
    else:
        return turn_str

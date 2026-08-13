import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from infrastructure import Hub
from rich import print as rprint
import time
from typing import Any


class sim_state:
    def __init__(self, config: dict[Any, Any], output_type: str):
        self.num_hubs: int = config['total_hubs']
        self.hubs: dict[Any, Any] = config['hubs']
        self.goal_name: str = config['goal_name']
        self.connections: list[Any] = config['connections']
        self.drones: list[Any] = [f'D{drone.id}' for drone in config['drones']]
        self.current_turn: int = 0
        self.total_cost: int = 0
        self.output_type: str = output_type
        self.init_check: bool = False
        self.turn_saver: list[Any] = []
        if self.output_type == 'pygame' or self.output_type == 'both':
            self.display = pygame.display.set_mode((1800, 1000))
            self.copy_display = self.display
        self.current_state: dict[Any, Any] = self.setup_state()
        self.graph: dict[Any, Any] = {}

    # pygame setup
    def sim_init(self) -> None:
        pygame.init()
        pygame.display.set_caption('Fly-in')
        self.display.fill((0, 0, 0))

        font = pygame.font.Font(None, 20)

        if self.num_hubs > 35:
            self.display = pygame.display.set_mode((1800, 600))

        # creating the hub visuals
        for i in self.graph:
            for j in self.graph[i]:
                x: float = i
                y: float = j
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
                elif config_color == 'yellow':
                    hub_color = pygame.Color('yellow3')
                elif config_color == 'lime':
                    hub_color = pygame.Color('limegreen')
                elif config_color == 'cyan':
                    hub_color = pygame.Color('cyan4')
                elif config_color == 'rainbow':
                    hub_color = pygame.Color('violetred')
                else:
                    try:
                        hub_color = pygame.Color(self.graph[i][j].color)
                    except ValueError:
                        hub_color = pygame.Color('snow3')
                text = font.render(self.graph[i][j].name, True,
                                   (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (int(x * 180 + 50), int(y * 180 + 10))
                if self.num_hubs > 35:
                    pygame.draw.rect(self.display, (hub_color),
                                     ((x * 180, y * 180), (50, 36)),
                                     0)
                    font = pygame.font.Font(None, 10)
                    text_rect.center = (int(x * 180 + 25), int(y * 180 + 5))
                else:
                    pygame.draw.rect(self.display, (hub_color),
                                     ((x * 180, y * 180), (100, 75)),
                                     0)
                self.display.blit(text, text_rect)

        # creating the connections visuals
        link_color = pygame.Color('snow3')
        size_adjust: int = 0
        if self.num_hubs > 35:
            size_adjust = -6
        for link in self.connections:
            hub1: Hub = link.init_hub
            for hub2 in link.linked_hubs:
                x1: float = hub1.x
                y1: float = hub1.y
                x2: float = hub2.x
                y2: float = hub2.y
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
                                         [x1 * 180 - 10 - size_adjust,
                                         y1 * 180 + 37 + size_adjust],
                                         [x2 * 180 + 110 + size_adjust,
                                         y2 * 180 + 37 + size_adjust],
                                         3)
                    elif hub1.y < hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 10 + size_adjust * 2,
                                         y1 * 180 + 85 + size_adjust * 7],
                                         [x2 * 180 + 110 + size_adjust * 9,
                                         y2 * 180 - 10 - size_adjust * 0.5],
                                         3)
                    if hub1.y > hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 - 10 + size_adjust * 2,
                                         y1 * 180 - 10 + size_adjust * 3.25],
                                         [x2 * 180 + 110 + size_adjust * 7,
                                         y2 * 180 + 85 + size_adjust * 3.25],
                                         3)
                elif hub1.x < hub2.x:
                    if hub1.y == hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 110 + size_adjust * 8,
                                         y1 * 180 + 37 + size_adjust * 3],
                                         [x2 * 180 - 10 + size_adjust,
                                         y2 * 180 + 37 + size_adjust * 3],
                                         3)
                    elif hub1.y < hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 110 + size_adjust * 10,
                                         y1 * 180 + 85 + size_adjust * 7],
                                         [x2 * 180 - 10 - size_adjust * 0.5,
                                         y2 * 180 - 10 - size_adjust * 1],
                                         3)
                    if hub1.y > hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 110 + size_adjust * 9,
                                         y1 * 180 - 10 - size_adjust * 1],
                                         [x2 * 180 - 10 - size_adjust * 0.5,
                                         y2 * 180 + 85 + size_adjust * 7],
                                         3)
                else:
                    if hub1.y == hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 50 + size_adjust,
                                         y1 * 180 + 37 + size_adjust],
                                         [x2 * 180 + 50 + size_adjust,
                                         y2 * 180 + 37 + size_adjust],
                                         3)
                    elif hub1.y < hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 50 + size_adjust * 4,
                                         y1 * 180 + 85 + size_adjust * 3.25],
                                         [x2 * 180 + 50 + size_adjust * 4,
                                         y2 * 180 - 10 + size_adjust * 3.25],
                                         3)
                    if hub1.y > hub2.y:
                        pygame.draw.line(self.display, (link_color),
                                         [x1 * 180 + 50 + size_adjust * 4,
                                         y1 * 180 - 10 + size_adjust * 3.25],
                                         [x2 * 180 + 50 + size_adjust * 4,
                                         y2 * 180 + 85 + size_adjust * 3.25],
                                         3)

        pygame.display.update()
        self.copy_display = self.display.copy()

    def sim_updater(self) -> None:
        # resetting the screen to be the copy to remove the old drones
        self.display.blit(self.copy_display, (0, 0))
        pygame.display.update()
        font = pygame.font.Font(None, 15)
        drone_color = pygame.Color('springgreen')
        offset: dict[Any, Any] = {}

        # searching for drones that might be on connections
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
                if self.num_hubs > 35:
                    text_rect.center = (int(mid_x * 180 + 40),
                                        int(mid_y * 180 + offset[
                                            self.current_state[key]]) - 30)
                else:
                    text_rect.center = (int(mid_x * 180 + 60),
                                        int(mid_y * 180 + offset[
                                            self.current_state[key]]))

                self.display.blit(text, text_rect)

                if self.num_hubs > 35:
                    pygame.draw.circle(self.display, (drone_color),
                                       [mid_x * 180 + 25, mid_y * 180 + 20],
                                       3.14)
                else:
                    pygame.draw.circle(self.display, (drone_color),
                                       [mid_x * 180 + 50, mid_y * 180 + 50],
                                       3.14)

            # creating the drones that are on hubs
            for hub in self.hubs:
                if self.current_state[key] == hub.name:
                    try:
                        offset.get(hub.name)
                        offset[hub.name] += 10
                    except KeyError:
                        offset[hub.name] = 40
                    x: float = hub.x
                    y: float = hub.y
                    if x > 9:
                        y += x - 9.5
                        x = 9
                    text = font.render(key, True,
                                       (drone_color))
                    text_rect = text.get_rect()
                    if self.num_hubs > 35:
                        text_rect.center = (int(x * 180 + 40),
                                            int(y * 180 + offset[hub.name] -
                                                20))
                    else:
                        text_rect.center = (int(x * 180 + 60),
                                            int(y * 180 + offset[hub.name]))
                    self.display.blit(text, text_rect)

                    if self.num_hubs > 35:
                        pygame.draw.circle(self.display, (drone_color),
                                           [x * 180 + 25, y * 180 + 20],
                                           3.14)
                    else:
                        pygame.draw.circle(self.display, (drone_color),
                                           [x * 180 + 50, y * 180 + 40],
                                           3.14)
        pygame.display.flip()

    def setup_state(self) -> dict[Any, Any]:
        setup_dict: dict[Any, Any] = {'turn': self.current_turn}
        init_turn: dict[Any, Any] = {}

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

    def update_state(self, turn_result: dict[Any, Any]) -> None:
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
        wait_close: bool = False

        # print out all the turns to the terminal after pygame is finished
        if self.output_type == 'pygame':
            for turn in self.turn_saver:
                rprint(turn)

        # allow the user to end pygame/close window gracefully
        if self.output_type == 'pygame' or self.output_type == 'both':
            wait_close = True
        while wait_close is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait_close = False
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_ESCAPE or key == pygame.K_SPACE:
                        wait_close = False

        # print statistics
        print('-' * 16)
        print(f"Turns to complete full sim: {self.current_turn}")
        print("Average number of drones moved per turn:",
              f"{self.total_cost / self.current_turn:.2f}")
        print("Average turns used per drone:",
              f"{self.total_cost / num_drones:.2f}")
        print(f"Sum of turns taken by drones: {self.total_cost}")


def create_graph(hubs: dict[Any, Any]) -> dict[Any, Any]:
    row_track: dict[Any, Any] = {}
    graph_track: dict[Any, Any] = {}
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

    if len(hubs) > 35:
        for hub in hubs:
            hub.x /= 2.5
            hub.y /= 2.5

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


def turn_print(turn_result: dict[Any, Any], out_type: str,
               hubs: dict[Any, Any]) -> str:
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
        if out_type != 'both':
            time.sleep(0.5)
    return turn_str

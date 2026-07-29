

class sim_state:
    def __init__(self, config: dict, output_type: str):
        self.num_hubs: int = config['total_hubs']
        self.hubs: dict = config['hubs']
        self.connections: list = [link.hubs for link in config['connections']]
        self.drones: list = [f'D{drone.id}' for drone in config['drones']]
        self.current_turn: int = 0
        self.output_type: str = output_type
        self.current_state: dict = self.setup_state()
        self.graph: list = None

    def setup_state(self) -> dict:
        setup_dict: dict = {'turn': self.current_turn}

        for drone in self.drones:
            setup_dict[drone] = 'start'
        if self.output_type != 'neither' and self.output_type != 'default':
            self.graph = create_graph(self.hubs, self.connections)

        return setup_dict

    def update_state(self, turn_result: dict) -> None:
        self.current_turn += 1
        self.current_state['turn'] = self.current_turn

        for drone in turn_result:
            self.current_state[drone] = turn_result[drone]

        handle_output(self.current_state, turn_result, self.output_type)


def handle_output(sim_state: dict, turn_result: dict, out_type: str) -> None:
    if out_type == 'terminal':
        print(sim_state)
    elif out_type == 'pygame':
        print("omg look a visual *mind_blown.gif*")
    elif out_type == 'both':
        print(sim_state)
        print("omg look a visual and terminal stuff *EXTREME_mind_blown.gif*")
    else:
        turn_print(turn_result)


def create_graph(hubs: list, links: list) -> list:
    max_height: int = 0
    min_height: int = 0
    num_columns: int = 0
    max_width: int = 0
    min_width: int = 0
    num_rows: int = 0
    cell_width: int = 0
    blank_cell: str = ''
    graph: list = []

    # set base stats
    for hub in hubs:
        if hub.location[0] > max_width:
            max_width = hub.location[0]
        elif hub.location[0] < min_width:
            min_width = hub.location[0]
        if hub.location[1] > max_height:
            max_height = hub.location[1]
        elif hub.location[0] < min_height:
            min_height = hub.location[0]
            print(min_height)
        if len(hub.name) > cell_width:
            cell_width = len(hub.name)

    # normalize all x and y values
    print(f'{min_width}         {min_height}')
    if min_width < 0:
        for hub in hubs:
            hub.location[0] += (min_width * -1)
    elif min_width > 0:
        for hub in hubs:
            hub.location[0] -= min_width
    if min_height < 0:
        for hub in hubs:
            hub.location[1] += (min_height * -1)
    elif min_height > 0:
        for hub in hubs:
            hub.location[1] -= min_height

    num_columns = (max_width - min_width) * 2 + 1
    num_rows = (max_height - min_height) * 2 + 1
    blank_cell = ' ' * cell_width

    for x in range(0, num_columns):
        temp_row: list = []
        for y in range(0, num_rows):
            temp_row.append(blank_cell)
        graph.append(temp_row)
        # print(graph[x])

    for hub in hubs:
        graph[hub.location[0] * 2][hub.location[1] * 2] = f'x{hub.location[0]}y{hub.location[1]}-{hub.name}'
    for row in graph:
        print(row)


def turn_print(turn_result: dict) -> None:
    num_moves: int = len(turn_result)
    for movement in turn_result:
        print(f'{movement}-{turn_result[movement]}', end='')
        num_moves -= 1
        if num_moves != 0:
            print(' ', end='')
        else:
            print('')

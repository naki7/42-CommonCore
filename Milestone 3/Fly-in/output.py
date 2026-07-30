

class sim_state:
    def __init__(self, config: dict, output_type: str):
        self.num_hubs: int = config['total_hubs']
        self.hubs: dict = config['hubs']
        self.connections: list = [link.hubs for link in config['connections']]
        self.drones: list = [f'D{drone.id}' for drone in config['drones']]
        self.current_turn: int = 0
        self.output_type: str = output_type
        self.init_check: bool = False
        self.turn_saver: list = []
        self.current_state: dict = self.setup_state()
        self.graph: list = None

    def setup_state(self) -> dict:
        setup_dict: dict = {'turn': self.current_turn}
        init_turn: dict = {}

        for drone in self.drones:
            setup_dict[drone] = 'start'
            if self.init_check is False:
                init_turn[drone] = 'start'
        if self.init_check is False:
            self.init_check = True
        self.turn_saver.append(turn_print(init_turn, self.output_type))
        if self.output_type != 'neither' and self.output_type != 'default':
            self.graph = create_graph(self.hubs, self.connections)
            print(setup_dict)

        return setup_dict

    def update_state(self, turn_result: dict) -> None:
        self.current_turn += 1
        self.current_state['turn'] = self.current_turn

        for drone in turn_result:
            self.current_state[drone] = turn_result[drone]

        self.turn_saver.append(turn_print(turn_result, self.output_type))
        handle_output(self.current_state, turn_result, self.output_type)

    def produce_end(self) -> None:
        for turn in self.turn_saver:
            print(turn)


def handle_output(sim_state: dict, turn_result: dict, out_type: str) -> None:
    if out_type == 'terminal':
        print(sim_state)
    elif out_type == 'pygame':
        print("omg look a visual *mind_blown.gif*")
    elif out_type == 'both':
        print(sim_state)
        print("omg look a visual and terminal stuff *EXTREME_mind_blown.gif*")


def create_graph(hubs: list, links: list) -> dict:
    row_track: dict = {}
    graph_track: dict = {}

    for hub in hubs:
        try:
            row_track.get(hub.x)
            row_track[hub.x].append(hub)
        except KeyError:
            row_track[hub.x] = [hub]
    print(row_track)

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



class sim_state:
    def __init__(self, config: dict, output_type: str):
        self.num_hubs: int = config['total_hubs']
        self.hubs: dict = {hub.name: hub.color for hub in config['hubs']}
        self.connections: list = [link.hubs for link in config['connections']]
        self.drones: list = [f'D{drone.id}' for drone in config['drones']]
        self.current_turn: int = 0
        self.current_state: dict = self.setup_state()
        self.output_type: str = output_type
        self.graph: list = None

    def setup_state(self) -> dict:
        setup_dict: dict = {'turn': self.current_turn}

        for drone in self.drones:
            setup_dict[drone] = 'start'
        if self.output_type != 'neither' and self.output_type != 'default':
            print(setup_dict)

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


def turn_print(turn_result: dict) -> None:
    num_moves: int = len(turn_result)
    for movement in turn_result:
        print(f'{movement}-{turn_result[movement]}', end='')
        num_moves -= 1
        if num_moves != 0:
            print(' ', end='')
        else:
            print('')

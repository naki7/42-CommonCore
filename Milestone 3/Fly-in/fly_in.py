from infrastructure import base_structure, Hub, Connection
from typing import Any
from parser import parser_main
from output import sim_state
from dijkstra import dijkstra
from astar import astar
import pygame
import time
import sys


def get_connect(current: Hub, next: Hub) -> Any:
    current_name: str = f'{current.name}-{next.name}'
    reverse_name: str = f'{next.name}-{current.name}'

    for link in current.connections:
        if link.name == current_name or link.name == reverse_name:
            return link
    return None


def path_finder(drones: list[Any], state: sim_state) -> None:
    searching_drones: int = len(drones)

    while searching_drones > 0:
        turn_result: dict[Any, Any] = {}
        for drone in drones:

            # check at start of loop to allow pygame to be closed
            if state.output_type == 'both' or state.output_type == 'pygame':
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        state.output_type = 'default'
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            state.output_type = 'default'
                            pygame.quit()

            if drone.status == 'searching':
                prev_len: int = drone.path_len

                # finds the best next turns for the current drone
                if drone.next_hub is None:
                    if state.num_hubs > 10:
                        temp: list[Any] = dijkstra(drone.current_path,
                                                   drone.path_len,
                                                   state.goal_name)
                    else:
                        temp = astar(drone.current_path, drone.path_len,
                                     state.goal_name)

                else:
                    temp = [drone.next_hub]
                temp_len: int = len(temp) + prev_len

                # cleans out the second hub so turns print one at a time
                if temp_len - prev_len == 2:
                    temp.pop(1)
                    temp_len -= 1

                # goes through the previous hubs visited by the drone to clear
                # the space and make capacity available and also appends the
                # next hub it moves to in current turn
                if temp_len > prev_len:
                    for i in range(0, temp_len):
                        if i < prev_len:
                            if drone.current_path[i].occupants.count(
                                                            drone) != 0:
                                drone.current_path[i].remove_drone(drone)
                        else:
                            curr_i: int = i - prev_len
                            if temp[curr_i].type != 'restricted':
                                if temp[curr_i].name == state.goal_name:
                                    pass

                                drone.current_path.append(temp[curr_i])
                                temp[curr_i].add_drone(drone)
                            else:
                                if drone.next_hub is None:
                                    prev_i: int = prev_len - 1
                                    drone.next_hub = temp[curr_i]
                                    connection: Connection = get_connect(
                                        drone.current_path[prev_i],
                                        drone.next_hub
                                    )
                                    connection.add_drone(drone)
                                    drone.current_path.append(connection)
                                else:
                                    drone.current_path.append(drone.next_hub)
                                    drone.next_hub.add_drone(drone)
                                    drone.next_hub = None
                            local_name: str = drone.current_path[i].name
                            turn_result[f'D{drone.id}'] = local_name
                drone.path_len = temp_len
                if state.output_type == 'pygame':
                    if state.num_hubs < 15:
                        time.sleep(0.4)
                    elif state.num_hubs < 20:
                        time.sleep(0.25)
                    elif state.num_hubs < 35:
                        time.sleep(0.1)
                    else:
                        time.sleep(0.05)
                elif state.output_type == 'both':
                    if state.num_hubs < 15:
                        time.sleep(0.4)
                    elif state.num_hubs < 20:
                        time.sleep(0.25)
                    elif state.num_hubs < 35:
                        time.sleep(0.1)
                    else:
                        time.sleep(0.05)

                # sets drone to no longer be looped
                if drone.current_path[
                        drone.path_len - 1].name == state.goal_name:
                    drone.status = 'plotted'

            # sets drone count to reduce and eventually ending loop
            if drone.status == 'plotted':
                searching_drones -= 1
                drone.status = 'goal'

        # update state class with the new locations
        state.update_state(turn_result)

    state.produce_end()


def main() -> None:
    output_type: str = 'default'
    preplanned_outputs: list[Any] = ['terminal', 'pygame', 'both', 'default']

    if len(sys.argv) < 2:
        print("Invalid command line input",
              "Please try: python3 fly-in.py ./maps/easy/01_linear_path.txt",
              sep='\n')
        return
    elif len(sys.argv) == 2 or len(sys.argv) == 3:
        try:
            test = open(sys.argv[1], 'r')
        except FileNotFoundError as alert:
            print(alert)
            quit()
        test.close()

        if len(sys.argv) == 3:
            if preplanned_outputs.count(f'{sys.argv[2]}') == 1:
                output_type = sys.argv[2]
            else:
                print('Invalid output type; using default output')
    else:
        print("Invalid command line input",
              "Please try: python3 fly-in.py ./maps/easy/01_linear_path.txt",
              sep='\n')
        quit()

    sim_config: dict[Any, Any] = base_structure(parser_main(sys.argv[1]))

    state_saver: sim_state = sim_state(sim_config, output_type)
    path_finder(sim_config['drones'], state_saver)


if __name__ == '__main__':
    main()

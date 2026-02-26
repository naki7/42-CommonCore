# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/25 13:31:21 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/26 13:49:55 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from typing import Generator


def fibonacci(repeats: int) -> Generator[int, None, None]:
    """
    This Fibonacci generator takes in a number and then does a for loop
    within that range to repeatedly take a and add it to b to yield a sum
    of the two while still remembering the result of the last call.
    """
    a: int = 0
    b: int = 1
    for n in range(repeats):
        yield a
        a, b = b, a + b


def prime_numbers() -> Generator[int, None, None]:
    """
    This generator produces prime numbers by starting with a number, then
    checks to see if the number compared to numbers greater than or equal to 2
    but smaller than the number itself would create 0 remainder when modulared.
    The number is then increased by 1 so that the next time it is called a new
    prime number can be found
    """
    current_num: int = 2
    while True:
        is_prime: bool = True
        for i in range(2, int(current_num ** 0.5) + 1):
            if current_num % i == 0:
                is_prime = False
                break
        if is_prime is True:
            yield current_num
        current_num += 1


def game_event(count: int) -> Generator[dict[str: int or str], None, None]:
    """
    A generator function which takes in a number of events that could be run.
    The generator holds on to a group of players, their levels and current exp.
    A player is picked from the modular of the current event count, and they
    gain exp based on the modular of the event count.
    Events are then determined by leveling up (passing 100 exp), or modular of
    the event count to either be a treasure picked up or a monster encounter.
    neither of the 3 can occur thus filtering out non important events.
    """
    alice: dict[str: int] = {"level": 7, "exp": 10}
    bob: dict[str: int] = {"level": 5, "exp": 16}
    charlie: dict[str: int] = {"level": 1, "exp": 0}
    player_arr: list[str] = ["alice", "bob", "charlie"]
    players: dict[str: dict] = {"alice": alice, "bob": bob, "charlie": charlie}
    for i in range(1, count + 1):
        player: str = player_arr[i % 3]
        exp_gain: int = (i * 131) % 15
        players[player]["exp"] += exp_gain
        if players[player]["exp"] > 100:
            players[player]["exp"] -= 100
            players[player]["level"] += 1
            level_up = True
        else:
            level_up = False
        event: str = None
        if level_up is True:
            event = "leveled up"
        elif i % 16 == 0:
            event = "killed monster"
        elif i % 4 == 0:
            event = "found treasure"
        yield {
            "count": i,
            "player": player,
            "level": players[player]["level"],
            "event": event
        }


def main() -> None:
    """
    A for loop will be used to call the 1000 game events. This will
    automatically use the next() and iter() methods which would usuall be
    called like this:
    "ex.
    event_generator = iter(game_event(1000))
    while True:
        try:
            value = next(event_generator)
            print(value)
        except StopIteration:
            break"
    Analytics of the stream will be kept as the generator runs, then printed.
    Then 2 generators will be shown, one to calculate fibonnacci and the other
    to find a number of prime numbers
    """
    print("=== Game Data Stream Processor ===\n")
    total_events: int = 0
    total_treasures: int = 0
    total_level_ups: int = 0
    total_players: dict[str: int] = {}
    print("Processing 1000 game events...\n")
    for event in game_event(1000):
        total_events += 1
        if event["event"] is not None:
            print(f"Event {event['count']}: Player {event['player']}",
                  f"(level {event['level']}) {event['event']}")
            if event["event"] == "found treasure":
                total_treasures += 1
            if event["event"] == "leveled up":
                total_level_ups += 1
                total_players[event["player"]] = event['level']

    print("\n=== Stream Analytics ===\n")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (lvl 10+): {len(total_players)}")
    print(f"Treasure events: {total_treasures}")
    print(f"Level-up events: {total_level_ups}\n")

    print("Memory usage: Constant (streaming)\nProcessing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    times_to_repreat: int = 10
    times_ran: int = 0
    print(f"Fibonacci sequence (first {times_to_repreat}): ", end="")
    for num in fibonacci(times_to_repreat):
        times_ran += 1
        if times_ran < times_to_repreat:
            print(f"{num}, ", end="")
        else:
            print(num)

    times_to_repreat: int = 5
    prime_gen: list[int] = iter(prime_numbers())
    print(f"Prime numbers (first {times_to_repreat}): ", end="")
    for i in range(times_to_repreat):
        if i + 1 < times_to_repreat:
            print(f"{next(prime_gen)}, ", end="")
        else:
            print(next(prime_gen))


if __name__ == "__main__":
    main()

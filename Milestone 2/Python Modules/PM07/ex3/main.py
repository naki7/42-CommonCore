from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory as Factory
from ex3.AggressiveStrategy import AggressiveStrategy as Strategy


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    fantasy: Factory = Factory()
    aggressive: Strategy = Strategy()
    base_engine: GameEngine = GameEngine()
    base_engine.configure_engine(fantasy, aggressive)
    status_result: dict = base_engine.get_engine_status()
    for result in status_result:
        print(f"{result}: {status_result[result]}")

    print("\nSimulating aggressive turn...")
    turn_result: dict = base_engine.simulate_turn()
    i: int = 0
    print("Hand: [", end="")
    for card in turn_result["Hand"]:
        print(f"{turn_result['Hand'][card].name}",
              f"({turn_result['Hand'][card].cost})", end="")
        if i < 2:
            i += 1
            print(", ", end="")
        else:
            print("]\n")

    for result in turn_result:
        if result == "Hand":
            continue
        elif result == "Actions":
            print("Turn execution:")
            print("Stratergy:",
                  f"{turn_result['Game Report']['strategy_used']}")
            print(f"{result}: {turn_result[result]}\n")
        elif result == "Game Report":
            print(f"{result}:\n{turn_result[result]}\n")

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()

from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        super().__init__()

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.mana = 8

    def simulate_turn(self) -> dict:
        deck: dict = self.factory.create_themed_deck(3)
        saved_deck: dict = self.factory.create_themed_deck(3)
        strategy_name: str = self.strategy.get_strategy_name()
        turn_result: dict = self.strategy.execute_turn(deck, ["Enemy Player"])
        sim_result: dict = {
            "Hand": saved_deck,
            "Actions": turn_result,
            "Game Report": {
                "turns_simulated": 1,
                "strategy_used": strategy_name,
                "total_damage": turn_result["damage_dealt"],
                "cards_created": len(saved_deck)
            }
        }
        return sim_result

    def get_engine_status(self) -> dict:
        factory: str = self.factory.class_name
        strategy: str = self.strategy.get_strategy_name()
        types: dict = self.factory.get_supported_types()
        results_dict: dict = {
            "Factory": factory,
            "Strategy": strategy,
            "Available types": types
        }
        return results_dict

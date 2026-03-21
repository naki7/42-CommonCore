from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        return game_state

    def get_card_info(self) -> dict:
        card_info: dict = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }
        if self.attack:
            card_info["attack"] = self.attack
        if self.health:
            card_info["health"] = self.health
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        if self.cost <= available_mana:
            return True
        else:
            return False

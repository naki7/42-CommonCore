from abc import ABC, abstractmethod


class Combatable(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def attack(self, target) -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass

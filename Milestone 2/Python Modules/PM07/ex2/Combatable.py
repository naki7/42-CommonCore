from abc import ABC, abstractmethod


class Combatable(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        if (self.health - incoming_damage) < 1:
            self.still_alive = False
        defense_result: dict = {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": self.damage - incoming_damage,
            "still_alive": self.still_alive
        }
        self.defense_result = defense_result
        return defense_result

    def get_combat_stats(self) -> dict:
        combat_stats: dict = {}
        if self.attack_result is not None:
            combat_stats["Attack result"] = self.attack_result
        if self.defense_result is not None:
            combat_stats["Defense result"] = self.defense_result
        if self.attack_result is None and self.defense_result is None:
            combat_stats["Attack result"] = "No attack initiated"
            combat_stats["Defense result"] = "No defense initiated"
        return combat_stats

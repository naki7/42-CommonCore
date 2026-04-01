from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str):
        super().__init__(name, cost, rarity)
        self.still_alive = True
        self.attack_result: dict = None
        self.defense_result: dict = None

    def play(self, game_state: dict) -> dict:
        elite_result: dict = {}

        self.combat_type = game_state["combat_type"]
        self.health = game_state["health"]
        self.damage = game_state["damage"]
        self.attack(game_state["target"])
        self.defend(game_state["incoming_damage"])
        elite_result["Combat phase"] = self.get_combat_stats()

        self.cast_spell(game_state["spell_name"], game_state["targets"])
        self.channel_mana(game_state["channel_amount"])
        elite_result["Magic phase"] = self.get_magic_stats()
        return elite_result

    def attack(self, target) -> dict:
        attack_result: dict = {
            "attacker": self.name,
            "target": target,
            "damage": self.damage,
            "combat_type": self.combat_type
        }
        self.attack_result = attack_result
        return attack_result

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        cast_result: dict = {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost
        }
        self.cast_result = cast_result
        return cast_result

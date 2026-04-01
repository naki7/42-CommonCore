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

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        cast_result: dict = {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost
        }
        self.cast_result = cast_result
        return cast_result

    def channel_mana(self, amount: int) -> dict:
        channel_result: dict = {
            "channeled": amount,
            "total_mana": self.cost + amount
        }
        self.channel_result = channel_result
        return channel_result

    def get_magic_stats(self) -> dict:
        magic_stats: dict = {
            "Spell cast": self.cast_result,
            "Mana channel": self.channel_result
        }
        return magic_stats

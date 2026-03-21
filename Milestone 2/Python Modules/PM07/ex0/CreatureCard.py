from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        if attack > 0 or health > 0:
            super().__init__(name, cost, rarity)
            self.attack = attack
            self.health = health
        else:
            raise ValueError("Attack and Health should be positive integers")

    def play(self, game_state: dict) -> dict:
        current_state: dict = {
            "card_played": game_state["name"],
            "mana_used": game_state["cost"],
            "effect": "Creature summoned to battlefield"
        }
        return current_state

    def attack_target(self, target) -> dict:
        combat_resolved: bool = False
        damage_dealt = target.attack
        if self.attack > target.health:
            combat_resolved = True
            damage_dealt = self.attack

        attack_result: dict = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": damage_dealt,
            "combat_resolved": combat_resolved
        }
        return attack_result

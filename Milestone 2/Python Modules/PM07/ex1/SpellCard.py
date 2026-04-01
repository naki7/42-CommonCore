from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: dict) -> dict:
        self.effect_str: str = self.effect_type
        if self.effect_str == "damage":
            self.effect_str = "Deal 3 damage to target"
        elif self.effect_str == "heal":
            self.effect_str = "Heal 3 damage from target"
        elif self.effect_str == "buff":
            self.effect_str = "Add 3 attack to target"
        elif self.effect_str == "debuff":
            self.effect_str = "Remove 3 attack from target"
        self.resolve_effect(game_state["targets"])
        current_state: dict = {
            "card_played": game_state["name"],
            "mana_used": game_state["cost"],
            "effect": self.effect_str
        }
        return current_state

    def resolve_effect(self, targets: list) -> dict:
        target_dict: dict = {}
        for target in targets:
            target_dict[target] = self.effect_str
        return target_dict

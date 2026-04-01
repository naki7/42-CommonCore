from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect
        self.current_effect: dict = {}

    def play(self, game_state: dict) -> dict:
        active_effect = self.activate_ability()
        current_state: dict = {
            "card_played": game_state["name"],
            "mana_used": game_state["cost"],
            "effect": f"{active_effect['duration']}: {active_effect['effect']}"
        }
        return current_state

    def activate_ability(self) -> dict:
        self.current_effect["duration"] = "Permanent"
        self.current_effect["effect"] = self.effect
        return self.current_effect

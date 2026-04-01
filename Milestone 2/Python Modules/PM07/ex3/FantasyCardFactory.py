from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory():
    def __init__(self):
        super().__init__()
        self.class_name = "FantasyCardFactory"

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "dragon" or name_or_power == 7:
            dragon_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
            return dragon_card
        return CreatureCard("Goblin Warrior", 2, "Common", 5, 2)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "fireball" or name_or_power == 2:
            return SpellCard("Fireball", 1, "Common", "damage")
        return SpellCard("Lightning Bolt", 3, "Rare", "damage")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        return ArtifactCard("Mana Ring", 12, "Legendary", 10,
                            "+3 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        if size < 1:
            return {}
        elif size == 3:
            deck: dict = {
                "dragon": self.create_creature("dragon"),
                "goblin": self.create_creature("goblin"),
                "spell": self.create_spell("spell")
            }
            return deck
        else:
            deck: dict = {
                "dragon": self.create_creature("dragon"),
                "goblin": self.create_creature("goblin"),
                "spell": self.create_spell("fireball"),
                "artifact": self.create_artifact("mana_ring")
            }
            return deck

    def get_supported_types(self) -> dict:
        type_list: dict = {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
        return type_list

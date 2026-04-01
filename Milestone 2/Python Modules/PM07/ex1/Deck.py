from ex0.Card import Card
from ex0.CreatureCard import CreatureCard as Creature
from .ArtifactCard import ArtifactCard as Artifact
from .SpellCard import SpellCard as Spell
import random
import math


class Deck:
    def __init__(self):
        self.library: dict = {}
        self.deck_list: list = []

    def add_card(self, card: Card) -> None:
        if self.library.get(card.name) is not None:
            self.library[card.name] += 1
        else:
            self.library[card.name] = 1
        self.deck_list.append(card)

    def remove_card(self, card_name: str) -> bool:
        if self.library[card_name] == 1:
            self.library.pop(card_name)
            return False
        else:
            self.library[card_name] -= 1
            return True

    def shuffle(self) -> None:
        random.shuffle(self.deck_list)

    def draw_card(self) -> Card:
        top_card: Card = self.deck_list.pop(0)
        self.remove_card(top_card.name)
        return top_card

    def get_deck_stats(self) -> dict:
        deck_stats: dict = {
            "total_cards": 0,
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0
        }
        total_cost: int = 0

        for card in self.deck_list:
            deck_stats["total_cards"] += 1
            total_cost += card.cost
            if isinstance(card, Creature):
                deck_stats["creatures"] += 1
            elif isinstance(card, Spell):
                deck_stats["spells"] += 1
            elif isinstance(card, Artifact):
                deck_stats["artifacts"] += 1
        deck_stats["avg_cost"] = total_cost / deck_stats["total_cards"]
        deck_stats["avg_cost"] = float(math.ceil(deck_stats["avg_cost"]))
        return deck_stats

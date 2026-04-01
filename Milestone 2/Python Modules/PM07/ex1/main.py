from .Deck import Deck
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")

    main_deck: Deck = Deck()
    print("Building deck with different card types...")
    spell_card: SpellCard = SpellCard("Lightning Bolt", 3, "Common", "damage")
    artifact_card: ArtifactCard = ArtifactCard("Mana Crystal", 2, "Common", 5,
                                               "+1 mana per turn")
    creature_card: CreatureCard = CreatureCard("Fire Dragon", 5, "Legendary",
                                               7, 5)
    main_deck.add_card(creature_card)
    main_deck.add_card(spell_card)
    main_deck.add_card(artifact_card)

    print(f"Deck stats: {main_deck.get_deck_stats()}")

    print("\nDrawing and playing cards:\n")
    main_deck.shuffle()

    while len(main_deck.deck_list) > 0:
        drawn_card = main_deck.draw_card()
        card_type: str = ""
        if isinstance(drawn_card, ArtifactCard):
            card_type = "Artifact"
        elif isinstance(drawn_card, CreatureCard):
            card_type = "Creature"
        elif isinstance(drawn_card, SpellCard):
            card_type = "Spell"
        print(f"Drew: {drawn_card.name} ({card_type})")
        game_state: dict = {
            "name": drawn_card.name,
            "cost": drawn_card.cost,
            "targets": "target"
            }
        print(f"Play result: {drawn_card.play(game_state)}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()

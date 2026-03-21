from .CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")
    try:
        dragon_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    except ValueError as alert:
        print(f"Error: {alert}")
        return
    try:
        goblin_card = CreatureCard("Goblin Warrior", 2, "Common", 2, 2)
    except ValueError as alert:
        print(f"Error: {alert}")
        return
    print("\nCreatureCard Info:")
    print(dragon_card.get_card_info())
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon_card.is_playable(6)}")
    print(f"Play result: {dragon_card.play(dragon_card.get_card_info())}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon_card.attack_target(goblin_card)}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon_card.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()

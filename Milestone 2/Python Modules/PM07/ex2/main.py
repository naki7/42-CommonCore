from .EliteCard import EliteCard
from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


def get_accessible_funcs() -> dict:
    elite_card_funcs: list = [func for func in dir(EliteCard) if callable(
        getattr(EliteCard, func))]
    elite_card_funcs = [func for func in elite_card_funcs if func.find(
        "__") == -1]

    card_funcs: list = [func for func in dir(Card) if callable(
        getattr(EliteCard, func))]
    card_funcs = [func for func in card_funcs if func.find("__") == -1]

    combatable_funcs: list = [func for func in dir(Combatable) if callable(
        getattr(EliteCard, func))]
    combatable_funcs = [func for func in combatable_funcs if func.find(
        "__") == -1]

    magical_funcs: list = [func for func in dir(Magical) if callable(
        getattr(EliteCard, func))]
    magical_funcs = [func for func in magical_funcs if func.find("__") == -1]

    funcs_to_compare: dict = {
        "Card": card_funcs,
        "Combatable": combatable_funcs,
        "Magical": magical_funcs
    }
    accessible_funcs: dict = {
        "Card": [],
        "Combatable": [],
        "Magical": []
    }
    for elite_func in elite_card_funcs:
        for func_list in funcs_to_compare:
            for original_func in funcs_to_compare[func_list]:
                if elite_func == original_func:
                    accessible_funcs[func_list].append(elite_func)
    play_func: str = accessible_funcs["Card"].pop(2)
    accessible_funcs["Card"].insert(0, play_func)

    return accessible_funcs


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    elite_card_funcs: dict = get_accessible_funcs()
    for class_type in elite_card_funcs:
        print(f"- {class_type}: {elite_card_funcs[class_type]}")

    arcane_card: EliteCard = EliteCard("Arcane Warrior", 4, "Legendary")
    game_state: dict = {
        "target": "Enemy",
        "health": 7,
        "damage": 5,
        "combat_type": "melee",
        "incoming_damage": 2,
        "spell_name": "Fireball",
        "targets": ["Enemy1", "Enemy2"],
        "channel_amount": 3
    }
    print(f"\nPlaying {arcane_card.name} (Elite Card)")
    play_result: dict = arcane_card.play(game_state)
    for category in play_result:
        print(f"\n{category}:")
        for sub_category in play_result[category]:
            print(f"{sub_category}: {play_result[category][sub_category]}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()

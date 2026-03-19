from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    components: str = f"{lead_to_gold()} and {healing_potion()}"
    return f"Philosopher’s stone created using {components}"


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"

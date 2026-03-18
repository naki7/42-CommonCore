def healing_potion() -> str:
    from .elements import create_fire, create_water
    results: str = f"{create_fire()} and {create_water()}"
    return f"Healing potion brewed with {results}"


def strength_potion() -> str:
    from .elements import create_earth, create_fire
    results: str = f"{create_earth()} and {create_fire()}"
    return f"Strength potion brewed with {results}"


def invisibility_potion() -> str:
    from .elements import create_air, create_water
    results: str = f"{create_air()} and {create_water()}"
    return f"Invisibility potion brewed with {results}"


def wisdom_potion() -> str:
    from .elements import create_fire, create_water, create_air, create_earth
    results_one: str = f"{create_fire()} {create_water()}"
    results_two: str = f"{create_air()} {create_earth()}"
    all_results: str = f"{results_one} {results_two}"
    return f"Wisdom potion brewed with all elements: {all_results()}"

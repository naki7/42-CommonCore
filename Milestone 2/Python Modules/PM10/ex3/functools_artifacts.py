from collections.abc import Callable
from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return max(spells)
    elif operation == "min":
        return min(spells)
    else:
        raise Exception("Invalid operation entered.")


def spell(power: int, element: str, target: str) -> str:
    return f"{target} takes {power} {element} damage"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    ice_spell: Callable = partial(base_enchantment, 50, "ice")
    fire_spell: Callable = partial(base_enchantment, 50, "fire")
    water_spell: Callable = partial(base_enchantment, 50, "water")

    return {
        "Lightning Chicken": ice_spell,
        "Ice Turkey": fire_spell,
        "Flaming Ostrich": water_spell
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(type: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(type: int) -> str:
        return f"{type} damage"

    @dispatcher.register
    def _(type: str) -> str:
        return f"{type}ball"

    @dispatcher.register
    def _(type: list) -> str:
        if len(type) == 1:
            return "1 spell"
        else:
            return f"{len(type)} spells"

    return dispatcher


def main() -> None:
    print("\nTesting spell reducer...")
    spell_list: list = [20, 40, 10, 30]
    print(f"Sum: {spell_reducer(spell_list, 'add')}")
    print(f"Product: {spell_reducer(spell_list, 'multiply')}")
    print(f"Max: {spell_reducer(spell_list, 'max')}")
    print(f"Min: {spell_reducer(spell_list, 'min')}")
    try:
        print(f"Stuff: {spell_reducer(spell_list, 'words')}")
    except Exception as alert:
        print(f"Error: {alert}")

    print("\nTesting partial enchanter...")
    enchant_dict: dict = partial_enchanter(spell)
    for trigger in enchant_dict:
        print(enchant_dict[trigger](trigger))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    # print(memoized_fibonacci.cache_info())
    print(f"Fib(1): {memoized_fibonacci(1)}")
    # print(memoized_fibonacci.cache_info())
    print(f"Fib(10): {memoized_fibonacci(10)}")
    # print(memoized_fibonacci.cache_info())
    print(f"Fib(15): {memoized_fibonacci(15)}")
    # print(memoized_fibonacci.cache_info())
    # print(memoized_fibonacci(15))
    # print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    dispatch: Callable = spell_dispatcher()
    print(f"Damage spell: {dispatch(42)}")
    print(f"Enchantment: {dispatch('fire')}")
    print(f"Multi-cast: {dispatch(['fire', 'water', 'grass'])}")
    print(dispatch({'key': 'value'}))


if __name__ == "__main__":
    main()

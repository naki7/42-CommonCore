from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count: int = 0

    def tracker() -> int:
        nonlocal count
        count += 1
        return count
    return tracker


def spell_accumulator(initial_power: int) -> Callable:
    curr_power: int = initial_power

    def accumulator(power: int) -> int:
        nonlocal curr_power
        curr_power += power
        return curr_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory: dict = {}

    def store(key: str, value: int) -> dict:
        memory[key] = value
        return memory

    def recall(key: str) -> Any:
        if key in memory:
            return memory[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    print("\nTesting mage counter...")
    counter_a: Callable = mage_counter()
    counter_b: Callable = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    initial: int = 100
    increasing_spell: Callable = spell_accumulator(100)
    print(f"Base {initial}, add 20: {increasing_spell(20)}")
    print(f"Base {initial}, add 30: {increasing_spell(30)}")

    print("\nTesting enchantment factory...")
    hot_factory: Callable = enchantment_factory("Flaming")
    cold_factory: Callable = enchantment_factory("Frozen")
    print(hot_factory('Sword'))
    print(cold_factory('Shield'))

    print("\nTesting memory vault...")
    vault: dict[str, Callable] = memory_vault()
    try:
        vault["store"]("secret", 42)
        print("Store \'secret\' = 42")
    except Exception as alert:
        print(alert)
    print(f"Recall \'secret\': {vault['recall']('secret')}")
    print(f"Recall \'unknown\': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()

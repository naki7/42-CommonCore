def full_module() -> None:
    import alchemy.elements

    element_method = alchemy.elements.create_fire
    element_name: str = element_method.__name__
    print(f"alchemy.elements.{element_name}(): {element_method()}\n")


def specific_function() -> None:
    from alchemy.elements import create_water

    element_method = create_water
    element_name: str = element_method.__name__
    print(f"{element_name}(): {element_method()}\n")


def aliased() -> None:
    from alchemy.potions import healing_potion as heal
    potion_method = heal
    print(f"heal(): {potion_method()}\n")


def multiple() -> None:
    from alchemy.elements import create_fire, create_water
    from alchemy.potions import strength_potion

    mixed_methods = [
        create_fire,
        create_water,
        strength_potion
        ]
    for method in mixed_methods:
        print(f"{method.__name__}(): {method()}")


def main() -> None:
    print("\n=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    full_module()

    print("Method 2 - Specific function import:")
    specific_function()

    print("Method 3 - Aliased import:")
    aliased()

    print("Method 4 - Multiple imports:")
    multiple()

    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    main()

from alchemy.grimoire import validate_ingredients as validator
from alchemy.grimoire import record_spell as recorder


def main() -> None:
    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print(f"{validator.__name__}(\"fire air\"): {validator('fire air')}")
    print(f"{validator.__name__}(\"dragon scales\"): ",
          validator('dragon scales'))

    print("\nTesting spell recording with validation:")
    print(f"{recorder.__name__}(\"Fireball\", \"fire air\"): ",
          recorder("Fireball", "fire air"))
    print(f"{recorder.__name__}(\"Dark Magic\", \"shadow\"): ",
          recorder("Dark Magic", "shadow"))

    print("\nTesting late import technique:")
    print(f"{recorder.__name__}(\"Lightning\", \"air\"): ",
          recorder("Lighting", "air"))
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()

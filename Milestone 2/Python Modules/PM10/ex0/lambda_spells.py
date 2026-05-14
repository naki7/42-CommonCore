def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: (mage["power"] - min_power) >= 0, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    total: int = sum(map(lambda mage: mage["power"], mages))
    return {
        "max_power": max(mages, key=lambda mage: mage["power"]),
        "min_power": min(mages, key=lambda mage: mage["power"]),
        "avg_power": "%.2f" % (total / len(mages))
        }


def main() -> None:
    print("\nTesting artifact sorter...")
    artifacts: list = [
        {
            "name": "Crystal",
            "power": 85,
            "type": "Orb"
        },
        {
            "name": "Fire",
            "power": 92,
            "type": "Staff"
        }
    ]
    artifacts = artifact_sorter(artifacts)
    print(f"{artifacts[0]['name']} {artifacts[0]['type']}",
          f"({artifacts[0]['power']} power) comes before",
          f"{artifacts[1]['name']} {artifacts[1]['type']}",
          f"({artifacts[1]['power']} power)")

    og_mages: list = [
        {
            "name": "Elric",
            "power": 85,
            "element": "Electric"
        },
        {
            "name": "Saint",
            "power": 97,
            "element": "Water"
        }
    ]
    mages = power_filter(og_mages, 90)
    print("\nTesting power filter...")
    for mage in mages:
        print(f"{mage['name']} the {mage['element']} Mage has {mage['power']}",
              "power")

    print("\nTesting spell transformer...")
    spells: list = [
        "fireball",
        "heal",
        "shield"
    ]
    spells = spell_transformer(spells)
    for spell in spells:
        print(spell, end=" ")
    print("")

    print("\nTesting mage stats...")
    stats: dict = mage_stats(og_mages)
    for stat in stats:
        print(f"{stat}: {stats[stat]}")


if __name__ == "__main__":
    main()

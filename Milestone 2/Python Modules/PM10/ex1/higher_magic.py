from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heals {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def caster_validator(target: str, power: int) -> bool:
    if target == "Dragon" and power < 90:
        return False
    else:
        return True


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(target: str, power: int) -> tuple:
        return (spell1(target, power)[:-10], spell2(target, power)[:-10])
    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)[-5:-3]
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def condition_check(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return condition_check


def spell_sequence(spells: list[Callable]) -> Callable:
    def spell_caster(target: str, power: int) -> list:
        casted_spells: list = []
        for spell in spells:
            casted_spells.append(spell(target, power))
        return casted_spells
    return spell_caster


def main() -> None:
    dmg_spell: Callable = fireball
    heal_spell: Callable = heal

    print("\nTesting spell combiner...")
    combine_spells: Callable = spell_combiner(dmg_spell, heal_spell)
    result: tuple = combine_spells('Dragon', 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball: Callable = power_amplifier(dmg_spell, 3)
    print(f"Original: 10, Amplified: {mega_fireball('Dragon', 10)}")

    print("\nTesting conditional caster...")
    condition: Callable = caster_validator
    cast_conditional: Callable = conditional_caster(condition, dmg_spell)
    print(cast_conditional('Dragon', 80))

    print("\nTesting spell sequence...")
    spell_list: list = [dmg_spell, heal_spell, dmg_spell, dmg_spell]
    spell_activation: Callable = spell_sequence(spell_list)
    for spell in spell_activation('Dragon', 90):
        print(spell)


if __name__ == "__main__":
    main()

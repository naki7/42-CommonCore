from collections.abc import Callable
from functools import wraps
from time import sleep


def spell_timer(func: Callable) -> Callable:
    wraps(func)

    def timer() -> str:
        sleep_time: float = 1.234
        print(f"Casting {func.__name__}...")
        sleep(sleep_time)
        print(f"Spell completed in {sleep_time} seconds")
        return func()
    return timer


@spell_timer
def fire_spell() -> str:
    return "Fireball"


def power_validator(min_power: int) -> Callable:
    def factory(func: Callable) -> Callable:
        wraps(func)

        def validator(*args, **kwargs) -> str:
            if len(args) < 2:
                if args[0] >= min_power:
                    return func(*args, **kwargs)
            elif len(args) >= 2:
                if args[2] >= min_power:
                    return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return validator
    return factory


@power_validator(60)
def unstable_spell(power: int) -> str:
    return f"Chaotic energy levels of {power} (balanced and cast)"


def retry_spell(max_attempts: int) -> Callable:
    def retrier(func: Callable) -> Callable:
        wraps(func)

        def attempter(charges: int) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    if charges < 3:
                        charges += 1
                        raise Exception(f"(attempt {attempt}/3)")
                    return func(charges)
                except Exception as alert:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... {alert}")
            return f"Spell casting failed after {attempt} attempts"
        return attempter
    return retrier


@retry_spell(3)
def charging_spell(charges: int) -> str:
    return f"Supreme Blast successful with {charges} charges"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) > 2:
            if all(char.isalpha() or char.isspace() for char in name):
                return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")
    print(f"Result: {fire_spell()} cast!")

    print("\nTesting power validator...")
    print(f"Weak power: {unstable_spell(59)}")
    print(f"Strong power: {unstable_spell(70)}")

    print("\nTesting retrying spell...")
    print(charging_spell(0))
    print("\nRe-Testing retrying spell...")
    print(charging_spell(2))

    print("\nTesting MageGuild...")
    wizzie: MageGuild = MageGuild()
    print(wizzie.validate_mage_name("Charles The Great"))
    print(wizzie.validate_mage_name("Ch4r312"))
    print(wizzie.cast_spell("Lightning", 15))
    print(wizzie.cast_spell("Spark", 3))


if __name__ == "__main__":
    main()

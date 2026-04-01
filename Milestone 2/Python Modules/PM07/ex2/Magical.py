from abc import ABC, abstractmethod


class Magical(ABC):
    def __init__(self):
        super().__init__()
        self.cast_result: dict = None
        self.channel_result: dict = None

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        channel_result: dict = {
            "channeled": amount,
            "total_mana": self.cost + amount
        }
        self.channel_result = channel_result
        return channel_result

    def get_magic_stats(self) -> dict:
        magic_stats: dict = {
            "Spell cast": self.cast_result,
            "Mana channel": self.channel_result
        }
        return magic_stats

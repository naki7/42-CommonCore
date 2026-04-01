from .GameStrategy import GameStrategy
from ex1.SpellCard import SpellCard


class AggressiveStrategy(GameStrategy):
    def __init__(self):
        super().__init__()
        self.mana: int = 5

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        turn_result: dict = {}
        played_this_turn: list = []
        damage_dealt: dict = {"Enemy Player": 0}
        total_damage: int = 0
        mana_used: int = 0
        sorted_hand: list = {k: v for k, v in sorted(hand.items(),
                                                     key=lambda item: item[0],
                                                     reverse=True)}
        for card in sorted_hand:
            if (self.mana - mana_used) >= sorted_hand[card].cost:
                mana_used += sorted_hand[card].cost
                battlefield.append(card)
                played_this_turn.append(sorted_hand[card])
                hand.pop(card)

        attack_order: list = []
        for card in played_this_turn:
            attack_order = self.prioritize_targets(battlefield)
            card_index: int = played_this_turn.index(card)
            if isinstance(played_this_turn[card_index], SpellCard):
                if damage_dealt.get(attack_order[0]) is not None:
                    damage_dealt[attack_order[0]] += 3
                else:
                    damage_dealt[attack_order[0]] = 3
                total_damage += 3
            else:
                if damage_dealt.get(attack_order[0]) is not None:
                    damage_dealt[attack_order[0]] += played_this_turn[
                        card_index].attack
                else:
                    damage_dealt[attack_order[0]] = played_this_turn[
                        card_index].attack
                total_damage += played_this_turn[card_index].attack

        rearrange: SpellCard = played_this_turn.pop(0)
        played_this_turn.append(rearrange)
        turn_result = {
            "cards_played": [played.name for played in played_this_turn],
            "mana_used": mana_used,
            "targets_attacked": [damage for damage in damage_dealt],
            "damage_dealt": total_damage
        }
        return turn_result

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        try:
            if available_targets.index("Enemy Player") != 0:
                available_targets.pop("Enemy Player")
                new_target_order: list = ["Enemy Player"]
                new_target_order.append(available_targets)
                return new_target_order
        except ValueError:
            return available_targets
        return available_targets

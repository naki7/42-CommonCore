from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
        if rarity == "Legendary":
            self.rating: int = 1200
            self.damage: int = 10
            self.health: int = 10
        else:
            self.rating: int = 1150
            self.damage: int = 6
            self.health: int = 6
        self.wins: int = 0
        self.losses: int = 0
        self.previous_stats: dict = {"win": 0, "loss": 0}
        self.rank = None

    def play(self, game_state: dict) -> dict:
        game_state["self"] = self
        game_state.update(self.attack(game_state["target"]))
        if self.health > game_state["damage_taken"]:
            self.update_wins(1)
        elif self.health < game_state["damage_taken"]:
            self.update_losses(1)
        game_state["rank"] = self.get_rank_info()
        self.previous_stats = {"win": self.wins, "loss": self.losses}
        return game_state

    def attack(self, target) -> dict:
        damage_taken: int = 0
        if target.get('wizard_001'):
            if target['wizard_001'].damage > 0:
                damage_taken = target['wizard_001'].damage
        else:
            if target['dragon_001'].damage > 0:
                damage_taken = target['dragon_001'].damage
        return {"damage_taken": damage_taken}

    def calculate_rating(self) -> int:
        win_increase: int = self.wins - self.previous_stats["win"]
        loss_increase: int = self.losses - self.previous_stats["loss"]
        self.rating += (win_increase - loss_increase) * 16
        return self.rating

    def get_tournament_stats(self) -> dict:
        tournament_dict: dict = {
            "name": self.name,
            "interfaces": [base.__name__ for base in self.__class__.__bases__],
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
        return tournament_dict

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        return

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        return

    def get_rank_info(self) -> dict:
        curr_rating: int = self.rating
        rating_change: int = curr_rating - self.calculate_rating()
        if rating_change < 0:
            if self.rank is None:
                self.rank = 1
            elif self.rank > 1:
                self.rank -= 1
        elif rating_change > 0:
            if self.rank is None:
                self.rank = 2
            else:
                self.rank += 1
        rank_dict: dict = {
            "rank": self.rank,
            "name": self.name,
            "rating": self.rating,
            "win_loss": f"({self.wins}-{self.losses})"
        }
        return rank_dict

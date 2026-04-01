from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards: list = []
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        if card.name == "Fire Dragon":
            id: str = "dragon_001"
        elif card.name == "Ice Wizard":
            id: str = "wizard_001"
        else:
            id: str = "damnthiscrazy_001"
        self.cards.append({id: card})
        initial_stats: dict = card.get_tournament_stats()
        title: str = f"{card.name} (ID: {id}):\n"
        inter1: str = "Interfaces:"
        inter2: str = f"{'[%s]' % ', '.join(initial_stats['interfaces'])}\n"
        interface: str = f"{inter1} {inter2}"
        rating: str = f"Rating: {initial_stats['rating']}\n"
        record: str = f"Record: {initial_stats['record']}\n"
        final_result: str = f"{title}{interface}{rating}{record}"
        return final_result

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        id_1game_state: dict = {"target": self.cards[1]}
        id_2game_state: dict = {"target": self.cards[0]}
        self.cards[0][card1_id].play(id_1game_state)
        self.cards[1][card2_id].play(id_2game_state)
        match_result: dict = {}
        if self.cards[0][card1_id].rating > self.cards[1][card2_id].rating:
            match_result["winner"] = card1_id
            match_result["loser"] = card2_id
            match_result["winner_rating"] = self.cards[0][card1_id].rating
            match_result["loser_rating"] = self.cards[1][card2_id].rating
        elif self.cards[1][card2_id].rating > self.cards[0][card1_id].rating:
            match_result["winner"] = card2_id
            match_result["loser"] = card1_id
            match_result["winner_rating"] = self.cards[1][card2_id].rating
            match_result["loser_rating"] = self.cards[0][card1_id].rating
        else:
            match_result["none"] = "There are no winners right now"
        self.matches_played += 1
        return match_result

    def get_leaderboard(self) -> list:
        leaderboard: list = []
        num_cards: int = len(self.cards)
        i: int = 1
        while i <= num_cards:
            for card in self.cards:
                if card.get('dragon_001'):
                    if card['dragon_001'].rank == i:
                        rank_str = ""
                        rank_dict: dict = card['dragon_001'].get_rank_info()
                        name_str: str = f"{rank_dict['name']}"
                        rating_str: str = f"Rating: {rank_dict['rating']}"
                        win_str: str = f"{rank_dict['win_loss']}"
                        rank_str = f"{i}. {name_str} - {rating_str} {win_str}"
                        leaderboard.insert(i - 1, rank_str)
                        i += 1
                elif card.get('wizard_001'):
                    if card['wizard_001'].rank == i:
                        rank_str = ""
                        rank_dict: dict = card['wizard_001'].get_rank_info()
                        name_str: str = f"{rank_dict['name']}"
                        rating_str: str = f"Rating: {rank_dict['rating']}"
                        win_str: str = f"{rank_dict['win_loss']}"
                        rank_str = f"{i}. {name_str} - {rating_str} {win_str}"
                        leaderboard.insert(i - 1, rank_str)
                        i += 1
        return leaderboard

    def generate_tournament_report(self) -> dict:
        report_dict: dict = {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played
        }
        total_rating: int = 0
        for card in self.cards:
            if card.get('dragon_001'):
                total_rating += card['dragon_001'].rating
            elif card.get('wizard_001'):
                total_rating += card['wizard_001'].rating
        report_dict["avg_rating"] = int(total_rating / len(self.cards))
        report_dict["platform_status"] = "active"
        return report_dict

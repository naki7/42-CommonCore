# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/26 14:04:12 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/26 23:08:58 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class Lists():
    """
    creates lists with tuples to be used for comprehension as well as functions
    that run the comprehension on the lists and return a list as a result
    """
    def __init__(self) -> None:
        self.players: list[tuple[str, int, str]] = [
            ('alice', 2300, 'online'),
            ('bob', 1800, 'online'),
            ('charlie', 2150, 'online'),
            ('diana', 2050, 'offline')
            ]

    def get_high_scorers(self) -> list[str]:
        """loops through list to get scores above 2000, returns their names"""
        high_scores: list[str] = [name[0] for name in self.players
                                  if name[1] > 2000]
        return high_scores

    def get_double_scores(self) -> list[str]:
        """loops through list to get scores doubled and returns their names"""
        double_scores: list[str] = [score[1] * 2 for score in self.players]
        return double_scores

    def get_active_players(self) -> list[str]:
        """loops through list to online ones and returns their names"""
        active_players: list[str] = [name[0] for name in self.players
                                     if name[2] == 'online']
        return active_players


class Dictionaries():
    """
    creates dictionaries to be used for comprehension as well as functions
    that run comprehension to return a dictionary as a result
    """
    def __init__(self, database: dict[dict[str: int or str or set]]) -> None:
        self.database = database

    def get_players_scores(self) -> dict[str: int]:
        players_scores: dict[str: int] = {
            name: self.database[name]['score'] for name in self.database
            if self.database[name]['status'] == 'online'
        }
        return players_scores

    def get_score_categories(self) -> dict[str: int]:
        score_categories: dict[str: int] = {
            'high': sum(self.database[name]['score'] >= 2200
                        for name in self.database),
            'medium': sum(2000 <= self.database[name]['score'] < 2200
                          for name in self.database),
            'low': sum(self.database[name]['score'] < 2000
                       for name in self.database)
        }
        return score_categories

    def get_achievment_count(self) -> dict[str: int]:
        achievment_count: dict[str: int] = {
            name: len(self.database[name]['achievements']) for name in
            self.database if self.database[name]['status'] == 'online'
        }
        return achievment_count


class Sets():
    """
    creates sets to be used for comprehension as well as functions
    that run comprehension to return a set as a result
    """
    def __init__(self, database: dict[dict[str: int or str or set]]) -> None:
        self.database = database

    def get_unique_players(self) -> set[str]:
        unique_players: set[str] = {name for name in self.database}
        return unique_players

    def get_unique_achievements(self) -> set[str]:
        unique_achievements: set[str] = {
            achievement for name in self.database for achievement in
            self.database[name]['achievements'] if
            sum(achievement in self.database[player]['achievements'] for player
                in self.database) == 1
        }
        return unique_achievements

    def get_active_regions(self) -> set[str]:
        active_regions: set[str] = {
            self.database[name]['region'] for name in self.database
        }
        return active_regions


def main() -> None:
    """
    This project and function focuses on using the three of the collection
    storing data types [lists, dictionaries, sets], to show off comprehension.
    Comprehension is a simpler way of processing already stored data in a
    simpler and more efficient manner. an example is:
    new_store = [expression(&|key, pair) for item(&|key, pair) in
    iterable_object if condition == True/False]
    Operations can be performed on the expression such as x * 2 to double
    the values.
    """
    database: dict[dict[str: int or str or set]] = {
            'alice': {
                'score': 2300,
                'status': 'online',
                'region': 'north',
                'achievements': {"level_5", "level_10", "minion_slayer",
                                 "boss_slayer", "da_best"}
                },
            'bob': {
                'score': 1800,
                'status': 'online',
                'region': 'east',
                'achievements': {"perfectionist", "level_5", "special"}
                },
            'charlie': {
                'score': 2150,
                'status': 'online',
                'region': 'central',
                'achievements': {"baby", "starter", "target",
                                 "speed_demon", "first_kill", "perfectionist",
                                 "da_best"}
                },
            'diana': {
                'score': 2050,
                'status': 'offline',
                'region': 'north',
                'achievements': {"starter", "speed_demon", "baby",
                                 "minion_slayer", "target", "special"}
            },
        }
    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    player_list = Lists()
    high_scorers: list[str] = player_list.get_high_scorers()
    print(f"High scorers (>2000): {high_scorers}")
    doubled_scores: list[str] = player_list.get_double_scores()
    print(f"Scores doubled: {doubled_scores}")
    active_players: list[str] = player_list.get_active_players()
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_dict = Dictionaries(database)
    players_scores: dict[str: int] = player_dict.get_players_scores()
    print(f"Player scores: {players_scores}")
    score_categories: dict[str: int] = player_dict.get_score_categories()
    print(f"Score categories: {score_categories}")
    achievment_count: dict[str: int] = player_dict.get_achievment_count()
    print(f"Score categories: {achievment_count}")

    print("\n=== Set Comprehension Examples ===")
    player_set = Sets(database)
    unique_players: set[str] = player_set.get_unique_players()
    print(f"Unique players: {sorted(unique_players)}")
    unique_achievements: set[str] = player_set.get_unique_achievements()
    print(f"Unique achievements: {unique_achievements}")
    active_regions: set[str] = player_set.get_active_regions()
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players: int = len(database)
    print(f"Total players: {total_players}")
    all_achievements: set[str] = {
            achievement for name in database for achievement in
            database[name]['achievements']
        }
    print(f"Total unique achievements: {len(all_achievements)}")
    total_score: int = sum(database[player]['score'] for player in database)
    print(f"Average score: {total_score / total_players}")
    highest_scorer: dict[str: str] = {
            'name': player for player in database
            if database[player]['score'] == max(database[name]['score']
                                                for name in database)
        }
    top_name: str = highest_scorer['name']
    print(f"Top performer: {top_name} ({database[top_name]['score']} points,",
          f"{len(database[top_name]['achievements'])} achievements)")


if __name__ == "__main__":
    main()

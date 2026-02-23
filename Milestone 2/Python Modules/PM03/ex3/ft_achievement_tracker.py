# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 17:35:58 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/23 19:22:55 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main() -> None:
    """
    Create an achievement tracker using sets as the core variable.
    This will use union to find all unique achievements,
    intersection to find the achivements that all players have,
    and difference to find where there are unique achievements
    """
    print("=== Achievement Tracker System ===\n")
    alice: set[str] = {"first_kill", "level_10", "treasure_hunter",
                       "speed_demon"}
    bob: set[str] = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie: set[str] = {"level_10", "treasure_hunter", "boss_slayer",
                         "speed_demon", "perfectionist"}
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===\n")
    all_achievements: set[str] = alice.union(bob, charlie)
    print(f"All unique achievements: {all_achievements}")
    num_of_all: int = len(all_achievements)
    print(f"Total unique achievements: {num_of_all}\n")

    print("\n  = All Player Analytics =  \n")
    common: set[str] = alice.intersection(bob, charlie)
    print(f"Common to all players: {common}")
    rare_alice: set[str] = alice.difference(bob, charlie)
    rare_bob: set[str] = bob.difference(alice, charlie)
    rare_charlie: set[str] = charlie.difference(alice, bob)
    rare: set[str] = rare_alice.union(rare_bob, rare_charlie)
    print(f"Rare achievements (1 player): {rare}\n")

    print("\n  = Alice compared to Bob Analytics =  \n")
    alice_and_bob: set[str] = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_and_bob}")
    alice_minus_bob: set[str] = alice.difference(bob)
    print(f"Alice unique: {alice_minus_bob}")
    bob_minus_alice: set[str] = bob.difference(alice)
    print(f"Bob unique: {bob_minus_alice}")


if __name__ == "__main__":
    main()

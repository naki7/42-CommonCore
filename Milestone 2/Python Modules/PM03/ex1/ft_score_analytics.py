# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 11:46:04 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/17 15:24:05 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
import sys


def main() -> None:
    """
    Input needs to be received from the command line. This input then needs to
    be error handled, then also used to create a scoreboard using all argv's
    list attributes
    """
    size = len(sys.argv) - 1
    print("=== Player Score Analytics ===")
    if size < 1:
        print("No scores provided.\nUse: python3 ft_score_analytics.py",
              "<score1> <score2>...\nex. $> python3 ft_score_analytics.py",
              "1500 2300 1800 2100 1950\n")
        return
    scores: list[int] = []
    i: int = 0
    while i < size:
        i += 1
        try:
            scores += [int(sys.argv[i])]
        except ValueError:
            print(f"{sys.argv[i]} is not a valid input;",
                  f"{sys.argv[i]} ignored.")
    print("Scores processed: [", end="")
    i = 0
    size = len(scores)
    while i < size:
        print(scores[i], end="")
        i += 1
        if i == size:
            print("]")
        else:
            print(", ", end="")
    print(f"Total players: {size}")
    total_score = sum(scores)
    print(f"Total score: {total_score}")
    print(f"Average score: {total_score / size}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}\n")


if __name__ == "__main__":
    main()

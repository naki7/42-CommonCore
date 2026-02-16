# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/30 16:17:10 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/16 13:44:28 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    """Class representing a plant with growth and aging capabilities."""
    def __init__(self, name: str, height: float, days: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.days = days

    def grow(self, time: int) -> None:
        """Increase the plant's height based on growth rate over time."""
        self.height += time * 0.75

    def age(self, time: int) -> None:
        """Increase the plant's age in days."""
        self.days += time

    def get_info(self, time: int) -> None:
        """Display the plant's current info and projected growth."""
        self.grow(time)
        self.age(time)
        print(f"{self.name}: {self.height}cm, {self.days} days old", sep="")
        if time > 0:
            print(f"Growth in {time} days time is: +{(time * 0.75)}cm", sep="")


def main() -> None:
    """Initialize a plant and display its growth over time."""
    init_days = 16
    p1 = Plant('Spekboom', 5, init_days)
    print("~~~Day 1~~~")
    time = 0
    p1.get_info(time)
    time = 7
    print("~~~Day ", (time + 1), "~~~", sep="")
    p1.get_info(time)


if __name__ == "__main__":
    main()

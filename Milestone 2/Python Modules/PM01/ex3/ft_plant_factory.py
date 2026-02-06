# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 11:03:31 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/05 16:27:58 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    """Class representing a plant with basic attributes."""
    def __init__(self, name: str, height: float, days: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.days = days


def main() -> None:
    """Initialize and display a list of plants created by the factory."""
    print("~~~Plant Initialization~~~\n")
    p1 = Plant('Spekboom', 5, 2)
    p2 = Plant('Rose', 35, 30)
    p3 = Plant('Orchid', 21, 90)
    p4 = Plant('Protea', 2, 16)
    p5 = Plant('Sunflower', 124, 61)
    plant_arr: list[Plant] = [p1, p2, p3, p4, p5]
    for plant in plant_arr:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.days} days)")
    print("\n~~~Initialized 5 Plants~~~")


if __name__ == "__main__":
    main()

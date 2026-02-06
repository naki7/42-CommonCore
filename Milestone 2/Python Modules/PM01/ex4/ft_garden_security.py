# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 12:37:42 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/05 16:28:05 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class SecurePlant:
    """Class representing a plant with secure attributes."""
    def __init__(self, name: str, height: float, days: int) -> None:
        """Initialize a SecurePlant instance with private attributes."""
        self.__name = name
        self.__height = height
        self.__days = days
        print(f"Created: {name} ({height}cm, {days} days)")

    def get_name(self) -> str:
        """Return the name of the plant."""
        return self.__name

    def get_height(self) -> float:
        """Return the height of the plant."""
        return self.__height

    def get_age(self) -> int:
        """Return the age of the plant in days."""
        return self.__days

    def set_height(self, height: float) -> None:
        """Set the height of the plant if the input is valid."""
        if height > 0:
            self.__height = height
            print(f"Height updated to: {height}cm [OK]\n")
        else:
            print("ERROR: Invalid height input [NEGATIVE HEIGHT]\n")

    def set_age(self, days: int) -> None:
        """Set the age of the plant in days if the input is valid."""
        if days > 0:
            self.__days = days
            print(f"Age updated to: {days} days [OK]\n")
        else:
            print("ERROR: Invalid age input [NEGATIVE DAYS]\n")


def main() -> None:
    """Initialize and manage a list of secure plants."""
    print("~~~Plant Initialization~~~\n")
    p1 = SecurePlant('Spekboom', 5, 2)
    p2 = SecurePlant('Rose', 35, 30)
    p3 = SecurePlant('Orchid', 21, 90)
    p4 = SecurePlant('Protea', 2, 16)
    p5 = SecurePlant('Sunflower', 124, 61)
    print("\n~~~Garden Armour Initialized~~~\n")
    plant_arr: list[SecurePlant] = [p1, p2, p3, p4, p5]
    p1.set_age(40)
    p1.set_height(76)
    p2.set_height(36)
    p3.set_age(-12)
    p4.set_age(17)
    p5.set_height(-5)
    for plant in plant_arr:
        print(f"Current plant: {plant.get_name()} ({plant.get_height()}cm, ",
              f"{plant.get_age()} days)", sep="")


if __name__ == "__main__":
    main()

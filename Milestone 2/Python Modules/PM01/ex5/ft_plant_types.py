# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 13:21:55 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/05 16:42:39 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    """Class representing a plant with basic attributes."""
    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age = age

    def get_plant_info(self, plant_type: str) -> None:
        """Display the plant's information"""
        print(f"{self.name} ({plant_type}): {self.height}cm, {self.age}",
              " days, ", sep="", end="")


class Flower(Plant):
    """Class representing a flower with color and blooming status."""
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        """Initialize a Flower instance."""
        super().__init__(name, height, age)
        self.color = color
        self.bloom(False)

    def bloom(self, truthy: bool) -> None:
        """Set the blooming status of the flower."""
        if truthy:
            self.blooming = "blooming beautifully!\n"
        else:
            self.blooming = "not blooming yet\n"

    def get_flower_info(self) -> None:
        """Display the flower's information."""
        self.get_plant_info('Flower')
        print(f"{self.color} color\n{self.name} is {self.blooming}")


class Tree(Plant):
    """Class representing a tree with trunk diameter and shade production."""
    def __init__(self, name: str, height: float, age: int, diameter: float) \
            -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = diameter
        self.produce_shade((self.height * ((diameter) / 1000) * 3))

    def produce_shade(self, amount: float) -> None:
        """Set the amount of shade produced by the tree."""
        self.shade = amount

    def get_tree_info(self) -> None:
        """Display the tree's information."""
        self.get_plant_info('Tree')
        print(f"{self.trunk_diameter}cm diameter\n{self.name} provides ",
              f"{self.shade} square meters of shade\n", sep="")


class Vegetable(Plant):
    """Class of a vegetable with harvest season and nutritional value."""
    def __init__(self, name: str, height: float, age: int, season: str,
                 value: str) -> None:
        """Initialize a Vegetable instance."""
        super().__init__(name, height, age)
        self.harvest_season = season
        self.nutritional_value = value

    def get_vegetable_info(self) -> None:
        """Display the vegetable's information."""
        self.get_plant_info('Vegetable')
        print(f"{self.harvest_season} season\n{self.name} is rich in ",
              self.nutritional_value, "\n", sep="")


def main() -> None:
    """Initialize and display information about different plant types."""
    print("~~~Plant Types~~~\n")
    f1 = Flower('Orchid', 5, 2, 'blue')
    f2 = Flower('Rose', 35, 30, 'pink')
    f2.bloom(True)
    t1 = Tree('Oak', 500, 1825, 50)
    t1.produce_shade(78)
    t2 = Tree('Chestnut', 240, 700, 16)
    v1 = Vegetable('Tomato', 80, 90, 'summer', 'vitamin C')
    v2 = Vegetable('Spinach', 61, 43, 'autumn', 'Iron')
    flower_arr = [f1, f2]
    tree_arr = [t1, t2]
    vegetable_arr = [v1, v2]
    for flower in flower_arr:
        flower.get_flower_info()
    for tree in tree_arr:
        tree.get_tree_info()
    for vegetable in vegetable_arr:
        vegetable.get_vegetable_info()


if __name__ == "__main__":
    main()

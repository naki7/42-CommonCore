# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 15:06:27 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/16 14:13:10 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenManager:
    """Class to manage multiple gardens and perform analytics on them."""
    gardens: list["Garden"] = []

    class GardenStats:
        """Static methods for analyzing garden data."""
        def total_height(garden: "Garden") -> float:
            """Calculate the total height of all plants in a garden."""
            total = 0
            for plant in garden.plants:
                total += plant.height
            return total

        def total_prize_points(garden: "Garden") -> int:
            """Calculate the total prize points from all plants in a garden"""
            total = 0
            for plant in garden.plants:
                if plant.points > 0:
                    total += plant.points
            return total

        def check_valid(manager: "GardenManager") -> bool:
            """Check if all plants in all gardens have valid heights."""
            for garden in manager.gardens:
                for plant in garden.plants:
                    if plant.height < 0:
                        return (False)
            return True

        def total_gardens(manager: "GardenManager") -> int:
            """Calculate the total number of gardens managed."""
            total = 0
            for garden in manager.gardens:
                total += 1
            return total

        total_height = staticmethod(total_height)
        total_prize_points = staticmethod(total_prize_points)
        check_valid = staticmethod(check_valid)
        total_gardens = staticmethod(total_gardens)

    def create_garden_network(cls: type["GardenManager"]) -> dict[str, int]:
        """Create a network of gardens and calculate their scores."""
        scores: dict[str, int] = {}
        for garden in cls.gardens:
            score = garden.total_plants * 10
            score += cls.GardenStats.total_height(garden)
            score += cls.GardenStats.total_prize_points(garden)
            scores[garden.name] = score
        return scores

    create_garden_network = classmethod(create_garden_network)


class Garden:
    """Class representing a garden with a collection of plants."""
    def __init__(self, name: str) -> None:
        """Initialize a Garden instance."""
        self.name = name
        self.plants: list["Plant"] = []
        self.total_plants = 0
        self.growth = 0

    def add_plant(self, plant: "Plant") -> None:
        """Add a plant to the garden and update its total plant count."""
        self.plants = self.plants + [plant]
        self.total_plants += 1
        print(f"Added {plant.name} to {self.name}'s Garden")

    def grow_all(self) -> None:
        """Grow all plants in the garden and update the total growth."""
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.growth += 1

    def garden_report(self) -> None:
        """
        Generate a report of the garden's plants and their attributes.
        This relies on blooming and points being truthy based values.
        """
        print(f"=== {self.name}'s Garden Report ===\nPlants in garden:")
        regular = 0
        flowering = 0
        prize = 0
        for plant in self.plants:
            print(f"- {plant.name}: {plant.height}cm", end="")
            regular += 1
            if plant.blooming:
                regular -= 1
                flowering += 1
                print(f", {plant.color} flowers (blooming)", end="")
                if plant.points:
                    flowering -= 1
                    prize += 1
                    print(f", Prize points: {plant.points}")
            print("")
        print(f"Plants added: {self.total_plants},",
              f"Total growth: {self.growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering,",
              f"{prize} prize flowers\n")


class Plant:
    """Class representing a basic plant with growth capabilities."""
    def __init__(self, name: str, height: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.color = None
        self.blooming = False
        self.points = 0

    def grow(self) -> None:
        """Increase the plant's height by 1cm."""
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    """Class representing a flowering plant with color and blooming status."""
    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a FloweringPlant instance."""
        super().__init__(name, height)
        self.color = color
        self.blooming = True


class PrizeFlower(FloweringPlant):
    """Class representing a prize-winning flower with points."""
    def __init__(self, name: str, height: int, color: str,
                 points: int) -> None:
        """Initialize a PrizeFlower instance."""
        super().__init__(name, height, color)
        self.points = points


def main() -> None:
    """Initialize gardens, add plants, and generate reports and analytics."""
    print("~~~Garden Manager Mainframe~~~\n")

    alice = Garden("Alice")
    bob = Garden("Bob")

    GardenManager.gardens = [alice, bob]

    bobs_prizeflower = PrizeFlower("Rose", 80, "Pink", 2)
    bob.plants = [bobs_prizeflower]
    bob.total_plants = 1

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print("\n")
    alice.grow_all()
    print("\n")
    alice.garden_report()

    scores = GardenManager.create_garden_network()
    print("Height validation test:",
          GardenManager.GardenStats.check_valid(GardenManager))
    print("Garden scores - ", end="")
    for name in scores:
        print(name + ":", scores[name], end="")
        if name == "Alice":
            print(", ", end="")
        else:
            print("")
    print("Total gardens managed:",
          GardenManager.GardenStats.total_gardens(GardenManager))


if __name__ == "__main__":
    main()

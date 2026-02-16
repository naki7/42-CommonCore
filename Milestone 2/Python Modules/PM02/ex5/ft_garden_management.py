# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/07 14:25:35 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/16 17:28:17 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenManager:
    """
    Class representing a garden with a collection of plants.
    Error handling is used to validate input, as well as to validate data
    that is currently stored in the garden.
    """
    def __init__(self) -> None:
        """Initialize a Garden instance."""
        self.plants: list["Plant"] = []
        self.water = 5

    def check_plants(self) -> None:
        """Calls the PlantError class for the plant error"""
        for plant in self.plants:
            if plant.water == 0:
                raise PlantError(f"The {plant.name} plant is wilting")

    def check_water(self) -> None:
        """Calls the WaterError class for the water error"""
        if self.water < 5:
            raise WaterError("Not enough water in tank")

    def add_plant(self, plant: "Plant") -> None:
        """Add a plant to the garden after validating its data."""
        if plant.name == "":
            raise ValueError("Error adding plant: Plant name cannot be empty!")
        if plant.water < 1 or plant.water > 10:
            raise ValueError(f"Error: Water level {plant.water}")
        if plant.sunlight < 2 or plant.sunlight > 12:
            raise ValueError(f"Error: Sunlight hours {plant.sunlight}")
        self.plants = self.plants + [plant]
        print(f"Added {plant.name} successfully")

    def water_plants(self) -> None:
        """Loops through all the plants and waters them, or raises an error"""
        print("\nWatering plants...\nOpening watering system")
        try:
            for plant in self.plants:
                if plant is None or plant == "":
                    raise ValueError("invalid plant!")
                print(f"watering {plant.name} - success")
                plant.water += 1
                self.water -= 1
        except ValueError as alert:
            print(f"Error: Cannot water {plant.name} - {alert}")
        finally:
            print("Closing Watering System (sweeping the shed)")

    def check_plant_health(self) -> None:
        """Validates the plants already added in the garden
        and raises an error for issues"""
        for plant in self.plants:
            if plant.water < 1 or plant.water > 10:
                raise ValueError(f"{plant.name}: Water level {plant.water}")
            if plant.sunlight < 2 or plant.sunlight > 12:
                raise ValueError(f"{plant.name}: Sunlight {plant.sunlight}")
            print(f"{plant.name}: healthy",
                  f"(water: {plant.water}, sun: {plant.sunlight})")


class Plant:
    """Class representing a basic plant with watering capabilities."""
    def __init__(self, name: str, water: int, sunlight: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.water = water
        self.sunlight = sunlight


class GardenError(Exception):
    """This class creates a garden error which works for all garden problems"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """This class creates a plant error which works for plant problems"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    """This class creates a water error which works for water problems"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


def test_garden_management() -> None:
    """
    This function tests for:
    Adding plants with both valid and invalid inputs
    Watering plants with proper cleanup
    Checking plant health and handling validation errors
    Error recovery
    """
    manager = GardenManager()
    tomato = Plant("tomato", 4, 8)
    lettuce = Plant("lettuce", 10, 3)
    error_plant = Plant("", 7, 5)
    print("\nAdding plants to garden...")
    try:
        manager.add_plant(tomato)
        manager.add_plant(lettuce)
        manager.add_plant(error_plant)
    except ValueError as alert:
        print(alert)

    manager.water_plants()

    print("\nChecking plant health...")
    try:
        manager.check_plant_health()
    except ValueError as alert:
        print(f"Error checking {alert} is invalid")

    print("\nTesting error recovery...")
    try:
        for function in (manager.check_plants, manager.check_water):
            function()
    except GardenError as alert:
        print(f"Caught GardenError: {alert}")
    finally:
        print("System recovered and continuing...")

    print("\n~~~ Garden management system test complete ~~~")


def main() -> None:
    """
    Calls the test garden management function which is responsible for
    making sure that all the different input and error validation systems work
    """
    print("~~~ Garden Management System ~~~")
    test_garden_management()


if __name__ == "__main__":
    main()

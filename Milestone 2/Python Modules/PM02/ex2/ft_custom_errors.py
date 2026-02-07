# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/06 17:42:44 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/07 15:08:20 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

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


def check_plants() -> None:
    """Calls the PlantError class for the plant error"""
    raise PlantError("The tomato plant is wilting")


def check_water() -> None:
    """Calls the WaterError class for the water error"""
    raise WaterError("Not enough water in the tank")


def main() -> None:
    """Calling each function that calls the error classes
    along with try/catch blocks"""
    print("~~~ Garden Errors ~~~\n")
    print("Testing PlantError...")
    try:
        check_plants()
    except PlantError as alert:
        print(f"Caught a plant error: {alert}!")
        print("\nTesting WaterError...")
    try:
        check_water()
    except WaterError as alert:
        print(f"Caught a water error: {alert}!")
    print("\nTesting GardenError...")
    for function in (check_plants, check_water):
        try:
            function()
        except GardenError as alert:
            print(f"Caught a garden error: {alert}!")

    print("\n~~~ All errors tested succesfully! ~~~")


if __name__ == "__main__":
    main()

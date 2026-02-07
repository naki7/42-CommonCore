# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/07 13:21:53 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/07 13:51:33 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def water_plants(plant_list: list[str]) -> None:
    """This Function loops through a list of plants, waters each, and then
    cleans up afterwards. It also handles errors when they occur."""
    print("~~~ Opening Watering System ~~~")
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise ValueError("invalid plant!")
            print(f"watering {plant}")
    except ValueError as alert:
        print(f"Error: Cannot water {plant} - {alert}")
    finally:
        print("~~~ Closing Watering System (sweeping the shed) ~~~")


def test_watering_system() -> None:
    """Runs the water_plants function against different arrays of strings
    to show that the function safeguards against invalid inputs, always
    cleans up, and doesn't cause the program to crash"""
    good_array: list[str] = ["tomato", "lettuce", "carrots"]
    bad_array: list[str | None] = ["tomato", None]
    print("~~~ Garden Watering System ~~~\n")
    print("Testing normal watering system...")
    try:
        water_plants(good_array)
    finally:
        print("Watering completed succesfully!\n")
    print("Testing error prone watering system...")
    try:
        water_plants(bad_array)
    finally:
        print("\nEven with errors, the shed gets swept!")


def main() -> None:
    """Calls the watering system tester to show how it still works
    and cleans after crashes"""
    test_watering_system()


if __name__ == "__main__":
    main()

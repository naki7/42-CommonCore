# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_errors.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/07 13:59:53 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/07 14:24:02 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """This function validates the 3 arguments against certain criteria,
    if the criteria is not met then an error is raised (to be caught later)"""
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!\n")
    if water_level < 1 or water_level > 10:
        raise ValueError(f"Error: Water level {water_level}")
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}")
    print(f"Plant {plant_name} is healthy!\n")


def test_plant_checks() -> None:
    """Function shows how errors being raised in another function can be caught
    Each error is directly raised by a unique set of criteria"""
    print("Testing good values...")
    try:
        check_plant_health("tomato", 1, 6)
    except ValueError as alert:
        print(alert)
    print("Testing empty plant name...")
    try:
        check_plant_health("", 1, 6)
    except ValueError as alert:
        print(alert)
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 6)
    except ValueError as alert:
        print(f"{alert} is invalid (min: 1 - max: 10)\n")
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 1, 0)
    except ValueError as alert:
        print(f"{alert} is invalid (min: 2 - max: 12)\n")
    print("~~~ All error raising tests completed! ~~~")


def main() -> None:
    """Calls test plant function that shows how individual errors can be raised
    and caught"""
    print("~~~ Garden Plant Health Tester ~~~\n")
    test_plant_checks()


if __name__ == "__main__":
    main()

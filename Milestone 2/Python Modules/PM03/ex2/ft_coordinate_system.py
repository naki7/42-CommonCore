# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 17:43:19 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/23 17:33:57 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
import sys
import math


def run_euclidean_formula(values: tuple[int]) -> float:
    """
    Calculates the distance between two 3D points, 1 being the command line
    input and the other being (0, 0, 0). This is done by using a modified
    Pythagorean theorem.
    Since 0 is set for all points, it is a waste to do value[i] - origin[i]
    however this can be achieved with the below tuple and also line of code
    origin: tuple[int] = (0, 0, 0)
    result: float = math.sqrt((values[0] - origin[0])**2 +
    (values[1] - origin[1])**2 + (values[2] - origin[2])**2)
    """
    result: float = math.sqrt((values[0])**2 + (values[1])**2 + (values[2])**2)
    return result


def main() -> None:
    """
    Input will be received from the command line. This input will then be
    validated according to whether it is an integer/split possible strings
    into ints. These values will tehn be stored and printed out with the
    Euclidean distance formula being applied or an error message will be
    returned if the input is invalid.
    """
    print("=== Game Coordinate System ===\n")
    size: int = len(sys.argv) - 1
    if size != 1 and size != 3:
        print("Invalid coordinates provided.\n",
              "Use: python3 ft_coordinate_system.py <x> <y> <z>\n",
              "ex. $> python3 ft_coordinate_system.py 10 20 5")
        return
    coordinates: tuple[int] = ()
    if size == 1:
        values_arr: list[str] = sys.argv[1].split(",")
    else:
        values_arr: list[str] = [sys.argv[1], sys.argv[2], sys.argv[3]]
    if len(values_arr) != 3:
        print("Invalid coordinates provided.\n",
              "Use: python3 ft_coordinate_system.py <x> <y> <z>\n",
              "ex. $> python3 ft_coordinate_system.py 10 20 5")
        return

    i: int = 0
    while i < 3:
        try:
            value: tuple[int] = (int(values_arr[i]),)
            coordinates += value
        except ValueError as alert:
            print(f"Error: {values_arr[i]} is not valid - {alert}\n")
            print("Invalid coordinates provided.\n",
                  "Use: python3 ft_coordinate_system.py <x> <y> <z>\n",
                  "ex. $> python3 ft_coordinate_system.py 10 20 5")
            return
        i += 1

    print(f"Coordinates {coordinates} successfully added\n")

    print("This is the coordinates unpacked:")
    (x, y, z) = coordinates
    print(f"Coordinates: X={x}, Y={y}, Z={z}\n")

    distance: float = run_euclidean_formula(coordinates)
    distance = "%.2f" % distance
    print(f"Distance between (0, 0, 0) and {coordinates}: {distance}\n")


if __name__ == "__main__":
    main()

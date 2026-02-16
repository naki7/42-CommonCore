# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/06 14:58:46 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/16 14:25:33 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_temperature(temp_str: str) -> int:
    """Takes in a string, and tries to convert it into an int. It will either
    return and error or it will validate the int to see if it is in range"""
    try:
        temp_int: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a number")
        return -1

    if temp_int < 0:
        print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
        return -1
    elif temp_int > 40:
        print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
        return -1
    else:
        print(f"{temp_int}°C is a perfect temperature for plants!")
        return temp_int


def main() -> None:
    """Calls the temp checker with different errors and success cases"""
    print("~~~ Start of Program: testing for crashes ~~~\n")
    examples: list[str] = ["apple", "124", "7", "-16", "25"]
    for value in examples:
        print(f"Testing temperature: {value}")
        check_temperature(value)
        print("")
    print("End of Program reached: Crash Free!")


if __name__ == "__main__":
    main()

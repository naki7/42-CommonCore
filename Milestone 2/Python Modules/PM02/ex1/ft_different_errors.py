# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/06 15:53:49 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/16 14:29:36 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def garden_operations(error_type: str) -> None:
    """Demonstrates ValueError, ZeroDivisionError, FileNotFoundError,
    and KeyError"""
    if error_type == "value":
        int("six plus four")
    elif error_type == "zero":
        16/0
    elif error_type == "file":
        open("nonsense.txt")
    elif error_type == "key":
        badlist: list[str, int] = {"keys": 7}
        print(badlist["wrongkey"])


def test_error_types() -> None:
    """try/catch one or more errors, explains them, and keeps running"""
    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError as alert:
        print(f"Caught ValueError: {alert}\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as alert:
        print(f"Caught ZeroDivisionError: {alert}\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as alert:
        print(f"Caught FileNotFoundError: {alert}\n")

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError as alert:
        print(f"Caught KeyError: {alert}\n")

    print("Testing multiple errors together...")
    try:
        garden_operations("key")
    except (ValueError, ZeroDivisionError, FileNotFoundError,
            KeyError) as alert:
        print(f"Caught an error: {alert},\nBut program continues!\n")


def main() -> None:
    """Initialize the two functions that are being tested"""
    print("~~~ Error Testing Initializing ~~~\n")
    test_error_types()
    print("~~~ All errors tested succesfully! ~~~")


if __name__ == "__main__":
    main()

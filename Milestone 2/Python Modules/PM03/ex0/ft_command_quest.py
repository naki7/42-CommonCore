# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 10:27:41 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/17 12:44:39 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
import sys


def main() -> None:
    """
    sys gives acces to the method argv. Argv functions similarly to how it
    does in C. It basically creates a list/array with values that were input
    on the command line, it starts at the 0th index with the program name.
    There is no argc though so we can use len(sys.argv) to get the argc.
    """
    size = len(sys.argv)
    i: int = 0

    print("=== Command Quest ===")
    if size == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if size > 1:
        print(f"Arguments received: {size - 1}")
        while i < size - 1:
            i += 1
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {size}\n")


if __name__ == "__main__":
    main()

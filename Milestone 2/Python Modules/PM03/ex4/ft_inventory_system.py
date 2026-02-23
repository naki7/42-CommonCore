# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 19:24:14 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/23 19:57:03 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
import sys


def main() -> None:
    """"""
    inventory = {}
"""
    for arg in argv[1:]:
        try:
            key, value = arg.split("=")
            inventory[key] = int(value)
        except ValueError:
            print(f"Ignoring invalid argument: {arg}")

    return inventory
"""
    size = len(sys.argv) - 1
    i = 1
    dictionary: dict[str: int] = {}
    while i < size + 1:
        dictionary.update(sys.argv[i])
        i += 1
    for x in dictionary:
        print(type(x))


if __name__ == "__main__":
    main()

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 19:24:14 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/24 18:49:51 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
import sys


def main() -> None:
    """
    This program pulls from the command line, splits the arguments based on
    ':' as a seperator and then builds an inventory dictionary from the result.
    After that, len is used to get the number of items types, values are used
    to total the number of items, get to list the values for the keys, uses
    value to get a list of all the values to then loop over to see the lowest
    and highest values - then matching that with the first key that has those
    values in a tuple - tuple comes from items.
    The tuple is then also used for the item categories and management
    suggestions.
    Lastly, keys(), values() and "if "key" in inventory: print()" to see if
    a key exists.
    """
    print("=== Inventory System Analysis ===")
    inventory: dict[str: int] = {}
    for arg in sys.argv[1:]:
        try:
            key, value = arg.split(":")
            inventory[key] = int(value)
        except ValueError:
            print(f"Ignoring invalid argument: {arg}")
    keys: list[str] = inventory.keys()
    values: list[int] = inventory.values()
    values_total: int = 0
    for value in values:
        values_total += value
    print(f"Total items in inventory: {values_total}")
    total_keys: int = len(inventory)
    print(f"Unique item types: {total_keys}")

    nested_invt = {value: {key: value} for (key, value) in inventory.items()}
    print(nested_invt)


    print("\n=== Current Inventory ===")
    for key in inventory:
        percentage = "%.1f" % ((inventory[key] / values_total) * 100)
        print(f"{key}: {inventory[key]}", end="")
        if inventory[key] == 1:
            print(" unit ", end="")
        else:
            print(" units ", end="")
        print(f"({percentage}%)")

    print("\n=== Inventory Statistics ===")


if __name__ == "__main__":
    main()

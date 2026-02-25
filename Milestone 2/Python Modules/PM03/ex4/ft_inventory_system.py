# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 19:24:14 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/25 13:17:03 by joshde-s        ###   ########.fr        #
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
    values: list[int] = inventory.values()
    values_total: int = 0
    for value in values:
        values_total += value
    print(f"Total items in inventory: {values_total}")
    total_keys: int = len(inventory)
    print(f"Unique item types: {total_keys}")

    print("\n=== Current Inventory ===")

    sorted: dict[dict: int[str, int]] = {}
    biggest: int = 0
    smallest: int = values_total
    for key in inventory:
        if inventory[key] > biggest:
            biggest = inventory[key]
        if inventory[key] < smallest:
            smallest = inventory[key]
    saved_biggest = biggest

    while biggest > -1:
        for key in inventory:
            if inventory[key] == biggest:
                if sorted.get(inventory[key], False) is False:
                    temp = {key: inventory[key]}
                    sorted.update({inventory[key]: temp})
                else:
                    sorted[inventory[key]].update({key: inventory[key]})
            else:
                if sorted.get(inventory[key], False) is False:
                    temp = {key: inventory[key]}
                    sorted.update({inventory[key]: temp})
                else:
                    sorted[inventory[key]].update({key: inventory[key]})
        biggest -= 1

    biggest = saved_biggest
    while biggest > -1:
        if sorted.get(biggest, False) is not False:
            for key in sorted[biggest]:
                percentage = (sorted[biggest][key] / values_total) * 100
                float_percentage = "%.1f" % percentage
                print(f"{key}: {sorted[biggest][key]}", end="")
                if biggest == 1:
                    print(" unit ", end="")
                else:
                    print(" units ", end="")
                print(f"({float_percentage}%)")
        biggest -= 1

    print("\n=== Inventory Statistics ===")
    most_key: str = None
    most_value: int = 0
    for key in sorted[saved_biggest]:
        if most_key is None:
            most_key = key
            most_value = sorted[saved_biggest][key]
    print(f"Most abundant: {most_key} ({most_value} units)")
    least_key: str = None
    least_value: int = 0
    for key in sorted[smallest]:
        if least_key is None:
            least_key = key
            least_value = sorted[smallest][key]
    print(f"Least abundant: {least_key} ({least_value} units)")

    print("\n=== Inventory Categories ===")
    nested: dict[dict: str[str, int]] = {}
    for key in inventory:
        if inventory[key] >= 4:
            if nested.get("Moderate", False) is False:
                moderate = {key: inventory[key]}
                nested.update({"Moderate": moderate})
            else:
                nested["Moderate"].update({key: inventory[key]})
        else:
            if nested.get("Scarce", False) is False:
                scarce = {key: inventory[key]}
                nested.update({"Scarce": scarce})
            else:
                nested["Scarce"].update({key: inventory[key]})

    print(f"{'Moderate'}: {nested['Moderate']}")
    print(f"{'Scarce'}: {nested['Scarce']}")

    print("\n=== Management Suggestions ===")
    restocks = sorted.get(1)
    restock_size = len(restocks)
    print("Restock needed: ", end="")
    for key in restocks:
        print(key, end="")
        if (restock_size > 1):
            restock_size -= 1
            print(", ", end="")
        else:
            print("")

    print("\n=== Dictionary Properties Demo ===")
    inv_dictionary: list[str: int] = inventory.items()
    print("Dictionary keys: ", end="")
    odd_even: int = 1
    for items in inv_dictionary:
        for key in items:
            if odd_even == 1:
                odd_even += 1
                print(key, end="")
                if (total_keys > 1):
                    total_keys -= 1
                    print(", ", end="")
                else:
                    print("")
            else:
                odd_even -= 1
    total_values: int = len(inventory)

    print("Dictionary values: ", end="")
    odd_even = 1
    for items in inv_dictionary:
        for key in items:
            if odd_even == 2:
                odd_even -= 1
                print(key, end="")
                if (total_values > 1):
                    total_values -= 1
                    print(", ", end="")
                else:
                    print("")
            else:
                odd_even += 1

    lookup: int = inventory.get("sword")
    if lookup:
        print("Sample lookup - 'sword' in inventory: True")
    else:
        print("Sample lookup - 'sword' in inventory: False")


if __name__ == "__main__":
    main()

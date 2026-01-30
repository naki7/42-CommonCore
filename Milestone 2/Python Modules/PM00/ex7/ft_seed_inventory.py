# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/23 15:30:27 by joshde-s        #+#    #+#               #
#  Updated: 2026/01/30 15:00:32 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(seed_type.capitalize(), " seeds:", quantity, "packets available")
    elif unit == "grams":
        print(seed_type.capitalize(), " seeds:", quantity, "grams total")
    elif unit == "area":
        print(seed_type.capitalize(), " seeds: covers", quantity,
              "square meters")
    else:
        print("Unknown unit type")

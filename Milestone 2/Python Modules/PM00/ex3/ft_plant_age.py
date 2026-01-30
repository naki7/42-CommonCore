# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/23 14:50:50 by joshde-s        #+#    #+#               #
#  Updated: 2026/01/30 14:58:50 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

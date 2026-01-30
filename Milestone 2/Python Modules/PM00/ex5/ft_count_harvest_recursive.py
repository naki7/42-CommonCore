# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/23 15:01:56 by joshde-s        #+#    #+#               #
#  Updated: 2026/01/30 14:58:31 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def recursive_helper(days):
    if days > 0:
        recursive_helper(days - 1)
        print("Day", days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recursive_helper(days)
    print("Harvest time!")

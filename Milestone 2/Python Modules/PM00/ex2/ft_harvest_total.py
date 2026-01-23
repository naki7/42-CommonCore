# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/23 14:47:07 by joshde-s        #+#    #+#               #
#  Updated: 2026/01/23 14:49:40 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_harvest_total():
	weight = int(input("Day 1 harvest: "))
	weight += int(input("Day 2 harvest: "))
	weight += int(input("Day 3 harvest: "))
	print("Total harvest: ", weight)

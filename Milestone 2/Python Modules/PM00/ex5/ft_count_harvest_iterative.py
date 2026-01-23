# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/23 15:01:24 by joshde-s        #+#    #+#               #
#  Updated: 2026/01/23 15:12:15 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_iterative():
	days = int(input("Days until harvest: ")) + 1
	for i in range(1, days):
		print("Day", i)
	print("Harvest time!")

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/23 14:57:11 by joshde-s        #+#    #+#               #
#  Updated: 2026/01/23 14:59:51 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_water_reminder():
	days = int(input("Days since last watering: "))
	if days > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")

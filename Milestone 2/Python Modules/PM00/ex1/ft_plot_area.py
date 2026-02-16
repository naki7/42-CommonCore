# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plot_area.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/23 14:38:42 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/16 13:30:12 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plot_area():
    length = input("Enter length: ")
    width = input("Enter width: ")
    area = int(length) * int(width)
    print(f"Plot area: {area}")

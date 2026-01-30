# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/30 15:38:31 by joshde-s        #+#    #+#               #
#  Updated: 2026/01/30 16:26:52 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def main():
    p1 = Plant('Sunflower', 100, 42)
    p2 = Plant('Orchid', 15, 97)
    p3 = Plant('Spekboom', 25, 61)
    plants = [p1, p2, p3]
    print("~~~Plant Database~~~")
    for i in range(0, 3):
        print(plants[i].name, ": ", plants[i].height, "cm, ", plants[i].age,
              " days old", sep="")


if __name__ == "__main__":
    main()

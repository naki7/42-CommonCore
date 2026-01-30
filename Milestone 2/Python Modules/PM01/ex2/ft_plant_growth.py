# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/30 16:17:10 by joshde-s        #+#    #+#               #
#  Updated: 2026/01/30 16:39:31 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant():
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    def grow(self, time):
        self.height += time * 0.75

    def age(self, time):
        self.days += time

    def get_info(self, time):
        self.grow(time)
        self.age(time)
        print(self.name, ": ", self.height, "cm, ", self.days,
              " days old", sep="")
        if time > 0:
            print("Growth in ", time, " days time is: ", (time * 0.75),
                  "cm", sep="")


def main():
    init_days = 16
    p1 = Plant('Spekboom', 5, init_days)
    print("~~~Day 1~~~")
    time = 0
    p1.get_info(time)
    time = 7
    print("~~~Day ", (time + 1), "~~~", sep="")
    p1.get_info(time)


if __name__ == "__main__":
    main()

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_intro.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: joshde-s <joshde-s@student.42porto.com>   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/30 15:20:46 by joshde-s        #+#    #+#               #
#  Updated: 2026/02/05 15:45:50 by joshde-s        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main() -> None:
    """
    Initializes a plant with basic attributes and prints them to the console.
    """
    name: str = 'Sunflower'
    height: float = 1.5
    age: int = 5
    print("~~~Loading into Garden~~~\n")
    print(f"Plant = {name}\nHeight = {height} meters")
    print(f"Age = {age} weeks\n\n~~~Exiting Garden~~~")


if __name__ == "__main__":
    main()

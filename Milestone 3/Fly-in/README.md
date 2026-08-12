*This project has been created as part of the 42 curriculum by joshde-s*

# Fly-in

## Description

### Overview

At its core the goal of this project is to create a pathfinding program that
    uses cost effective algorithms to take multiple drones from the start to
    the end of a map. The drones use nodes to traverse through the map, links
    between the nodes allow the drones to pass easier and even stay on them
    under very specific criteria. The maps themselves were given as examples
    and outlined specific ways that the maps can be setup and parsing these
    files was part of the challenge.

### Project Goals and Specifications

#### Step 1 - Parser
As the file specification for how the maps/drones/hubs should be configured
    is how any part of the program functions would rely on, it makes it the
    most important point to begin from.

The files themselves can have comments (which start with #s and are expected
    to be ignored).

Beyond that the setup for each is as follows:

_\<reference key\>: <name of hub\> \<x\> \<y\> \<[metadata]\>_

- The reference key typical is words like start_hub, end_hub, and hub.
- The name of the hub had to be one word and could not contain a - as this is
    used by the connection between hub names.
- The x refers to x position of the hub on a theoretical graph, and the y then
    refers to the y position of the hub
- The metadata is always specified within square brackets and involved keywords
    paired with specifications. This includes for example:

    _[color='blue' max_drones=8]_

The way the parser handles these files is by splitting the file by new lines,
    then splitting each line further by spaces to get the individual items. If
    statements are then used to validate each type of information and raising
    errors where the input fails the specifications.

#### Step 2 - Structure

The project had some slight specifications in the way that it needed to be
    setup but for the most part a lot of it was up to how the structure of if
    would be best suited to its function.

Pydantic was one of the primary uses for the structure. This allowed validation
    to extend further than just parsing the information as certain details would
    require default values where needed. For example if the color of a hub was
    not specified or more importantly if the max_drones or max_capacities were
    not specified for either hubs or connectiones, then a default of 1 max is
    then used.

Beyond that the structure for the objects themselves were done through 3 main
    classes. This included Drones, Hubs, and Connections. These three classes
    fulfilled the most important parts of the project which is holding all the
    information that would be required by the algorithm to calculate paths, to
    move the drones between connections and hubs, to translate all the current
    turn's data into a simulation state class which could then be used for
    visual representation.

The three classes would initially be set with their base details, and then they
    would be looped over to connect each other. For example, setting the drones
    to have the 'start' hub as their location to begin with, adding the needed
    hubs to the correct connections, as well as linking the hubs to the right
    connections and hubs that they required.

#### Step 3 - Pathfinding

This is where the primary magic of this project happens, and was the original
    purpose of starting the project. The pathfinding in this project is quite
    unique as pathfinding programs typically use literal distances to measure
    cost, also a lot of pathfinding is based around finding 1 individual best
    pathway through a map. These are both broken in this as the cost of the map
    rather comes toward how many turns a drone takes to move toward the goal,
    for example restricted hubs take 2 turns to move through (typically relying
    on their connections to hold the drone first), while also having multiple
    drones to manage at the same time can also impact movement costs as it can
    often be better long term to move a drone through a more expensive path as
    this will allow for other drones to move through the cheaper path at the
    same time, thus saving on drones moved per turn instead of turns per drone.

The algorithms will be explained further below, but the short of it is that
    multiple algorithms were needed to resolve this pathfinding. A version of A*
    algorithms were used to manage smaller maps with less than 10 hubs while all
    other maps used base dijkstra to find the best paths. The main difference
    between the two is that A* can handle small inputs with high efficiency
    but can get stuck in loops and dead ends in bigger maps. Where as dijkstra
    has the opposite results.

#### Step 4 - Bypassing Restrictions

Some key elements that made this project unique were the algorithm dealing with
    multiple drones at the same time, each hub could be set to 1 of four states
    such as normal and priority which take 1 turn for drones to move, while
    restricted hubs tooks 2 turns and blocked hubs could not be moved to. These
    cases were mostly hinderances to the algorithms that were used and would
    either make the algorithm calculate more pathways to see costs for multiple
    drones as a cost ineffecient path might long term result in an over all low
    turn count. While some blocked paths would result in dead ends that drones
    could get stuck in. Mean while restricted and priority hubs might cause
    drones to take paths that would lead to loops or long paths even though low
    costs would be viable through the opposite path compared to what most
    algorithms would predict would be useful.

Most of these situations are resolved by using the two different algorithms
    based on hub count alone.

#### Step 5 - Terminal Visuals

The terminal visuals were mostly easy to manage as I quite early on used an
    external function to print turn results instead of leaving it within the
    algorithm which would be messier and more confusing. This was then quite
    easy to later on change this function to instead create a storable string
    output. This was very handy as it allowed me to create a functionality that
    was not specified but visually resulted better than what could have been.
    This refers to the way that when Pygame is running the visual output, the
    program stores the expected turn outputs so that once the window is closed
    it can either continue posting the terminal, or if the program is finished,
    then it will output all the turns one after another so that the user can
    still refer to the processes without rerunning the program. This also makes
    it easier for outputting the end of program stats like how many turns the
    drones took in total, or how many turns it took for the program to finish
    moving all the drones to the end.

#### Step 6 - Graphical Output

To create the graphical components, Pygame, which is a python graphical library
    was used. Pygame was mostly simple to handle, however the randomness in
    terms of both the number of hubs that could be requested, and the colours
    that might be specified in the text file caused quite a bit of extra
    managing. While Pygame as it currently is accounts for many different
    colour names, it however does not account for all the colours that were
    given as examples. To resolve this, if statements were implemented to check
    for these abnormal colour names and then rerouting them through a different
    but similar colour name that pygame understands. To account for out of the
    if statement situations, a ValueError check is in place to catch the error
    thrown by pygame, and then retry the same thing but with a default colour.
    Laslty, an if statment is used to account for the fact that colours of
    vastly different saturations are called for. This can create issues with
    readability so some of these colours are replaced with a colour of the same
    hue but a better saturation and/or contrast.

The sizing of the screen to the number of hubs also presented a problem as a
    lot of the hubs that were manually drawn were too big to fit on the screen
    for larger working spaces. This was accounted for by creating a smaller
    shape sizing and distancing for those few maps, as well as adjust the y
    values from the extra x spacing for one map so that the same style could
    be maintained across the base maps.

### Algorithm Choices and Implementation Strategy

The initial implementation of the program took an A* inspired approach, which
    takes priority in finding a cheap path through the map by checking the
    costs (number of turns to move) by looking at the cost of the neighbors
    of the current hub, and then getting the costs of those neighbors' neighors
    thus adding multiple dimensions of length, putting them together and then
    seeing which out of the neighbor pairs would be the cheapest move to go to
    the goal. This overall worked really well and produced very efficient runs
    that tended to have very low number of turns to get all the drones to the
    goal. However, as this would run very live on actively changing drone
    locations, and hub capacities, this let multiple drones move at once well,
    but when encountering larger maps with large amount of loops, the drones
    could easily get stuck in dead ends as they would move into space to make
    space for other drones without considering the final result of such a move.

To solve the issue of large maps, I implemented a Dijkstra algorithm to solve
    the further paths that lead to the goal. The difference with this (since A*
    is based on Dijkstra) is that the algorithm tries to look for the actual
    end of the maze before starting to walk. This means that it is a lot more
    likely to find the goal and the hubs to take to get there. However, as it
    does all the cost checks in one step, it then lacks the flexibility that
    A* has as it will try moving all drones through the same "cheapest" path.

### Visual Representation Features

As mentioned above, both a terminal and graphical approach was implemented in
    this project. The terminal approach uses the base output that is expected
    of which drones move and what hub/connection they moved to during that turn
    with only 1 turn being printed per newline. This was easy to convert into a
    more readable terminal output by using the library Rich, which allowed the
    print outputs to be associated with either the specified or default colour.

Pygame was used as mentioned above for the graphical output. This was made
    pretty simple as pygame is pretty robust with how shapes are created and
    colours can be directly pulled. The simplest way I found to use it was to
    pair its inbuilt sizing and positioning system of drawn objects along with
    the hubs x and y positions. These positions were normalized to start at 0
    where possible and then increase from there to fill the space with all the
    hubs. The connections were then lines that were drawn directly between the
    hub x and y positions. The image of hubs and connections were then copied
    so that they could be blit'ed onto the screen to remove drones that had
    moved and then redrawing the drone locations through their current location
    using that x and y value, matching to the center of the hub rectangles.

## Instructions

### Installation

Due to the fact that this program requires both pydantic, rich and pygame to be
    installed before running, the Makefile create a virtual environment to run
    the program in and install all the dependencies. First run:

    ```
    make install
    ```

Then to enter the virtual environment use the command:

    ```
    source ./matrix/bin/activate
    ```

To leave the virtual environment simply call the command:

    ```
    deactivate
    ```

If you would like to run typing and syntax checks you can run these commands
    (note this is best done before using make install, or after using make
    clean - ensuring you are also outside of the virtual environment):

    ```
    make lint
    make lint-strict
    ```

### Executing the Program

To then execute Fly-in you can call the following terminal commands:

    ```
    make run FILE=<optional_file_path> OUTPUT=<optional_argument>
    ```
In the above template the text in between <> can be replaced with the required
    file directories, and file names. The optional_argument if left blank will
    automatically run the program in an only terminal output mode. If the
    argument 'terminal' is used, the same will happen, while if 'pygame' is
    specified this will run the program to output only using the graphical
    display, and lastly, if 'both' is used, it will then run both the terminal
    output and the graphical display.

While running pygame, you can press 'esc' key or the close terminal UI button
    and the pygame will close. The program will continue running and produce
    terminal output instead. You can force close the terminal output/program
    early like normal using 'Ctrl+c' on the terminal.

### Example Input and Expected Output

For the files, I would suggest using the ones provided or creating a txt file
    with inputs like this:

    ```
    nb_drones: 2

    start_hub: start -1 0 [color=green]
    hub: waypoint1 1 1 [zone=restricted color=blue]
    hub: waypoint2 2 1 [zone=priority color=blue]
    hub: waypoint3 3 1 [zone=restricted color=blue]
    hub: waypointA 1 2 [zone=priority color=blue]
    hub: waypointB 2 2 [zone=priority color=blue]
    hub: waypointC 3 2 [color=blue]
    end_hub: goal 3 3 [color=red]

    connection: start-waypoint1
    connection: start-waypoint2
    connection: start-waypoint3
    connection: waypoint1-waypointA
    connection: waypoint1-waypointB
    connection: waypoint2-waypointA
    connection: waypoint2-waypointB
    connection: waypoint2-waypointC
    connection: waypoint3-waypointB
    connection: waypoint3-waypointC
    connection: waypointA-waypointB
    connection: waypointB-waypointC
    connection: waypointB-goal
    connection: waypointC-goal
    ```

Lastly, you can then run the below command if all files are in place:

    ```
    make run FILE=./maps/easy/test.txt OUTPUT=pygame
    ```

## Resources

### Algorithms

- [Pathfinding](https://en.wikipedia.org/wiki/Pathfinding) — general pathfinding info
- [A* algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) — A* pathfinding info
- [Dijkstra algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) — Dijkstra pathfinding info

### Pygame & Rich

- [Pygame Tutorial](https://www.geeksforgeeks.org/python/pygame-tutorial/) — basic Pygame info
- [Pygame Surface Tutorial](https://www.geeksforgeeks.org/python/pygame-surface/) — info on Surfaces in Pygame
- [Deep Dive Pygame Surface Info](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.copy) - Deeper information about surfaces in pygame
- [Deep Dive Pygame Color Info](https://www.pygame.org/docs/ref/color.html) - Deeper information about colors in pygame
- [Pygame Text Tutorial](https://www.geeksforgeeks.org/python/pygame-working-with-text/) — info on Text in Pygame
- [Pygame Object Tutorial](https://www.geeksforgeeks.org/python/pygame-drawing-objects-and-shapes/) — info on creating Shapes in Pygame
- [Pygame Key Input Tutorial](https://www.geeksforgeeks.org/python/how-to-get-keyboard-input-in-pygame/) — info on using keyboard inputs in Pygame

- [Basics of Rich](https://rich.readthedocs.io/en/latest/introduction.html) — info on using the Rich Python library for colors and terminal output

### AI usage

AI was primarily used to refine some resources as some were leading to dead
    ends or were producing results unrelated to my specific issues. AI was also
    used as a tool to validate some steps such as struggles around looping and
    dead-end errors within the algorithm logic that I had already coded.

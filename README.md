# This is my final version of the blue jumping 'frog' who's goal is to get past the muddy walls and throught the clearing near the tree (largest pillar)

To Run the simulation (I recommend to change numberOfGenerations / populationSize to at least 12 for the best results)
You can use the terminal and enter the directory where the files are, typing in "python3 search.py" 
Alternatively you could also run button.py in a similar way

The fitness function optimizes the robot by heading in the direction of the corner (the sum of the negative x and negative y position of the world), and in turn ultimately avoiding the walls and any obstacles in its way in order to get through the clearing.
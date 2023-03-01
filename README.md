# This is my final version for Assignment 8

To Run the simulation, you can use the terminal and enter the directory where the files are, typing in "python3 search.py" 
Alternatively you could also run button.py in a similar way. Since there is a glitch with the UTC encoding, simply close and rerun the simulation if it crashes at any point.

Since the possible shape generations are very random, I'd recommend running the simulation multiple times.

What I did:

Almost all of my changes occured within the simulation.py file as well as some minor tweaks within the parallelHillClimber.py file.

The Create Body() method in the solution.py file utilized a list of arbitrary variables to decide body generation. To improve this, I decided to create three different lists of random values, namely "limbs", "allSizes", and "directions" in the init function of the solution class. These lists are in charge of deciding the size and axis of each joint, as well as the direction in which they are positioned and where they are added. 

To allow for mutations, I updated the Mutate() method to change one value in each of these lists at a time at random. As a result, the body might change in terms of joint size, joint axis, direction, and location. Importantly, no modifications were made to the create brain function.

The body, like the brain, changes one element at a time, with the fitness of the kid determining whether the characteristic is passed on to the next generation. But, I ran into a situation where the bots would add parts instead of developing to move, so I disabled the ability for the bodies to grow or lose limbs. This is something I intend to address in future assignments as there are still some funky creatures that are created with impromper dimensions/limbs as well as not adhering to the laws of physics exactly as I want them to. Therefore, that is something that I have to tackle when it comes to future assignments.

A diagram of how I mutated the bodies is shown below:

![Untitled Notebook-2](https://user-images.githubusercontent.com/115434259/222054614-06da92e3-7f88-44cc-b592-19e946672d86.jpg)

A diagram of the five fitness plots of five seeds is also shown below:

<img width="630" alt="Screen Shot 2023-02-28 at 8 25 01 PM" src="https://user-images.githubusercontent.com/115434259/222054536-25362fbb-6615-4581-b8b4-eee060a96342.png">


Robot could not have been built without the help of the following resources:
https://www.reddit.com/r/ludobots/
https://www.thunderheadeng.com/pyrosim



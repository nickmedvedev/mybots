# This is my final version for Assignment 7

To Run the simulation, you can use the terminal and enter the directory where the files are, typing in "python3 search.py" 
Alternatively you could also run button.py in a similar way

Since the possible shape generations are very random, I'd recommend running the simulation multiple times.

What I did:

The Create_Body() function was modified the most within solution.py for this assignment and a random position for each block to be placed accordingly was selected with options from the x and y axis and the positive z direction.

To avoid any overlapping of links, I implemented a loop that selects a new position for a link to add to the body if there's already a link coming out of the currently selected link in the uniform direction. I also devised a way to prevent joining links in the opposite direction by choosing a different direction. The joint placement was the most difficult element, since I utilized an if statement for each of the possible orientations to establish the joint's position. 

I made some other notable changes in simulation.py by cleaning up the GUI window and fixing some of the constants that were preventing the robot from fully moving. While any body type is technically possible with the random approach I decided to take, there's still a possibility of limbs overlapping that is dependent on the generation luck. In order to fix this problem, a complete overhaul of my approach to Create_Body() may be necessary. When it comes to the brain of the robot, the adjacent sensors of the respective motors control them. Hence, due to the creatures random movements, there is no real way to predict a clear movement style for the robot. Therefore, in the simplest way, the sensors linked to motors will act as 'legs' for the robot and cause the robot to move in the desired direction.

Some of the possible 3d creatures are shown below:

<img width="153" alt="Screen Shot 2023-02-20 at 11 54 31 PM" src="https://user-images.githubusercontent.com/115434259/220259911-56ea3e87-af82-4555-b6d9-77902c37e294.png">

<img width="189" alt="Screen Shot 2023-02-20 at 11 59 05 PM" src="https://user-images.githubusercontent.com/115434259/220260020-e257cd7b-86b4-4145-8871-c6ef76a91efb.png">

<img width="185" alt="Screen Shot 2023-02-21 at 12 00 07 AM" src="https://user-images.githubusercontent.com/115434259/220260153-47ad68ee-69c5-4c13-b228-8bd668441921.png">

Robot could not have been built without the help of the following resources:
https://www.reddit.com/r/ludobots/
https://www.thunderheadeng.com/pyrosim



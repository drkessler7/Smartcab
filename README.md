## Smartcab

### Overview
Autonomous (self-driving) cars are one of 4 innovations expected to disrupt the automotive industry. Driven by shared mobility, connectivity services and feature upgrades, new business models could expand automotive revenue pools by 30%, adding up to $1.5 trillion in profits. 

Safety is another huge motivator in the production of autonomous vehicles. Researchers estimate driverless cars will save 10 million lives per decade! And as this technology progresses, autonomous cars will surpass the driving skills of humans, translating into even more millions of lives saved. Current projections show as many as 10,000,000 self-driving cars on the road by 2020, with up to 15% of new cars sold in 2030 as fully autonomous.

Given the changing nature of engineering, and other industries across the globe, I completed this project as part of a continuing education program at Udacity. Engineering requires staying up-to-date on the latest tools and trends, to produce superior results. This was a fun and worthwhile project that allowed me to hone, sharpen and grow my skills, to guarantee just that.

### Problem
In order for autonomous vehicles such as smartcabs to become a reality, the systems within each vehicle must be produced to extreme quality. With passenger safety on the line, there is no room for error. This project shows how reinforcement learning allows vehicles to take in data from their surrounding environments, and make the proper decisions to ensure safe trips.

This problem that smartcabs face is very complex. When navigating, vehicles need to consider things like the presence of other vehicles, pedestrians, animals, or other road hazards. Beyond that, they need to be aware of lanes, signs, lights, destinations, and routes. 

In this project, the problem is replicated on a small scale grid that consists of streets and intersections. At each intersection there is a traffic light. Throughout the map are other cars making random turns at intersections as they move through the grid. 

### Process

#### Data Description
The data used in this project comes in the form of numerical and string input from the environment. The smartcab agent is told simple pieces of information such as if the light is red or green, and if there is another car approaching from the left, right, or oncoming direction towards the agent. A numerical reward is also given, and is described later. 

#### Naive Smartcab
To start the project, the smartcab is given no guidance. It simply makes random decisions about where it will go. It pays no attention to where the destination is. The smartcab gets input from the environment, but it does not process this information in any way, and so it does not learn. This naive agent reaches its destination only about 18% of the time, and makes many of mistakes along the way.

#### Implementing Q-Learning (Reinforcement Learning)
Next, the smartcab is given the tools to learn from its environment. It does this through something called ‘Q-learning’, which is an iterative process. The agent starts off with no knowledge of what will happen if it takes a certain action. As it navigates the environment, it takes note of what it sees (lights, other cars, etc.), and takes some action. The environment then gives it either a positive or negative reward for that action. 

As the agent continues to navigate through the environment, it collects more rewards. Eventually, it will encounter a situation that it has seen before. It will then remember the action it took in that situation, and the reward it received. If it was positively rewarded for taking a certain action before, it might take a similar action now. If it was negatively rewarded, it might take a different action this time. This process continues until the smartcab knows what to do in any situation.

#### Model Improvement
To improve the learning process of the smartcab agent, three mathematical parameters are tuned. Different combinations of values for these are tried, and their corresponding results are compared. By doing this, I am able to improve the way that the smartcab agent learns. 

#### Results
After tuning parameters of the Q-learning algorithm, the smartcab is able to consistently reach its destination without incurring any penalties. It is able to do this with a minimum number of moves. This translates into completely safe and efficient trips. At this point, the goals of the project are considered to be satisfied.   

#### More Information
The ‘Report.pdf’ document in this repository contains all of the questions and answers that are required by Udacity to meet specifications for this project. It first addresses the case of a smartcab that does not take input from its environment to reach the intended destination. Q-learning (reinforcement learning) is then described on conceptual and mathematical levels. Finally, a description of the q-learning parameters and their tuning is provided. 

### Code Availability
The Python code for the trained smartcab can be found in the folder ‘Final Smartcab/smartcab’ as ‘agent.py’. The ‘environment.py’, ‘planner.py’, and ‘simulator.py’ files in that same folder provide the simulated environment for the smartcab.

## About Files/Folders in this Repository
* ‘Final Smartcab’: This folder contains the Python 2.7 scripts and image files that produce the fully trained smartcab, as well as its environment.

* ‘Smartcab Starter Files’: This folder contains the Python 2.7 scripts and image files that are supplied by Udacity. These scripts produce the aimlessly wandering smartcab, as well as its environment.

* ‘Smartcab Images’: This folder contains images of the smartcab navigating its environment, as well as the parameters that are tuned during smartcab training.

* ‘Report.pdf’: This files documents all of the questions and answers that are required by Udacity to meet specifications for this project.

## Requirements 
This project requires **Python 2.7** and the following Python libraries to be installed:
* [pygame](https://www.pygame.org/wiki/GettingStarted#Pygame_Installation)


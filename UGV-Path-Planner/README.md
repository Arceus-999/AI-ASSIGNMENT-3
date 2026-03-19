UGV Tactical Path Planner 
--------------------------------------------------

This project implements a path planning system for an Unmanned Ground Vehicle (UGV) using the A* algorithm. The goal is to navigate a 70 x 70 grid while avoiding obstacles and finding the most efficient path from a start point to a goal point.

About the Program
--------------------------------------------------

This program shows a battlefield environment where a UGV must travel from a given start location to the goal. The grid represents the terrain, and obstacles are randomly placed based on a selected density level.
The system uses The A* algorithm to compute the shortest path while considering both distance traveled and estimated distance to the goal. This makes it more efficient than basic search algorithms.

Features
--------------------------------------------------

Dynamic Obstacle Density :



Low (10%) → Open terrain

Medium (20%) → Moderate obstacles

High (30%) → Dense obstacles


--------------------

8-Way Movement : 
    
Supports horizontal, vertical, and diagonal movement

--------------------

Tactical Visualization :



Grey background → Grid

Red squares → Obstacles

Blue square → Start node

Orange square → Goal node

Green line → Shortest path

--------------------

Provide inputs when prompted :



Enter obstacle density (1, 2, or 3)

Enter Start coordinates (0–69)

Enter Goal coordinates (0–69)

A* Search Algorithm
--------------------------------------------------

The A* algorithm calculates the best path using the function

f(n) = g(n) + h(n)

g(n) → Cost from start node to current node

h(n) → Estimated cost from current node to goal (Euclidean distance)

f(n) → Total cost used to decide the optimal path

By minimizing f(n), the algorithm efficiently finds the shortest possible route while avoiding unnecessary exploration.

Measures of Effectiveness (MoE)
--------------------------------------------------

The system evaluates performance using the following metrics

Path Success :
Indicates whether a valid path was found

Total Path Length :
Number of steps taken to reach the goal

Obstacle Density Avoided :
Percentage of obstacles in the grid

Output
--------------------------------------------------

Displays whether a path is found or not

Shows total path length

Visualizes the battlefield grid with path and obstacles


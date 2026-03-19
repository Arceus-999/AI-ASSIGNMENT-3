UGV Dynamic Navigation Project Overview
-----------------------------------------------

This project shows a UGV moving across a grid while avoiding obstacles that can change over time. The main goal is to travel from a starting point to a destination using the most efficient path possible, even when the environment is uncertain and constantly changing.

Navigation Algorithm Used: D Star Lite
----------------------------------------------

The system uses the D Star Lite algorithm for path planning. This algorithm is designed for dynamic environments where conditions are not fixed.

It updates only the affected part of the path when obstacles change

It avoids recomputing the entire path from scratch, making it faster

It allows the vehicle to continuously adjust its route toward the goal

Key Features
-------------------------------------------------------------------------
Dynamic Environment

---------------------------

Obstacles can appear or disappear during the simulation

This represents real-world uncertainty such as moving objects or changing terrain

The environment is not static and keeps evolving over time

Limited Sensor Range

------------------------------------

The vehicle does not know the full map in advance

It can only detect obstacles within a certain radius around its current position

As it moves, it gradually builds its own internal map based on sensor readings

Safety Handling

---------------------------------------

Before moving, the system checks the actual environment

If a path becomes blocked unexpectedly, the vehicle avoids the move

The system then recalculates a new path to continue navigation safely

Measures of Effectiveness
-----------------------------------------------------

The simulation evaluates performance using several metrics:

Goal success indicates whether the vehicle reached the destination

Steps taken shows how many moves were required

Replanning events counts how often the path had to be updated

Total sensor scans indicates how often the environment was observed

Visual Map 
-----------------------------------------------------------

The final grid visualization uses simple symbols to represent the environment:

S represents the starting position

G represents the goal or destination

● shows the path taken by the vehicle

█ represents obstacles that were detected and avoided

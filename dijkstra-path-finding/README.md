Dijkstra Path Finding 
--------------------------------------------------

This project is a implementation of Dijkstra’s Algorithm to find the shortest path between cities in India. The program takes a source and destination as input and calculates the minimum distance along with the route.

About the Project
--------------------------------------------------

This project finds a pathfinding system where cities are treated as nodes and the distances between them as edges. Using Dijkstra’s algorithm, the program finds the shortest route between any two selected cities.
A predefined set of around 20 major Indian cities is used, and the distances between them are stored in a graph using an adjacency matrix.

Features
--------------------------------------------------

Graph Network :

The program uses a pre-defined adjacency matrix that stores real-world distances forming a fixed network for pathfinding.

Dijkstra’s Method :

It applies Dijkstra’s algorithm, a greedy method that continuously selects the nearest unvisited city to determine the shortest path from the source to the destination.

Path Reconstruction :

After computing the shortest path, the program traces the route using a recursive function (printPath), showing the exact sequence of cities traveled.

Input Validation :

The system checks user inputs carefully to ensure valid city indices, preventing errors such as invalid memory access.

How It Works
--------------------------------------------------
Data Mapping :
Cities are mapped to integer indices for easier computation

HOW THE ALGORITHM WORKS

Initialization :
The distance to the source city is set to 0, while all other cities are assigned a very large value (infinity) to indicate they are not yet reachable.

Selection :
From the unvisited cities, the algorithm selects the one with the smallest known distance from the source. This ensures we always expand the closest possible path.

Formula :
For each neighboring city, the algorithm checks whether going through the current city gives a shorter path than the previously recorded one. If it does, the distance is updated.

dist[v] = min(dist[v], dist[u] + weight(u, v))

Iteration :
This process continues, marking cities as visited one by one, until the destination city is reached or all possible paths have been explored.

Output
--------------------------------------------------

Displays the shortest distance between the selected source and destination cities along with the optimal path showing the sequence of cities traveled.

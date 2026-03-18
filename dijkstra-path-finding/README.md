Dijkstra Path Finding 
--------------------------------------------------

This project is a implementation of Dijkstra’s Algorithm to find the shortest path between cities in India. The program takes a source and destination as input and calculates the minimum distance along with the route.

About the Project
--------------------------------------------------

This project finds a pathfinding system where cities are treated as nodes and the distances between them as edges. Using Dijkstra’s algorithm, the program finds the shortest route between any two selected cities.
A predefined set of around 20 major Indian cities is used, and the distances between them are stored in a graph using an adjacency matrix.

Features
--------------------------------------------------

Finds shortest path between two cities
Displays total distance in kilometers
Prints the complete route taken
Handles invalid input cases
Uses adjacency matrix representation

How It Works
--------------------------------------------------

Graph Initialization :
A 20 x 20 matrix is initialized with a large value (INF) to represent no connection

Data Mapping :
Cities are mapped to integer indices for easier computation

Algorithm Execution :
The source node is assigned a distance of 0
Distances are updated by checking neighboring nodes for shorter paths

Relaxation Formula :
dist[v] = min(dist[v], dist[u] + weight(u, v))

Path Reconstruction :
A parent array is used to trace and print the final shortest path

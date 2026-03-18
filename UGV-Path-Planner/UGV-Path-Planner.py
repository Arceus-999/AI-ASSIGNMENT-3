import numpy as np
import matplotlib.pyplot as plt
import heapq

def astar(grid, start, goal):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
   
    fscore = {start: np.sqrt((start[0]-goal[0])**2 + (start[1]-goal[1])**2)}
    oheap = []
    heapq.heappush(oheap, (fscore[start], start))
 
    while oheap:
        current = heapq.heappop(oheap)[1]
        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data[::-1] 

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
        
            move_cost = np.sqrt(i**2 + j**2)
            tentative_g_score = gscore[current] + move_cost
            
            if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1]:                
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue
            else:
                continue
 
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
 
            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + np.sqrt((neighbor[0]-goal[0])**2 + (neighbor[1]-goal[1])**2)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))
    return None

def get_single_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if 0 <= val < 70:
                return val
            else:
                print("Error: Coordinate must be between 0 and 69.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


print("UGV Battlefield Navigation System ")
d_choice = input("Select Obstacle Density (1: Low 10%, 2: Med 20%, 3: High 30%): ")
density = {'1': 0.1, '2': 0.2, '3': 0.3}.get(d_choice, 0.1)

print("\nStart Node Configuration")
sx = get_single_int("Enter Start X-coordinate: ")
sy = get_single_int("Enter Start Y-coordinate: ")
start_node = (sy, sx) 

print("\nGoal Node Configuration")
gx = get_single_int("Enter Goal X-coordinate: ")
gy = get_single_int("Enter Goal Y-coordinate: ")
goal_node = (gy, gx)


grid_size = 70
grid = np.zeros((grid_size, grid_size))
obs_count = int(grid_size * grid_size * density)
count = 0

while count < obs_count:
    rx, ry = np.random.randint(0, grid_size), np.random.randint(0, grid_size)
   
    if (rx, ry) != start_node and (rx, ry) != goal_node and grid[rx, ry] == 0:
        grid[rx, ry] = 1
        count += 1

path = astar(grid, start_node, goal_node)

fig, ax = plt.subplots(figsize=(10, 10))

ax.set_facecolor('#F0F0F0') 
plt.imshow(grid, cmap='Greys', origin='lower', alpha=0) 

obs_y, obs_x = np.where(grid == 1)
ax.scatter(obs_x, obs_y, color='red', marker='s', s=45, label='Obstacles')

ax.plot(sx, sy, 'bs', markersize=10, label='Start State')

ax.plot(gx, gy, marker='s', color='#FF8C00', markersize=10, label='Goal State')

if path:
    
    py, px = zip(*path)
    ax.plot(px, py, color='#00FF00', linewidth=3.5, label='Optimized Path')
  
    path_len_units = len(path)
    euclidean_dist = np.sqrt((start_node[0]-goal_node[0])**2 + (start_node[1]-goal_node[1])**2)
    path_efficiency = (euclidean_dist / path_len_units) * 100

    print(f"Measures of Effectiveness\n")
    print(f"1. Path Found: Successful")
    print(f"2. Total Path Length: {path_len_units} units")
    print(f"3. Obstacle Density Avoided: {int(density*100)}%")
else:
    print(" Measures of Effectiveness\n")
    print("Path Found: Unsuccessful (Goal unreachable with current obstacle density)")

plt.title(f"UGV Tactical Pathfinding")
plt.xlabel("X-Coordinate")
plt.ylabel("Y-Coordinate")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', frameon=True, shadow=True)
plt.grid(True, color='white', linestyle='-', linewidth=0.7)
plt.tight_layout()
plt.show()
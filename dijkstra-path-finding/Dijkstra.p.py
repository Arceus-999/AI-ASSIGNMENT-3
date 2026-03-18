import sys

# Constants
INF = 999999
CITY_COUNT = 20

# City List (Identical to C version)
cities = [
    "Agra", "Delhi", "Lucknow", "Kanpur", "Ahmedabad", 
    "Mumbai", "Pune", "Jaipur", "Udaipur", "Bengaluru", 
    "Hyderabad", "Chennai", "Goa", "Bhubaneswar", "Kolkata", 
    "Vishakhapatnam", "Patna", "Kochi", "Varanasi", "Thiruvananthapuram"
]

# Initialize Graph with INF (2D List)
graph = [[INF for _ in range(CITY_COUNT)] for _ in range(CITY_COUNT)]
for i in range(CITY_COUNT):
    graph[i][i] = 0

def get_index(name):
    try:
        return cities.index(name)
    except ValueError:
        return -1

def add_edge(u, v, dist):
    i = get_index(u)
    j = get_index(v)
    if i != -1 and j != -1:
        graph[i][j] = dist

def print_path(parent, j):
    if parent[j] == -1:
        return
    print_path(parent, parent[j])
    print(f" -> {cities[j]}", end="")

def dijkstra(src, dest):
    dist = [INF] * CITY_COUNT
    parent = [-1] * CITY_COUNT
    visited = [False] * CITY_COUNT

    dist[src] = 0

    for _ in range(CITY_COUNT - 1):
        min_val = INF
        u = -1

        for v in range(CITY_COUNT):
            if not visited[v] and dist[v] <= min_val:
                min_val = dist[v]
                u = v

        if u == -1 or dist[u] == INF:
            break
        
        visited[u] = True

        for v in range(CITY_COUNT):
            if not visited[v] and graph[u][v] != INF and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u

    if dist[dest] == INF:
        print(f"\nNo path exists between {cities[src]} and {cities[dest]}.")
    else:
        print(f"\nShortest Distance: {dist[dest]} KM")
        print(f"Route: {cities[src]}", end="")
        print_path(parent, dest)
        print()

def main():
    # Data Population (Exact copy of your C data)
    add_edge("Agra", "Delhi", 240); add_edge("Agra", "Lucknow", 334); add_edge("Agra", "Kanpur", 277)
    add_edge("Ahmedabad", "Mumbai", 526); add_edge("Ahmedabad", "Pune", 663); add_edge("Ahmedabad", "Jaipur", 660); add_edge("Ahmedabad", "Udaipur", 258)
    add_edge("Bengaluru", "Pune", 839); add_edge("Bengaluru", "Hyderabad", 576); add_edge("Bengaluru", "Chennai", 346); add_edge("Bengaluru", "Goa", 562)
    add_edge("Bhubaneswar", "Kolkata", 442); add_edge("Bhubaneswar", "Vishakhapatnam", 444); add_edge("Bhubaneswar", "Patna", 831)
    add_edge("Chennai", "Hyderabad", 626); add_edge("Chennai", "Bengaluru", 345); add_edge("Chennai", "Kochi", 690); add_edge("Chennai", "Mumbai", 1335); add_edge("Chennai", "Kolkata", 1666)
    add_edge("Delhi", "Jaipur", 307); add_edge("Delhi", "Agra", 243); add_edge("Delhi", "Lucknow", 548); add_edge("Delhi", "Chennai", 2208); add_edge("Delhi", "Bengaluru", 2174); add_edge("Delhi", "Mumbai", 1452); add_edge("Delhi", "Hyderabad", 1582)
    add_edge("Goa", "Hyderabad", 674); add_edge("Goa", "Kochi", 755); add_edge("Goa", "Mumbai", 585); add_edge("Goa", "Pune", 442); add_edge("Goa", "Thiruvananthapuram", 1305)
    add_edge("Hyderabad", "Pune", 562); add_edge("Hyderabad", "Bengaluru", 576); add_edge("Hyderabad", "Chennai", 627); add_edge("Hyderabad", "Goa", 674); add_edge("Hyderabad", "Mumbai", 708); add_edge("Hyderabad", "Delhi", 1583); add_edge("Hyderabad", "Kolkata", 1489)
    add_edge("Jaipur", "Ahmedabad", 659); add_edge("Jaipur", "Udaipur", 397); add_edge("Jaipur", "Delhi", 308); add_edge("Jaipur", "Mumbai", 1170); add_edge("Jaipur", "Pune", 1191)
    add_edge("Kanpur", "Agra", 301); add_edge("Kanpur", "Lucknow", 115); add_edge("Kanpur", "Varanasi", 328)
    add_edge("Kochi", "Chennai", 690); add_edge("Kochi", "Bengaluru", 547); add_edge("Kochi", "Goa", 754); add_edge("Kochi", "Thiruvananthapuram", 206)
    add_edge("Kolkata", "Varanasi", 680); add_edge("Kolkata", "Patna", 554); add_edge("Kolkata", "Bhubaneswar", 442); add_edge("Kolkata", "Chennai", 1668); add_edge("Kolkata", "Delhi", 1563)
    add_edge("Lucknow", "Delhi", 553); add_edge("Lucknow", "Agra", 333); add_edge("Lucknow", "Kanpur", 89)
    add_edge("Mumbai", "Pune", 148); add_edge("Mumbai", "Ahmedabad", 526); add_edge("Mumbai", "Delhi", 1453); add_edge("Mumbai", "Hyderabad", 713); add_edge("Mumbai", "Bengaluru", 984); add_edge("Mumbai", "Kolkata", 1886); add_edge("Mumbai", "Chennai", 1338)
    add_edge("Patna", "Varanasi", 256); add_edge("Patna", "Kolkata", 578)
    add_edge("Pune", "Mumbai", 150); add_edge("Pune", "Ahmedabad", 660); add_edge("Pune", "Hyderabad", 560); add_edge("Pune", "Bengaluru", 842)
    add_edge("Thiruvananthapuram", "Kochi", 206); add_edge("Thiruvananthapuram", "Goa", 1305)
    add_edge("Udaipur", "Ahmedabad", 257); add_edge("Udaipur", "Jaipur", 397); add_edge("Udaipur", "Mumbai", 767); add_edge("Udaipur", "Delhi", 688)
    add_edge("Varanasi", "Kanpur", 328); add_edge("Varanasi", "Patna", 259); add_edge("Varanasi", "Kolkata", 683); add_edge("Varanasi", "Lucknow", 312)
    add_edge("Vishakhapatnam", "Bhubaneswar", 441); add_edge("Vishakhapatnam", "Hyderabad", 618); add_edge("Vishakhapatnam", "Kolkata", 882)

    # Print city menu
    for i in range(CITY_COUNT):
        print(f"[{i:2d}] {cities[i]:<18s}", end="")
        if (i + 1) % 3 == 0:
            print()
    
    # Simple Input Handling
    try:
        # input() pauses the script and waits for user entry
        s_input = input("\n\nEnter Source Index: ")
        d_input = input("Enter Destination Index: ")
        
        s = int(s_input)
        d = int(d_input)
        
        if 0 <= s < CITY_COUNT and 0 <= d < CITY_COUNT:
            dijkstra(s, d)
        else:
            print("Invalid index range.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    
    # This prevents the terminal from closing immediately on some systems
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
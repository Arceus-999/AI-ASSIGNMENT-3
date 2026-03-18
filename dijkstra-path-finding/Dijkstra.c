#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#define INF 999999
#define CITY_COUNT 20  

char *cities[CITY_COUNT] = {
    "Agra", "Delhi", "Lucknow", "Kanpur", "Ahmedabad", 
    "Mumbai", "Pune", "Jaipur", "Udaipur", "Bengaluru", 
    "Hyderabad", "Chennai", "Goa", "Bhubaneswar", "Kolkata", 
    "Vishakhapatnam", "Patna", "Kochi", "Varanasi", "Thiruvananthapuram"
};

int graph[CITY_COUNT][CITY_COUNT];

void initGraph() {
    for(int i=0; i < CITY_COUNT; i++) {
        for(int j=0; j < CITY_COUNT; j++) {
            graph[i][j] = (i == j) ? 0 : INF;
        }
    }
}

int getIndex(char *name) {
    for(int i=0; i < CITY_COUNT; i++) {
        if(strcmp(cities[i], name) == 0) return i;
    }
    return -1;
}

void addEdge(char *u, char *v, int dist) {
    int i = getIndex(u);
    int j = getIndex(v);
    if(i != -1 && j != -1) {
        graph[i][j] = dist;
    }
}

void printPath(int parent[], int j) {
    if (parent[j] == -1) return;
    printPath(parent, parent[j]);
    printf(" -> %s", cities[j]);
}

void dijkstra(int src, int dest) {
    int dist[CITY_COUNT], parent[CITY_COUNT];
    bool visited[CITY_COUNT];

    for (int i = 0; i < CITY_COUNT; i++) {
        dist[i] = INF;
        visited[i] = false;
        parent[i] = -1;
    }

    dist[src] = 0;

    for (int count = 0; count < CITY_COUNT - 1; count++) {
        int min = INF, u = -1;

        for (int v = 0; v < CITY_COUNT; v++)
            if (!visited[v] && dist[v] <= min) {
                min = dist[v];
                u = v;
            }

        if (u == -1 || dist[u] == INF) break; 
        visited[u] = true;

        for (int v = 0; v < CITY_COUNT; v++) {
            if (!visited[v] && graph[u][v] != INF && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
                parent[v] = u;
            }
        }
    }

    if (dist[dest] == INF) {
        printf("\nNo path exists between %s and %s.\n", cities[src], cities[dest]);
    } else {
        printf("\nShortest Distance: %d KM\n", dist[dest]);
        printf("Route: %s", cities[src]);
        printPath(parent, dest);
        printf("\n");
    }
}

int main() {
    initGraph();
    addEdge("Agra", "Delhi", 240); addEdge("Agra", "Lucknow", 334); addEdge("Agra", "Kanpur", 277);
    addEdge("Ahmedabad", "Mumbai", 526); addEdge("Ahmedabad", "Pune", 663); addEdge("Ahmedabad", "Jaipur", 660); addEdge("Ahmedabad", "Udaipur", 258);
    addEdge("Bengaluru", "Pune", 839); addEdge("Bengaluru", "Hyderabad", 576); addEdge("Bengaluru", "Chennai", 346); addEdge("Bengaluru", "Goa", 562);
    addEdge("Bhubaneswar", "Kolkata", 442); addEdge("Bhubaneswar", "Vishakhapatnam", 444); addEdge("Bhubaneswar", "Patna", 831);
    addEdge("Chennai", "Hyderabad", 626); addEdge("Chennai", "Bengaluru", 345); addEdge("Chennai", "Kochi", 690); addEdge("Chennai", "Mumbai", 1335); addEdge("Chennai", "Kolkata", 1666);
    addEdge("Delhi", "Jaipur", 307); addEdge("Delhi", "Agra", 243); addEdge("Delhi", "Lucknow", 548); addEdge("Delhi", "Chennai", 2208); addEdge("Delhi", "Bengaluru", 2174); addEdge("Delhi", "Mumbai", 1452); addEdge("Delhi", "Hyderabad", 1582);
    addEdge("Goa", "Hyderabad", 674); addEdge("Goa", "Kochi", 755); addEdge("Goa", "Mumbai", 585); addEdge("Goa", "Pune", 442); addEdge("Goa", "Thiruvananthapuram", 1305);
    addEdge("Hyderabad", "Pune", 562); addEdge("Hyderabad", "Bengaluru", 576); addEdge("Hyderabad", "Chennai", 627); addEdge("Hyderabad", "Goa", 674); addEdge("Hyderabad", "Mumbai", 708); addEdge("Hyderabad", "Delhi", 1583); addEdge("Hyderabad", "Kolkata", 1489);
    addEdge("Jaipur", "Ahmedabad", 659); addEdge("Jaipur", "Udaipur", 397); addEdge("Jaipur", "Delhi", 308); addEdge("Jaipur", "Mumbai", 1170); addEdge("Jaipur", "Pune", 1191);
    addEdge("Kanpur", "Agra", 301); addEdge("Kanpur", "Lucknow", 115); addEdge("Kanpur", "Varanasi", 328);
    addEdge("Kochi", "Chennai", 690); addEdge("Kochi", "Bengaluru", 547); addEdge("Kochi", "Goa", 754); addEdge("Kochi", "Thiruvananthapuram", 206);
    addEdge("Kolkata", "Varanasi", 680); addEdge("Kolkata", "Patna", 554); addEdge("Kolkata", "Bhubaneswar", 442); addEdge("Kolkata", "Chennai", 1668); addEdge("Kolkata", "Delhi", 1563);
    addEdge("Lucknow", "Delhi", 553); addEdge("Lucknow", "Agra", 333); addEdge("Lucknow", "Kanpur", 89);
    addEdge("Mumbai", "Pune", 148); addEdge("Mumbai", "Ahmedabad", 526); addEdge("Mumbai", "Delhi", 1453); addEdge("Mumbai", "Hyderabad", 713); addEdge("Mumbai", "Bengaluru", 984); addEdge("Mumbai", "Kolkata", 1886); addEdge("Mumbai", "Chennai", 1338);
    addEdge("Patna", "Varanasi", 256); addEdge("Patna", "Kolkata", 578);
    addEdge("Pune", "Mumbai", 150); addEdge("Pune", "Ahmedabad", 660); addEdge("Pune", "Hyderabad", 560); addEdge("Pune", "Bengaluru", 842);
    addEdge("Thiruvananthapuram", "Kochi", 206); addEdge("Thiruvananthapuram", "Goa", 1305);
    addEdge("Udaipur", "Ahmedabad", 257); addEdge("Udaipur", "Jaipur", 397); addEdge("Udaipur", "Mumbai", 767); addEdge("Udaipur", "Delhi", 688);
    addEdge("Varanasi", "Kanpur", 328); addEdge("Varanasi", "Patna", 259); addEdge("Varanasi", "Kolkata", 683); addEdge("Varanasi", "Lucknow", 312);
    addEdge("Vishakhapatnam", "Bhubaneswar", 441); addEdge("Vishakhapatnam", "Hyderabad", 618); addEdge("Vishakhapatnam", "Kolkata", 882);

    for(int i=0; i<CITY_COUNT; i++) {
        printf("[%2d] %-18s", i, cities[i]);
        if((i+1)%3 == 0) printf("\n");
    }
    
    int s, d;
    printf("\n\nEnter Source Index: ");
    if(scanf("%d", &s) != 1) return 1;
    printf("Enter Destination Index: ");
    if(scanf("%d", &d) != 1) return 1;
    
    if(s >= 0 && s < CITY_COUNT && d >= 0 && d < CITY_COUNT) {
        dijkstra(s, d);
    } else {
        printf("Invalid input.\n");
    }

    return 0;
}

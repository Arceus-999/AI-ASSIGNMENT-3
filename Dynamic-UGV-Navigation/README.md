Dynamic UGV Navigation
-----------------------------------------------------
In a static environment, things are simple.
The UGV gets a complete map, calculates the shortest path, and follows it.

But in a dynamic battlefield, the situation is unpredictable.Obstcales move, debris can fall, and terrain can change.

So the UGV cannot just follow a fixed path.
It must constantly observe, decide, and react.

The Main Idea: Plan Globally, Act Locally

Instead of using a single planning method, the system is divided into two parts.

Global Planning : This part works like planning a long trip.
It looks at the entire map and calculates the best path while avoiding known obstacles.
Common algorithms used are A star and Dijkstra.

However, this plan may become outdated when new obstacles appear.

Local Planning
----------------------------------------------------

This part acts like real time reflexes while driving.

It runs very frequently, usually every 10 to 100 milliseconds.
It uses sensors such as LiDAR or Radar to detect nearby objects.

Based on this, it continuously adjusts the vehicle’s speed and direction.Even if something suddenly appears, the UGV can avoid it.

How the UGV Avoids Moving Obstacles
------------------------------------------------------------
D star Lite

----------------------------------------------------

This algorithm helps in quick re-planning.

If a new obstacle blocks the path, instead of recalculating the entire route, it only updates the affected part.
This makes it much faster and efficient.


Artificial Potential Fields

--------------------------------------

This method treats the UGV like an object influenced by forces.

The goal pulls the UGV forward.
Obstacles push it away.As a result, the UGV naturally moves around obstacles.
However, sometimes it can get stuck when forces cancel each other.
That is why it is combined with a global planner.


Velocity Obstacles

-------------------------------------

This method predicts future collisions.

The UGV calculates the speed and direction of moving obstacles.It identifies dangerous velocities that could lead to collisions.Then it selects a safe velocity that avoids those paths.

How Performance is Measured
-----------------------------------------------------

Time to Collision :

This measures how close the UGV comes to a collision.
Higher values mean safer operation.

Path Smoothness :

This checks whether the movement is smooth or full of sudden turns.
Smooth paths indicate better control.

Mission Success Rate :

This is the percentage of times the UGV reaches the goal without collisions.

Re planning Speed :

This measures how quickly the system reacts to changes.
Faster response means better performance.

Static vs Dynamic Environments 

------------------------------------------------

In a static environment, everything is known in advance.
Planning is done once, and the shortest path is guaranteed.

In a dynamic environment, only partial information is known.
Planning happens continuously, and the path is updated in real time.

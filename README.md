# MO_TwoRobots
There is a factory. The floor of the factory is a rectangle divided into unit squares. Some unit squares are walls, others are empty. You are given the plan of the factory: a String[] in which each '#' represents a wall and each '.' an empty square.

There are two robots in the factory: robot A and robot B. Their current locations are denoted 'A' and 'B' in the plan.

Both robots move synchronously at one step per second. In each step the robot must move from its current square to one of the squares that share a side with its current square. The robots cannot leave the factory, they cannot move to a wall, they cannot both move to the same square, and they also cannot trade spaces.

Robot A wants to reach location marked 'a' in the plan, and robot B wants to reach location marked 'b' at the same time. (The starting locations of both robots and their destinations also count as empty squares. The robots may enter them arbitrarily many times.)

Compute and return the minimum time in which both robots can reach their desired destinations at the same time. If that is impossible, return -1 instead.

# Definition
 - Class:	TwoRobots
 - Method:	move
 - Parameters:	String[]
 - Returns:	int
 - Method signature:	int move(String[] plan)
  (be sure your method is public)
  
# Constraints
-	plan will contain between 1 and 40 elements, inclusive.
-	Each element of plan will contain between 1 and 40 characters, inclusive.
-	Each element of plan will contain the same number of characters.
-	plan will contain exactly one 'A', exactly one 'B', exactly one 'a', and exactly one 'b'.
-	Each other character in plan will be either '#' or '.'.

# References
- https://community.topcoder.com/stat?c=problem_statement&pm=16537

# Cycle_Detection
This project uses Python to solve the problem of detecting cycles in directed graphs using adjacency lists as input representing the directed graphs. 

## Input:
Multiple adjacency lists (prefaced each with the respecitve graph order) of simple directed graphs (no loops or multiple edges). The value 0 as graph order indicates the end of the input.

## Methodology:
Using a Depth First Search implementation (recursive version) to detect back edges to conclude whether the directed graph has a (directed) cycle or not.

## Output:
Output file containing statement whether the directed graphs are DAGs (directed acyclic graphs) or not.

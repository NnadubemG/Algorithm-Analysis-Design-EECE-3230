# Section 4: Questions and Answers

## 1. Graph storage
I store the input graph as an adjacency list. Each node has a list of its neighbors, so the program only stores edges that exist. This is a good fit for sparse graphs and uses about O(n + m) space. I also count the edges and sort neighbor lists so the visit order is consistent between runs. Each search keeps its own visited information and traversal order.

## 2. Third algorithm
I chose uniform-cost search. It expands the node with the lowest total path cost, using a priority queue. Since the graph has no edge weights in the input, every edge is treated as having cost 1. The algorithm therefore visits nodes in order of increasing distance from the start, although it is more general than BFS. With a binary heap, its time complexity is O((n + m) log n), and its extra space is O(n + m).

## 3. Information used by BFS and DFS
BFS uses a queue to process nodes in the order they are discovered. A visited set prevents the program from processing the same node repeatedly, and a list records the visit order. DFS uses a stack instead of a queue, along with a visited set and visit-order list. The stack explores one path before moving to another. These structures prevent cycles from causing an endless search and help record the traversal.

## 4. Average times for different graph sizes
I use the same starting node for each graph and average five runs. Fill in the table using the program's output for each provided graph. Times depend on the computer, so I have not filled in made-up measurements.

*** The graph files and starting nodes for these experiments have not yet been specified. I will complete the tables once the required inputs are provided and the runtime measurements have been collected. ***

For an adjacency list, BFS and DFS are both O(n + m), because each reachable node and edge is examined a limited number of times. The measured times should generally increase as the graphs get larger, but small timing differences may be hidden by measurement overhead and other processes running on the computer. Uniform-cost search is O((n + m) log n) with a binary heap.

## 5. Effect of the starting node
Run the selected large graph several times for each starting node specified by the instructor, keeping the graph and number of repetitions the same. Record the average times below.

*** The graph files and starting nodes for these experiments have not yet been specified. I will complete the tables once the required inputs are provided and the runtime measurements have been collected. ***

For a connected graph, all three algorithms eventually visit every node, so the overall runtime should usually be similar across starting nodes. The exact order of visits can change, and small runtime differences are expected. In a disconnected graph, the starting node can affect how many nodes are reached, which can make a bigger difference.

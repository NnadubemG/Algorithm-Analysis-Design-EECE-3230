# Graph Search Assignment

## Files
- `main.py`: reads a graph and runs BFS, DFS, and uniform-cost search.
- `g1.txt`: the eight-node example graph from the assignment.
- `section4_answers.md`: brief written answers and a table for experiment results.

## Requirements
Python 3. No extra packages are needed.

## Run
Open a terminal in this directory and run:

```bash
python main.py
```

When prompted, enter `g1.txt` (or the path to another graph file), then enter a starting node. The program reports the node and edge counts, visit order, number of nodes reached, and average runtime from five runs.

Graph files start with the number of nodes. Each later line contains the two endpoints of one undirected edge. Nodes are numbered from `0` to `n - 1`.

## Notes
The program uses an adjacency list. Runtime measurements are small and noisy for small graphs, so run the same graph several times if you want a more stable comparison. Use the same starting node when comparing graph sizes, and the same large graph with different starts for the final experiment.

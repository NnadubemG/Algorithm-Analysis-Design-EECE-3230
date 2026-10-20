from collections import deque
from time import perf_counter
import heapq


def load_graph(filename):
    """Read an undirected graph from a file: node count, then edge pairs."""
    with open(filename, "r", encoding="utf-8") as file:
        values = [line.strip() for line in file if line.strip()]

    if not values:
        raise ValueError("The graph file is empty.")

    n = int(values[0])
    if n < 0:
        raise ValueError("The number of nodes cannot be negative.")

    graph = [[] for _ in range(n)]
    edges = set()

    for line in values[1:]:
        parts = line.split()
        if len(parts) != 2:
            raise ValueError(f"Invalid edge line: {line}")

        u, v = map(int, parts)
        if not (0 <= u < n and 0 <= v < n):
            raise ValueError(f"Edge ({u}, {v}) contains an invalid node.")
        if u == v:
            # Self-loops are supported, but only counted once.
            graph[u].append(v)
            edges.add((u, v))
        else:
            graph[u].append(v)
            graph[v].append(u)
            edges.add(tuple(sorted((u, v))))

    # Make results predictable when several neighbors are available.
    for neighbors in graph:
        neighbors.sort()

    return graph, len(edges)


def bfs(graph, start):
    """Breadth-first traversal using a queue."""
    visited = {start}
    order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dfs(graph, start):
    """Depth-first traversal using an explicit stack."""
    visited = set()
    order = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)

        # Reverse so smaller-numbered neighbors are visited first.
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return order


def uniform_cost_search(graph, start):
    """Uniform-cost search; each edge has cost 1."""
    distances = {start: 0}
    visited = set()
    order = []
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        order.append(node)

        for neighbor in graph[node]:
            new_cost = cost + 1
            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    return order


def benchmark(search_function, graph, start, repeats=5):
    """Return the average runtime and the final traversal order."""
    durations = []
    order = []

    for _ in range(repeats):
        begin = perf_counter()
        order = search_function(graph, start)
        durations.append(perf_counter() - begin)

    return sum(durations) / len(durations), order


def main():
    filename = input("Enter graph file name (for example, g1.txt): ").strip()

    try:
        graph, edge_count = load_graph(filename)
    except (OSError, ValueError) as error:
        print(f"Could not read graph: {error}")
        return

    n = len(graph)
    print(f"\nNodes: {n}")
    print(f"Edges: {edge_count}")

    if n == 0:
        print("The graph has no nodes to search.")
        return

    try:
        start = int(input(f"Enter starting node (0 to {n - 1}): "))
        if not 0 <= start < n:
            raise ValueError
    except ValueError:
        print("Please enter a valid node number.")
        return

    algorithms = [
        ("BFS", bfs),
        ("DFS", dfs),
        ("Uniform-Cost Search", uniform_cost_search),
    ]

    print("\nEach runtime is the average of 5 runs.")
    for name, algorithm in algorithms:
        average, order = benchmark(algorithm, graph, start)
        print(f"\n{name}")
        print(f"Visit order: {order}")
        print(f"Average runtime: {average:.9f} seconds")
        print(f"Nodes reached: {len(order)} of {n}")


if __name__ == "__main__":
    main()

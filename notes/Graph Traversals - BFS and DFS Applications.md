[!definition]
Breadth-First Search (BFS): Traverses graphs level-by-level using a Queue (FIFO). Guaranteed to find the minimum-hop shortest path in unweighted graphs.
Depth-First Search (DFS): Traverses as deep as possible along each branch before backtracking, utilizing a Stack / Recursion (LIFO).
[!theorem]
Complexity Invariants:
With Adjacency List: Time $= O(V + E)$, Space $= O(V)$.
With Adjacency Matrix: Time $= O(V^2)$, Space $= O(V)$.
A BFS traversal tree on any connected graph of $V$ vertices contains exactly $V - 1$ edges.

Algorithmic Application
BFS Suitable
DFS Suitable
Shortest Path (Unweighted)
Optimal ($O(V + E)$)
Unsuitable (Not guaranteed)
Connected Components
Yes
Yes
Cycle Detection (Undirected)
Yes (Cross edge to visited non-parent)
Yes (Back edge)
Topological Sorting
Kahn's Algorithm (in-degree array)
Yes (Reverse of finishing times)
Bipartite Graph Testing
Yes (No odd-length cycle)
Yes
Bridges & Articulation Points
No
Yes (Tarjan's Discovery/Low time)

[!trap] BFS Order Uniqueness: BFS does NOT always yield a unique traversal sequence. The order depends entirely on the tie-breaking order of adjacent vertices pushed into the queue.
[!question] PSU CBT Practice Drill: Starting from vertex $R$, if adjacent vertices are visited in alphabetical order, find the BFS traversal sequence for the undirected graph containing vertices $R, S, T, U, V, W, X, Y$ with edges $(R, S), (R, V), (S, W), (W, T), (W, X), (T, U), (T, X), (X, Y), (U, Y)$: (A) R, S, V, W, T, X, U, Y
(B) R, V, S, W, X, T, Y, U
(C) R, S, W, V, T, X, U, Y
(D) R, S, V, W, X, T, U, Y
Step-by-Step Resolution:
Start at vertex $R$ (Level 0): Visited = $\{R\}$, Queue = [R].
Dequeue $R$: Neighbors of $R$ are $S, V$.
Alphabetical order: Enqueue $S$, then $V$.
Traversal: $R, S, V$. Queue = [S, V].
Dequeue $S$: Neighbors are $R$ (visited), $W$ (unvisited).
Enqueue $W$. Traversal: $R, S, V, W$. Queue = [V, W].
Dequeue $V$: Neighbor is $R$ (visited). No new nodes enqueued. Queue = [W].
Dequeue $W$: Neighbors are $S$ (visited), $T, X$ (unvisited).
Alphabetical order: Enqueue $T$, then $X$.
Traversal: $R, S, V, W, T, X$. Queue = [T, X].
Dequeue $T$: Neighbors are $W$ (visited), $X$ (already in queue), $U$ (unvisited).
Enqueue $U$. Traversal: $R, S, V, W, T, X, U$. Queue = [X, U].
Dequeue $X$: Neighbors are $W, T$ (visited), $Y$ (unvisited).
Enqueue $Y$. Traversal: $R, S, V, W, T, X, U, Y$.
Remaining queue nodes ($U, Y$) have no unvisited neighbors.
Correct Answer: (A) R, S, V, W, T, X, U, Y

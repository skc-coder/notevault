# Comprehensive Time Complexity Guide: Paradigms, Algorithms & Full Derivations

---

## 1. Divide and Conquer

Divide and conquer works by breaking a problem into independent subproblems of the same type, recursively solving them, and combining the results. Most recurrence relations take the form:
$$T(n) = a T(n/b) + f(n)$$
where $a \ge 1$ is the number of subproblems, $b > 1$ is the problem size division factor, and $f(n)$ is the cost of division and combination.

### 1.1 Binary Search
* **Best Case:** $\mathcal{O}(1)$
* **Average Case:** $\Theta(\log n)$
* **Worst Case:** $\Theta(\log n)$
* **Space Complexity:** $\mathcal{O}(1)$ (Iterative), $\mathcal{O}(\log n)$ (Recursive stack)
* **Explanation & Derivation:**
  The algorithm compares the target element with the middle element of a sorted array. At each step, half of the search space is discarded.
  $$T(n) = T(n/2) + \mathcal{O}(1)$$
  Applying the Master Theorem ($a = 1, b = 2, f(n) = 1$):
  $$n^{\log_b a} = n^{\log_2 1} = n^0 = 1$$
  Since $f(n) = \Theta(n^{\log_b a})$, this is Case 2: $T(n) = \Theta(n^{\log_b a} \log n) = \Theta(\log n)$.

---

### 1.2 Merge Sort
* **Best Case:** $\Theta(n \log n)$
* **Average Case:** $\Theta(n \log n)$
* **Worst Case:** $\Theta(n \log n)$
* **Space Complexity:** $\mathcal{O}(n)$ (standard array-based), $\mathcal{O}(1)$ (linked list)
* **Explanation & Derivation:**
  The array is recursively split into two equal halves until subarrays of size 1 remain ($2T(n/2)$). Merging two sorted subarrays of total size $n$ takes linear time $\mathcal{O}(n)$.
  $$T(n) = 2T(n/2) + \Theta(n)$$
  By Master Theorem ($a = 2, b = 2, f(n) = n$):
  $$n^{\log_2 2} = n^1$$
  Since $f(n) = \Theta(n^1)$, this is Case 2: $T(n) = \Theta(n \log n)$. The merge step always takes linear work regardless of the initial order of elements, making best, average, and worst cases identical in time.

---

### 1.3 Quick Sort & Quickselect
* **Quick Sort Time:**
  * Best Case: $\Theta(n \log n)$ (Balanced partitioning around median)
  * Average Case: $\Theta(n \log n)$
  * Worst Case: $\Theta(n^2)$ (Unbalanced partitioning, e.g., already sorted array with end pivot)
* **Quickselect Time:**
  * Average Case: $\Theta(n)$
  * Worst Case: $\Theta(n^2)$
* **Explanation & Derivation:**
  * **Quick Sort Best Case:** $T(n) = 2T(n/2) + \Theta(n) \implies \Theta(n \log n)$.
  * **Quick Sort Worst Case:** If the pivot is always the extreme element, one partition has size $0$ and the other has size $n-1$:
    $$T(n) = T(n-1) + \Theta(n) = \sum_{k=1}^n k = \frac{n(n+1)}{2} = \Theta(n^2)$$
  * **Quickselect Average Case:** Unlike Quick Sort, it recurses only into **one** half:
    $$T(n) = T(n/2) + \Theta(n)$$
    Applying Master Theorem ($a = 1, b = 2, f(n) = n$):
    $$n^{\log_2 1} = n^0 = 1$$
    Since $f(n) = n = \Omega(n^{0 + \epsilon})$ for $\epsilon = 1$, and $a \cdot f(n/b) = n/2 \le c \cdot n$ for $c = 1/2 < 1$, this is Case 3: $T(n) = \Theta(n)$.

---

### 1.4 Karatsuba Fast Multiplication
* **Time Complexity:** $\mathcal{O}(n^{\log_2 3}) \approx \mathcal{O}(n^{1.585})$
* **Conventional Multiplication:** $\mathcal{O}(n^2)$
* **Explanation & Derivation:**
  Multiplying two $n$-digit numbers traditionally requires 4 sub-multiplications of size $n/2$. Karatsuba reduces this to 3 multiplications using the algebraic trick:
  $$xy = 2^{2m} x_1 y_1 + 2^m ((x_1 + x_0)(y_1 + y_0) - x_1 y_1 - x_0 y_0) + x_0 y_0$$
  Recurrence:
  $$T(n) = 3T(n/2) + \mathcal{O}(n)$$
  Applying Master Theorem ($a = 3, b = 2$):
  $$n^{\log_2 3} \approx n^{1.585}$$
  Since $f(n) = n = \mathcal{O}(n^{\log_2 3 - \epsilon})$, Case 1 yields $T(n) = \Theta(n^{\log_2 3})$.

---

### 1.5 Strassen’s Matrix Multiplication
* **Time Complexity:** $\mathcal{O}(n^{\log_2 7}) \approx \mathcal{O}(n^{2.807})$
* **Conventional Matrix Multiplication:** $\mathcal{O}(n^3)$
* **Explanation & Derivation:**
  Multiplying two $n \times n$ matrices typically requires 8 sub-matrix multiplications of dimension $n/2 \times n/2$. Strassen reduced this from 8 multiplications to 7 through 10 matrix additions and subtractions.
  $$T(n) = 7T(n/2) + \mathcal{O}(n^2)$$
  Applying Master Theorem ($a = 7, b = 2$):
  $$n^{\log_2 7} \approx n^{2.807}$$
  Since $f(n) = n^2 = \mathcal{O}(n^{\log_2 7 - \epsilon})$, Case 1 yields $T(n) = \Theta(n^{2.807})$.

---

## 2. Greedy Algorithms

Greedy algorithms construct solutions piece-by-piece, picking the locally optimal choice at each step without ever backtracking. Correctness requires two properties:
1. **Greedy-Choice Property:** A globally optimal solution can be reached by making locally optimal decisions.
2. **Optimal Substructure:** An optimal solution to the problem contains within it optimal solutions to subproblems.

### 2.1 Fractional Knapsack
* **Time Complexity:** $\mathcal{O}(n \log n)$
* **Space Complexity:** $\mathcal{O}(1)$ (excluding sort buffer)
* **Explanation & Derivation:**
  Each item $i$ has weight $w_i$ and value $v_i$. The algorithm computes the value density ratio $r_i = \frac{v_i}{w_i}$.
  * Calculating all ratios: $\mathcal{O}(n)$.
  * Sorting items in descending order of ratio: $\mathcal{O}(n \log n)$.
  * Greedily selecting full items and taking a fraction of the last fitting item: $\mathcal{O}(n)$.
  * Total time is dominated by the sorting stage: $\mathcal{O}(n \log n)$. (If selection uses a linear median-of-medians partition, it can be brought down to $\mathcal{O}(n)$).

---

### 2.2 Activity Selection / Interval Scheduling
* **Time Complexity:** $\mathcal{O}(n \log n)$
* **Space Complexity:** $\mathcal{O}(1)$
* **Explanation & Derivation:**
  To select the maximum number of mutually compatible intervals, intervals are sorted by their **finish time** $f_i$ in ascending order.
  * Sorting intervals by finish time: $\mathcal{O}(n \log n)$.
  * Linear sweep comparing the next activity's start time $s_{i}$ with the current active activity's finish time $f_{\text{last}}$: $\mathcal{O}(n)$.
  * Dominant cost: $\mathcal{O}(n \log n)$. If inputs are already pre-sorted by finish time, it runs in $\mathcal{O}(n)$.

---

### 2.3 Huffman Coding
* **Time Complexity:** $\mathcal{O}(n \log n)$
* **Space Complexity:** $\mathcal{O}(n)$
* **Explanation & Derivation:**
  Given an alphabet of $n$ symbols with given frequencies, construct an optimal prefix code tree:
  1. Insert all $n$ symbol frequencies into a min-priority queue: $\mathcal{O}(n)$ using `buildHeap`.
  2. For $n - 1$ steps, extract the two smallest frequency nodes ($2 \times \mathcal{O}(\log n)$), merge them into a parent node, and re-insert the parent ($\mathcal{O}(\log n)$).
  3. Total loop cost $= (n - 1) \times 3 \log n = \mathcal{O}(n \log n)$.
  4. If character frequencies are pre-sorted, using two FIFO queues yields $\mathcal{O}(n)$ total time.

---

### 2.4 Minimum Spanning Tree: Kruskal’s Algorithm
* **Time Complexity:** $\mathcal{O}(E \log E) = \mathcal{O}(E \log V)$
* **Space Complexity:** $\mathcal{O}(V + E)$
* **Explanation & Derivation:**
  1. Sort all $E$ edges in non-decreasing order of weight: $\mathcal{O}(E \log E)$.
     Since $E \le V^2$, $\log E \le 2 \log V$, meaning $\mathcal{O}(E \log E) = \mathcal{O}(E \log V)$.
  2. Iterate through sorted edges, checking if endpoints belong to the same component using a Disjoint Set Union (DSU) data structure with Path Compression and Union by Rank.
  3. Running $2E$ `find` and $V - 1$ `union` operations takes $\mathcal{O}(E \cdot \alpha(V))$ time, where $\alpha$ is the nearly-constant Inverse Ackermann function.
  4. Total time is dominated by edge sorting: $\mathcal{O}(E \log V)$.

---

### 2.5 Minimum Spanning Tree: Prim’s Algorithm
* **Time Complexity:**
  * With Adjacency Matrix: $\mathcal{O}(V^2)$
  * With Binary Min-Heap: $\mathcal{O}((V + E) \log V) = \mathcal{O}(E \log V)$
  * With Fibonacci Heap: $\mathcal{O}(E + V \log V)$
* **Space Complexity:** $\mathcal{O}(V + E)$
* **Explanation & Derivation:**
  The algorithm grows a single tree starting from an arbitrary vertex:
  * Extract-min is called $V$ times. On a binary heap: $V \cdot \mathcal{O}(\log V)$.
  * Decrease-key is called at most once for every edge traversed ($E$ times). On a binary heap: $E \cdot \mathcal{O}(\log V)$.
  * Total binary heap time: $\mathcal{O}(V \log V + E \log V) = \mathcal{O}(E \log V)$.
  * In a Fibonacci heap, `decreaseKey` runs in $\mathcal{O}(1)$ amortized time, giving $V \log V + E(1) = \mathcal{O}(E + V \log V)$.

---

### 2.6 Single-Source Shortest Path: Dijkstra’s Algorithm
* **Time Complexity:**
  * With Adjacency Matrix: $\mathcal{O}(V^2)$
  * With Binary Min-Heap: $\mathcal{O}((V + E) \log V)$
  * With Fibonacci Heap: $\mathcal{O}(E + V \log V)$
* **Space Complexity:** $\mathcal{O}(V)$
* **Explanation & Derivation:**
  Identical operational profile to Prim's algorithm. It extracts the vertex with minimum tentative distance from the queue ($V$ times) and relaxes outgoing edges, issuing up to $E$ decrease-key updates.
  * **Array implementation:** Finding minimum takes $\mathcal{O}(V)$ across $V$ vertices $\implies \mathcal{O}(V^2)$. Edge updates take $\mathcal{O}(1) \implies \mathcal{O}(E)$. Total: $\mathcal{O}(V^2 + E) = \mathcal{O}(V^2)$. Optimal for dense graphs where $E = \Theta(V^2)$.
  * **Binary Min-Heap:** $V$ extractions take $\mathcal{O}(V \log V)$, and $E$ edge relaxations take $\mathcal{O}(E \log V)$, yielding $\mathcal{O}(E \log V)$. Optimal for sparse graphs where $E \ll V^2$.

---

## 3. Dynamic Programming

Dynamic programming solves optimization problems by breaking them into overlapping subproblems, computing solutions to smaller subproblems once, and storing them in a table (memoization or tabulation).

$$\text{Time Complexity} = (\text{Total Number of Subproblems}) \times (\text{Time Spent per Subproblem})$$

### 3.1 0/1 Knapsack Problem
* **Time Complexity:** $\mathcal{O}(n \cdot W)$ (Pseudo-polynomial)
* **Space Complexity:** $\mathcal{O}(n \cdot W)$ (Standard), reducible to $\mathcal{O}(W)$ (1D array)
* **Explanation & Derivation:**
  Let $DP[i][w]$ represent the maximum value attainable using a subset of the first $i$ items with capacity limit $w$:
  $$DP[i][w] = \max(DP[i-1][w], \; DP[i-1][w - w_i] + v_i)$$
  * Total unique states: $(n + 1) \times (W + 1) = \Theta(n \cdot W)$ cells.
  * Transition cost per cell: $\mathcal{O}(1)$ (one comparison and addition).
  * Total time: $\mathcal{O}(n \cdot W)$.
  * **Why Pseudo-Polynomial:** The input size of capacity $W$ is proportional to the number of bits $\log_2 W$. With respect to input bit-length $L$, the complexity is $\mathcal{O}(n \cdot 2^L)$, which is exponential.

---

### 3.2 Longest Common Subsequence (LCS)
* **Time Complexity:** $\mathcal{O}(m \cdot n)$
* **Space Complexity:** $\mathcal{O}(m \cdot n)$ (Standard), reducible to $\mathcal{O}(\min(m, n))$
* **Explanation & Derivation:**
  For strings $X$ of length $m$ and $Y$ of length $n$, the state $DP[i][j]$ denotes the LCS length of prefixes $X[1..i]$ and $Y[1..j]$:
  $$DP[i][j] = \begin{cases}    DP[i-1][j-1] + 1 & \text{if } X[i] = Y[j] \\    \max(DP[i-1][j], DP[i][j-1]) & \text{if } X[i] \ne Y[j]    \end{cases}$$
  * Total states: $(m + 1)(n + 1) = \Theta(m \cdot n)$.
  * Transition cost: $\mathcal{O}(1)$.
  * Total time: $\Theta(m \cdot n)$.

---

### 3.3 Matrix Chain Multiplication (MCM)
* **Time Complexity:** $\mathcal{O}(n^3)$
* **Space Complexity:** $\mathcal{O}(n^2)$
* **Explanation & Derivation:**
  Given a sequence of $n$ matrices $\langle A_1, A_2, \dots, A_n \rangle$ where matrix $A_i$ has dimension $p_{i-1} \times p_i$. Let $m[i][j]$ be the minimum scalar multiplications needed to compute $A_i \dots A_j$:
  $$m[i][j] = \min_{i \le k < j} \left( m[i][k] + m[k+1][j] + p_{i-1} p_k p_j \right)$$
  * Number of subproblems (subchains of length $2$ to $n$): $\binom{n}{2} = \frac{n(n-1)}{2} = \Theta(n^2)$ states.
  * Work per subproblem: For a chain of length $L = j - i + 1$, the index $k$ can take $L - 1$ distinct split positions.
  * Total operations:
    $$\sum_{L=2}^n (n - L + 1)(L - 1) = \Theta(n^3)$$

---

### 3.4 Bellman-Ford Algorithm (Single-Source Shortest Paths)
* **Time Complexity:** $\mathcal{O}(V \cdot E)$
* **Space Complexity:** $\mathcal{O}(V)$
* **Explanation & Derivation:**
  Let $dist^{(k)}[v]$ be the length of the shortest path from source $s$ to $v$ containing at most $k$ edges:
  $$dist^{(k)}[v] = \min \left( dist^{(k-1)}[v], \; \min_{(u, v) \in E} (dist^{(k-1)}[u] + w(u, v)) \right)$$
  * Any simple path has at most $V - 1$ edges.
  * The outer loop executes $V - 1$ passes. In each pass, all $E$ edges are relaxed.
  * Total time: $(V - 1) \times \mathcal{O}(E) = \mathcal{O}(V \cdot E)$.
  * For dense graphs where $E = \Theta(V^2)$, Bellman-Ford takes $\mathcal{O}(V^3)$.

---

### 3.5 Floyd-Warshall Algorithm (All-Pairs Shortest Paths)
* **Time Complexity:** $\Theta(V^3)$
* **Space Complexity:** $\Theta(V^2)$
* **Explanation & Derivation:**
  Computes shortest paths between all pairs of vertices in a directed graph with positive or negative weights (no negative cycles). Let $D^{(k)}[i][j]$ be the shortest path from $i$ to $j$ using intermediate vertices only from $\{1, \dots, k\}$:
  $$D^{(k)}[i][j] = \min\left(D^{(k-1)}[i][j], \; D^{(k-1)}[i][k] + D^{(k-1)}[k][j]\right)$$
  * Structure consists of three nested loops running from $1$ to $V$:
    ```c
    for (int k = 1; k <= V; k++)
        for (int i = 1; i <= V; i++)
            for (int j = 1; j <= V; j++)
                D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
    ```
  * Each update inside the innermost loop takes $\mathcal{O}(1)$ time.
  * Total execution time: $V \times V \times V = \Theta(V^3)$.

---

### 3.6 Longest Increasing Subsequence (LIS)
* **Standard Dynamic Programming:** $\mathcal{O}(n^2)$ time, $\mathcal{O}(n)$ space.
  * $DP[i] = 1 + \max(\{DP[j] \mid 0 \le j < i \text{ and } A[j] < A[i]\} \cup \{0\})$.
  * Evaluating each of the $n$ entries requires scanning up to $i$ previous entries $\implies \sum_{i=1}^n i = \Theta(n^2)$.
* **Patience Sorting + Binary Search:** $\mathcal{O}(n \log n)$ time, $\mathcal{O}(n)$ space.
  * Maintains an array `tail` where `tail[len]` stores the smallest tail of all increasing subsequences of length `len` found so far.
  * For each of the $n$ elements, use binary search to find its position in `tail`: $\mathcal{O}(\log n)$.
  * Total time: $n \times \mathcal{O}(\log n) = \mathcal{O}(n \log n)$.

---

## 4. Master Comparison Table

| Paradigm | Algorithm | Best Case | Average Case | Worst Case | Auxiliary Space |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Divide & Conquer** | Binary Search | $\mathcal{O}(1)$ | $\Theta(\log n)$ | $\Theta(\log n)$ | $\mathcal{O}(1)$ |
| **Divide & Conquer** | Merge Sort | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\mathcal{O}(n)$ |
| **Divide & Conquer** | Quick Sort | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n^2)$ | $\mathcal{O}(\log n)$ / $\mathcal{O}(n)$ |
| **Divide & Conquer** | Quickselect | $\Theta(n)$ | $\Theta(n)$ | $\Theta(n^2)$ | $\mathcal{O}(\log n)$ / $\mathcal{O}(n)$ |
| **Divide & Conquer** | Karatsuba Multiplication | $\Theta(n^{1.585})$ | $\Theta(n^{1.585})$ | $\Theta(n^{1.585})$ | $\mathcal{O}(n)$ |
| **Divide & Conquer** | Strassen Matrix Multiplication | $\Theta(n^{2.807})$ | $\Theta(n^{2.807})$ | $\Theta(n^{2.807})$ | $\mathcal{O}(n^2)$ |
| **Greedy** | Fractional Knapsack | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(1)$ |
| **Greedy** | Activity Selection | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(1)$ |
| **Greedy** | Huffman Coding | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ |
| **Greedy** | Kruskal's MST | $\mathcal{O}(E \log V)$ | $\mathcal{O}(E \log V)$ | $\mathcal{O}(E \log V)$ | $\mathcal{O}(V + E)$ |
| **Greedy** | Prim's MST (Binary Heap) | $\mathcal{O}(E \log V)$ | $\mathcal{O}(E \log V)$ | $\mathcal{O}(E \log V)$ | $\mathcal{O}(V)$ |
| **Greedy** | Dijkstra's SSSP (Binary Heap) | $\mathcal{O}(E \log V)$ | $\mathcal{O}(E \log V)$ | $\mathcal{O}(E \log V)$ | $\mathcal{O}(V)$ |
| **Dynamic Programming**| 0/1 Knapsack | $\Theta(n \cdot W)$ | $\Theta(n \cdot W)$ | $\Theta(n \cdot W)$ | $\mathcal{O}(W)$ |
| **Dynamic Programming**| Longest Common Subsequence | $\Theta(m \cdot n)$ | $\Theta(m \cdot n)$ | $\Theta(m \cdot n)$ | $\mathcal{O}(\min(m, n))$ |
| **Dynamic Programming**| Matrix Chain Multiplication | $\Theta(n^3)$ | $\Theta(n^3)$ | $\Theta(n^3)$ | $\mathcal{O}(n^2)$ |
| **Dynamic Programming**| Bellman-Ford SSSP | $\mathcal{O}(E)$ (Optimized) | $\mathcal{O}(V \cdot E)$ | $\mathcal{O}(V \cdot E)$ | $\mathcal{O}(V)$ |
| **Dynamic Programming**| Floyd-Warshall APSP | $\Theta(V^3)$ | $\Theta(V^3)$ | $\Theta(V^3)$ | $\Theta(V^2)$ |
| **Dynamic Programming**| LIS (Binary Search variant) | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\mathcal{O}(n)$ |
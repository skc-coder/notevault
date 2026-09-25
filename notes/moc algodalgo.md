[[time complexirty quiz]]
[[sorting algorithmss quiz]]

![[attachments 1/moc algodalgo-1790160313113.webp]]


![](attachments%201/moc%20algodalgo-1790158160830.webp)
![[attachments 1/moc algodalgo-1790158380087.webp]]



| Problem | Recurrence Core | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Climbing Stairs** | $T(n) = T(n-1) + T(n-2)$ | $O(n)$ | $O(1)$ |
| **LCS** | Match: $+1$ diag; Mismatch: $\max(\text{up}, \text{left})$ | $O(m \cdot n)$ | $O(m \cdot n)$ or $O(\min(m, n))$ |
| **MCM** | $\min_k [m[i,k] + m[k+1,j] + d_{i-1}d_kd_j]$ | $O(n^3)$ | $O(n^2)$ |
| **0/1 Knapsack** | $\max(\text{exclude}, \text{include if } w_i \le w)$ | $O(n \cdot W)$ | $O(n \cdot W)$ or $O(W)$ |
| **SCS Length** | $m + n - \text{LCS}(X, Y)$ | $O(m \cdot n)$ | $O(\min(m, n))$ |
| **MCM Bracketings** | Catalan number $C_{n-1} = \frac{1}{n} \binom{2n-2}{n-1}$ | — | — |



| Problem                 | Sorting Criterion                  | Complexity                               | Key Property / Invariant                      |
| :---------------------- | :--------------------------------- | :--------------------------------------- | :-------------------------------------------- |
| **Huffman Coding**      | Min frequency first (Min-Heap)     | $O(n \log n)$                            | Strictly full binary tree ($2n - 1$ nodes)    |
| **Optimal Merge**       | Smallest file sizes first          | $O(n \log n)$                            | Total cost $= \sum (\text{internal nodes})$   |
| **Activity Selection**  | Earliest **Finish Time** ($f_i$)   | $O(n \log n)$                            | Maximizes remaining time availability         |
| **Job Sequencing**      | Decreasing **Profit** ($p_i$)      | $O(n \cdot d)$ or $O(n \log n)$ with DSU | Place at latest valid empty slot $t \le d_i$  |
| **Fractional Knapsack** | Decreasing **Ratio** ($v_i / w_i$) | $O(n \log n)$ or $O(n)$ with selection   | Optimal Substructure + Greedy Choice Property |



---

## 1. Fundamentals & Core Properties (29a–29b)

* **Total Spanning Trees in a Complete Graph ($K_n$)**:
  $$\text{Number of Spanning Trees} = n^{n-2} \quad \text{(Cayley's Formula)}$$

### Cut Property & Cycle Property (Very Common in PSU True/False Qs)
* **Cut Property**: For any cut $(S, V \setminus S)$ in graph $G$, if an edge $e$ crossing the cut has **strictly minimum weight**, that edge **must belong to every MST**.
  * If weights are not distinct and there are multiple minimum-weight crossing edges, at least one of them belongs to an MST.
* **Cycle Property**: For any cycle $C$ in graph $G$, the edge with the **strictly maximum weight** in $C$ **cannot belong to any MST**.
* **Uniqueness Theorem**:
  * If **all edge weights are distinct**, the graph has a **unique MST**.
  * The converse is **false**: Distinct MST does *not* imply all edge weights are distinct.
* **Negative Edge Weights**:
  * MST algorithms (both Kruskal's and Prim's) work perfectly with **negative edge weights** (unlike Dijkstra's).
  * Adding a constant $c$ to every edge weight does **not** change the structure of the MST (it just increases total MST weight by $(V-1) \cdot c$).
  * Squaring/multiplying edge weights by a positive constant preserves the MST.

---

## 2. Kruskal's Algorithm (29c)

### Mechanics
* **Edge-centric approach**:
  1. Sort all $E$ edges in non-decreasing order of weights: $w(e_1) \le w(e_2) \le \dots \le w(e_E)$.
  2. Pick the smallest edge. If it forms a cycle with edges picked so far, discard it; otherwise, include it in the MST.
  3. Stop when $V - 1$ edges are added.
* **Cycle Detection Data Structure**: **Disjoint Set Union (DSU / Union-Find)** with path compression and union by rank/size.

### Time & Space Complexity
* **Sorting edges**: $O(E \log E) = O(E \log V)$ (since $E \le V^2 \implies \log E = O(\log V)$).
* **DSU operations**: $2E$ find operations and $V-1$ union operations take $O(E \cdot \alpha(V))$, where $\alpha$ is the Inverse Ackermann function (effectively $O(1)$).
* **Total Time Complexity**:
  * Using standard comparison sort: $O(E \log E) \equiv O(E \log V)$.
  * If edges are **pre-sorted** or sorted in $O(E)$ via counting sort (small integer weights): $O(E \cdot \alpha(V)) \approx O(E)$.
* **Space Complexity**: $O(V + E)$ for edges and parent/rank arrays.
* **Best suited for**: **Sparse graphs** ($E \ll V^2$).

---

## 3. Prim's Algorithm (30a–30b)

### Mechanics
* **Vertex-centric / Growing Tree approach**:
  1. Start with an arbitrary root vertex $r$; set its key to $0$ and all other vertices' keys to $\infty$.
  2. Maintain a Priority Queue (Min-Heap) of vertices not yet included in the tree.
  3. In each step, extract vertex $u$ with minimum key from the heap (adds $u$ to MST).
  4. For each neighbor $v$ of $u$, if $v$ is still in the heap and $w(u, v) < \text{key}[v]$, update $\text{key}[v] = w(u, v)$ (Decrease-Key operation).
  5. Repeat until all $V$ vertices are in the tree.

### Complexity Breakdown
| Implementation of Min-Heap | Extract-Min | Decrease-Key | Total Time Complexity | Best For |
| :--- | :--- | :--- | :--- | :--- |
| **Adjacency Matrix + Array** | $O(V)$ | $O(1)$ | $O(V^2)$ | **Dense graphs** ($E \approx V^2$) |
| **Binary Min-Heap + Adj List** | $O(\log V)$ | $O(\log V)$ | $O((V + E) \log V) \equiv O(E \log V)$ | **Sparse graphs** |
| **Fibonacci Heap + Adj List** | $O(\log V)$ amortized | $O(1)$ amortized | $O(E + V \log V)$ | Dense/large theoretical graphs |

---

| Query / Property                | Formula / Answer                                         |
| :------------------------------ | :------------------------------------------------------- |
| **Spanning Trees in $K_n$**     | $n^{n-2}$                                                |
| **Spanning Trees in $K_{m,n}$** | $m^{n-1} \cdot n^{m-1}$                                  |
| **Edges in any Spanning Tree**  | Exactly $V - 1$ edges                                    |
| **Kruskal's Complexity**        | $O(E \log V)$ (Sparse graph friendly)                    |
| **Prim's (Adj Matrix)**         | $O(V^2)$ (Dense graph friendly: $E = \Theta(V^2)$)       |
| **Prim's (Binary Heap)**        | $O(E \log V)$                                            |
| **Prim's (Fibonacci Heap)**     | $O(E + V \log V)$                                        |
| **Negative weights supported?** | **Yes** (Both Prim & Kruskal work with negative weights) |
| **All weights distinct?**       | Exactly **one unique MST** exists                        |
Every priority-queue graph algorithm (Prim’s and Dijkstra’s) runs in:

$$\text{Total Time} = V \times (\text{Extract-Min}) + E \times (\text{Decrease-Key})$$

Why?

- You extract each vertex from the heap **exactly once** $\implies V$ times.
    
- You inspect/relax edges across the whole run at most once per edge $\implies E$ times.

# High-Yield Shortest Path Algorithms Notes for PSU (IOCL) Exam

---

## 1. Dijkstra’s Algorithm (26a–27d)

### Core Objective & Paradigms
* **Single-Source Shortest Path (SSSP)** on directed or undirected graphs.
* **Paradigm**: **Greedy Strategy**.
* **Invariant**: Maintains a set $S$ of visited vertices whose final shortest path weights from source $s$ are already correctly determined. Once a vertex is extracted from the priority queue, its distance is **finalized** (never revisited in standard formulation).

### Edge Relaxation Formulation
For edge $(u, v)$ with weight $w(u, v)$:
$$\text{if } d[u] + w(u, v) < d[v] \implies d[v] = d[u] + w(u, v), \quad \pi[v] = u$$

### The Negative Weight / Negative Cycle Trap (PSU Favorite)
* **Dijkstra fails on graphs with negative weight edges**:
  * The greedy assumption breaks down: once a vertex is marked "visited", Dijkstra assumes no future path can reduce its distance. A subsequent negative edge can violate this.
  * **Does adding a constant $c$ to all edges fix Dijkstra for negative edges?**
    * **NO.** Paths with more edges get penalized more: if path $P_1$ has 3 edges and $P_2$ has 1 edge, $P_1$ increases by $3c$ while $P_2$ increases by only $c$, altering the shortest path.
* **Infinite Loops**: In the standard Dijkstra formulation (where each vertex is finalized once), it terminates in $O(E \log V)$ even with negative weights, but it gives **wrong answers**. If modified to re-insert relaxed nodes, a **negative weight cycle** causes an **infinite loop**.

### Complexity Recall Master Formula
$$\text{Total Time} = V \cdot T(\text{Extract-Min}) + E \cdot T(\text{Decrease-Key})$$

| Data Structure | Extract-Min ($V$ times) | Decrease-Key ($E$ times) | Total Time Complexity | Best For |
| :--- | :---: | :---: | :--- | :--- |
| **Unordered Array** | $O(V)$ | $O(1)$ | $O(V^2)$ | Dense graphs ($E \approx V^2$) |
| **Binary Min-Heap** | $O(\log V)$ | $O(\log V)$ | $O((V + E) \log V) \equiv O(E \log V)$ | Sparse graphs ($E \ll V^2$) |
| **Fibonacci Heap** | $O(\log V)$ amortized | $O(1)$ amortized | $O(E + V \log V)$ | Theoretical / Dense |

---

| Algorithm             | Problem | Edge Weights                | Time Complexity           |
| :-------------------- | :------ | :-------------------------- | :------------------------ |
| **Dijkstra**          | SSSP    | Non-negative only ($\ge 0$) | $O(E \log V)$ or $O(V^2)$ |
| **DAG Shortest Path** | SSSP    | Any (negative allowed)      | $\Theta(V + E)$           |
| **Bellman-Ford**      | SSSP    | Any (negative allowed)      | $O(V \cdot E)$            |
| **Floyd-Warshall**    | APSP    | Any (negative allowed)      | $\Theta(V^3)$             |




### Parenthesis Structure Theorem
For any two vertices $u$ and $v$, the intervals $[d[u], f[u]]$ and $[d[v], f[v]]$ are either **entirely disjoint** or **one is strictly nested inside the other**:
* **Nested**: $[d[v], f[v]] \subset [d[u], f[u]] \iff v$ is a descendant of $u$ in the DFS tree.
* **Disjoint**: Neither is a descendant of the other (cross-tree or parallel branches).

### Classification of Edges
When exploring edge $(u, v)$ during DFS:

| Edge Type | Directed Graph Condition | Undirected Graph? | Definition / Structural Role |
| :--- | :--- | :---: | :--- |
| **Tree Edge** | $(u, v)$ leads to a White vertex | **Yes** | Edges included in the DFS forest. |
| **Back Edge** | Leads to an **ancestor** (Gray vertex: $d[v] < d[u] < f[u] < f[v]$) | **Yes** | **Indicates presence of a cycle.** |
| **Forward Edge** | Leads to a **descendant** (Black vertex: $d[u] < d[v] < f[v] < f[u]$) | **No** | Non-tree shortcut down the DFS tree. |
| **Cross Edge** | Leads to another branch (Black vertex: $d[v] < f[v] < d[u] < f[u]$) | **No** | Connects unrelated subtrees/components. |

> **Critical PSU Rule**: In an **undirected graph**, every edge is **either a Tree Edge or a Back Edge**. Forward edges and Cross edges **never exist** in undirected DFS.


### BFS Edge Classification (Undirected Graph)
* In undirected BFS, every edge is either a:
  1. **Tree Edge**
  2. **Cross Edge** (connects vertices in the same layer or adjacent layers: $|level(u) - level(v)| \le 1$).
  * Back edges and Forward edges **never exist** in BFS.

### BFS Applications
1. **Shortest Cycle in an Undirected Graph**:
   * Run BFS from each vertex: $\Theta(V(V + E))$.
2. **Bipartite Graph Checking (2-Colorability)**:
   * A graph is bipartite $\iff$ it contains **no odd-length cycles**.
   * Run BFS and alternate colors (0 and 1) level-by-level. If an edge connects two vertices of the same color/level $\implies$ Not bipartite. Time: $O(V + E)$.
3. **Connected Components / Flood Fill**:
   * Standard BFS/DFS traversal counting disconnected trees in forest: $O(V + E)$.

---

## 5. IOCL Rapid-Fire Comparison Cheat Sheet

| Feature / Question               | BFS                                    | DFS                                        |
| :------------------------------- | :------------------------------------- | :----------------------------------------- |
| **Primary Data Structure**       | FIFO Queue                             | LIFO Stack (or recursion)                  |
| **Time Complexity (Adj List)**   | $O(V + E)$                             | $O(V + E)$                                 |
| **Time Complexity (Adj Matrix)** | $O(V^2)$                               | $O(V^2)$                                   |
| **Shortest Path (Unweighted)**   | **Optimal / Guarantees shortest path** | Does **not** guarantee shortest path       |
| **Cycle Detection (Directed)**   | Kahn's Algorithm (in-degree tracking)  | Back edge detection ($d[v] < d[u] < f[v]$) |
| **Topological Sort**             | Kahn's Algorithm                       | Decreasing order of finishing times $f[u]$ |
| **Undirected Edges Allowed**     | Tree Edges, Cross Edges                | Tree Edges, Back Edges                     |
| **Back Edge Implication**        | N/A                                    | **Guarantees a Cycle**                     |
| **Bipartite Verification**       | Odd-level conflict check               | 2-coloring conflict check                  |


| **Graph Type** | **Traversal** | **Possible Edge Types**                  | **Edges that NEVER Exist** |
| -------------- | ------------- | ---------------------------------------- | -------------------------- |
| **Directed**   | **DFS**       | **Tree, Back, Forward, Cross** _(All 4)_ | None                       |
| **Undirected** | **DFS**       | **Tree, Back**                           | **Forward, Cross**         |
| **Directed**   | **BFS**       | **Tree, Back, Cross**                    | **Forward**                |
| **Undirected** | **BFS**       | **Tree, Cross**                          | **Back, Forward**          |



# High-Yield Sorting Algorithms Notes for PSU (IOCL) Exam

---

## 1. Master Summary Matrix

| Algorithm          |   Best Time   | Average Time  |  Worst Time   |    Auxiliary Space    | Stable? | In-Place? |                     Comparisons (Worst)                     |         Swaps (Worst)         |
| :----------------- | :-----------: | :-----------: | :-----------: | :-------------------: | :-----: | :-------: | :---------------------------------------------------------: | :---------------------------: |
| **Bubble Sort**    |    $O(n)$     |   $O(n^2)$    |   $O(n^2)$    |        $O(1)$         | **Yes** |  **Yes**  |                     $\frac{n(n-1)}{2}$                      |      $\frac{n(n-1)}{2}$       |
| **Selection Sort** |   $O(n^2)$    |   $O(n^2)$    |   $O(n^2)$    |        $O(1)$         | **No**  |  **Yes**  |                     $\frac{n(n-1)}{2}$                      |     $n - 1$ *(Min Swaps)*     |
| **Insertion Sort** |    $O(n)$     |   $O(n^2)$    |   $O(n^2)$    |        $O(1)$         | **Yes** |  **Yes**  |                     $\frac{n(n-1)}{2}$                      | $\frac{n(n-1)}{2}$ *(shifts)* |
| **Merge Sort**     | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ |        $O(n)$         | **Yes** |  **No**   | $n \lceil \log_2 n \rceil - 2^{\lceil \log_2 n \rceil} + 1$ |        0 (data copied)        |
| **Quick Sort**     | $O(n \log n)$ | $O(n \log n)$ |   $O(n^2)$    | $O(\log n)$ to $O(n)$ | **No**  |  **Yes**  |                     $\frac{n(n-1)}{2}$                      |            $O(n)$             |
| **Heap Sort**      | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ |        $O(1)$         | **No**  |  **Yes**  |                     $2n \log n + O(n)$                      |          $n \log n$           |
|                    |               |               |               |                       |         |           |                                                             |                               |

* **Adaptive**: Runs faster if the input array is already partially or completely sorted.
* **Stable**: Maintains the relative order of duplicate elements.
* **In-Place**: Uses $O(1)$ (or $O(\log n)$ call-stack) auxiliary memory.

---

## 2. Bubble Sort

* **Comparisons (Total across all passes)**:
  $$\sum_{i=1}^{n-1} (n - i) = \frac{n(n - 1)}{2} \quad \text{(Invariant for unoptimized version)}$$
* **Swaps (Inversions)**:
  * **Best Case**: $0$ (Already sorted).
  * **Worst Case** (Reverse sorted): $\frac{n(n - 1)}{2}$.
  * Number of swaps equals the number of **inversions** in the input array.
* **Optimization**: Use a boolean `swapped` flag. If no swaps occur in a pass, break early $\implies$ **Best-case time becomes $O(n)$ with $n - 1$ comparisons**.

---

## 3. Selection Sort
Stick method
### Working Mechanism
Divides the array into a sorted sublist (left) and an unsorted sublist (right). In each iteration, it finds the absolute minimum element from the unsorted sublist and swaps it with the first unsorted element.

### Worked Example: `[29, 10, 14, 37, 13]`
1. Min of `[29, 10, 14, 37, 13]` is `10` $\to$ Swap with index 0: `[10 | 29, 14, 37, 13]`
2. Min of `[29, 14, 37, 13]` is `13` $\to$ Swap with index 1: `[10, 13 | 14, 37, 29]`
3. Min of `[14, 37, 29]` is `14` $\to$ Swap with itself: `[10, 13, 14 | 37, 29]`
4. Min of `[37, 29]` is `29` $\to$ Swap with index 3: `[10, 13, 14, 29 | 37]`

### PSU Metrics & Formulas
* **Comparisons**: Always independent of the initial order:
  $$\text{Comparisons} = \frac{n(n - 1)}{2} \quad \text{in Best, Average, and Worst cases}$$
* **Swaps**:
  * **Maximum Swaps**: At most **$n - 1$ swaps**.
  * **Best for**: Situations where memory write operations are extremely costly (e.g., writing to Flash memory / EEPROM).
* **Stability**: **Unstable** (e.g., sorting `[4a, 4b, 2]` picks `2` and swaps with `4a`, resulting in `[2, 4b, 4a]`).

---

## 4. Insertion Sort

### Working Mechanism
Maintains a sorted subarray on the left. Takes the next element (the "key") and inserts it into its correct position among the already-sorted elements by shifting larger elements one position to the right.

### Worked Example: `[12, 11, 13, 5, 6]`
1. `i = 1`, Key = `11`: Compare with `12` $\to$ shift `12` $\to$ `[11, 12, 13, 5, 6]`
2. `i = 2`, Key = `13`: Compare with `12` $\to$ already in place $\to$ `[11, 12, 13, 5, 6]`
3. `i = 3`, Key = `5`: Shifts `13, 12, 11` $\to$ `[5, 11, 12, 13, 6]`
4. `i = 4`, Key = `6`: Shifts `13, 12, 11` $\to$ `[5, 6, 11, 12, 13]`

### PSU Metrics & Formulas
* **Comparisons**:
  * **Best Case** (Already sorted): $n - 1$ comparisons ($O(n)$).
  * **Worst Case** (Reverse sorted): $\frac{n(n - 1)}{2}$ comparisons ($O(n^2)$).
* **Shifts/Movements**: Number of shifts $= \text{Inversion count } I$.
  $$\text{Running time} = O(n + I)$$
* **Best Choice For**:
  1. Small arrays ($n \le 20-30$, often used as the base-case cutoff in Hybrid Quick/Merge sorts).
  2. **Online sorting**: Can sort an incoming live data stream as elements arrive.
  3. Almost-sorted data ($I = O(n) \implies O(n)$ time).

---

## 5. Merge Sort

### Working Mechanism
A **Divide and Conquer** algorithm. Divides the array into two equal halves until single elements remain, recursively sorts them, and merges the two sorted halves using an auxiliary array.

### Worked Example: `[38, 27, 43, 3, 9, 82, 10]`
1. **Divide**: Split down to `[38], [27], [43], [3]` and `[9], [82], [10]`.
2. **Merge Sub-lists**:
   * Merge `[38]` and `[27]` $\to$ `[27, 38]`
   * Merge `[43]` and `[3]` $\to$ `[3, 43]`
   * Merge `[27, 38]` and `[3, 43]` $\to$ `[3, 27, 38, 43]`
   * Merge `[9, 82]` and `[10]` $\to$ `[9, 10, 82]`
3. **Final Merge**:
   * Merge `[3, 27, 38, 43]` and `[9, 10, 82]` $\to$ `[3, 9, 10, 27, 38, 43, 82]`

### PSU Metrics & Formulas
* **Recurrence**:
  $$T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n) \implies \Theta(n \log_2 n) \quad \text{(All cases)}$$
* **Merging Two Sorted Arrays of sizes $p$ and $q$**:
  * **Minimum Comparisons**: $\min(p, q)$
  * **Maximum Comparisons**: $p + q - 1$
* **Space Complexity**: $\Theta(n)$ auxiliary array space + $O(\log n)$ recursive stack space $= \Theta(n)$.
* **Linked Lists**: Preferred algorithm for sorting linked lists because merging nodes requires $O(1)$ extra space (pointer manipulation) and no random access is required.

---

## 6. Quick Sort

### Working Mechanism
Divide and Conquer approach. Chooses a **pivot** element and partitions the array such that all elements smaller than the pivot go to its left, and all larger elements go to its right. Recursively partitions the left and right subarrays.

### Worked Example (Lomuto Partition, Pivot = Last Element): `[10, 80, 30, 90, 40, 50]`
* Pivot $= 50$. Maintain partition index $i = -1$.
  * Scan $j=0$ (`10` $\le 50$): $i=0 \to$ Swap `10` with `10` $\to$ `[10, 80, 30, 90, 40, 50]`
  * Scan $j=1$ (`80` $> 50$): No swap.
  * Scan $j=2$ (`30` $\le 50$): $i=1 \to$ Swap `30` with `80` $\to$ `[10, 30, 80, 90, 40, 50]`
  * Scan $j=3$ (`90` $> 50$): No swap.
  * Scan $j=4$ (`40` $\le 50$): $i=2 \to$ Swap `40` with `80` $\to$ `[10, 30, 40, 90, 80, 50]`
* Finally, place pivot: Swap pivot `50` with element at $i+1=3$ (`90`) $\to$ `[10, 30, 40, 50, 80, 90]`. Pivot `50` is in its final sorted position.

### PSU Metrics & Formulas
* **Best/Average Case**: Occurs on balanced partitions (e.g., $1:1$ or constant ratio $\alpha : (1-\alpha)$):
  $$T(n) = 2T\left(\frac{n}{2}\right) + O(n) \implies O(n \log n)$$
* **Worst Case**: Occurs when the partition is maximally skewed ($0 : n-1$).
  * Causes: Array is already sorted (ascending or descending) and pivot is picked as the first or last element.
  $$\text{Recurrence}: T(n) = T(n-1) + T(0) + \Theta(n) \implies O(n^2)$$
  $$\text{Worst-case Comparisons}: \frac{n(n - 1)}{2}$$
* **Auxiliary Space (Recursion Call Stack)**:
  * Best/Average: $O(\log n)$
  * Worst: $O(n)$
* **Mitigation**: Randomized pivot selection or Median-of-Three pivot strategy.

---

## 7. Heap Sort

### Working Mechanism
1. Build a **Max-Heap** from the input array.
2. The root of the heap contains the maximum element. Swap it with the last element of the unsorted array and reduce the heap size by 1.
3. Call `Max-Heapify` on the root to restore heap property.
4. Repeat until the heap size reduces to 1.

### Key Operations & Complexities
* **Build-Max-Heap**:
  * Takes **$O(n)$** time (NOT $O(n \log n)$).
  * Formal summation: $\sum_{h=0}^{\lfloor \log n \rfloor} \lceil \frac{n}{2^{h+1}} \rceil O(h) = O(n)$.
* **Heapify Operation**: $O(\log n)$ time.
* **Extraction Phase**: Runs $(n - 1)$ times, each taking $O(\log n)$ time $\implies O(n \log n)$.
* **Total Time**: $O(n) + O(n \log n) = \mathbf{O(n \log n)}$ across **all cases** (Best, Average, Worst).
* **Auxiliary Space**: $\mathbf{O(1)}$ (In-place sorting).
* **Stability**: **Unstable**.

---

## 8. Non-Comparison Based Sorts

### Counting Sort
* **Concept**: Counts the frequencies of each distinct element, computes prefix sums to determine exact output positions, and places elements from right to left (to ensure stability).
* **Condition**: Keys must be integers in a bounded range $[0, k]$.
* **Time Complexity**: $\Theta(n + k)$.
* **Space Complexity**: $\Theta(n + k)$ for count and output arrays.
* **When is it linear?** When $k = O(n)$. If $k = O(n^2)$, it degrades to $O(n^2)$.

### Radix Sort
* **Concept**: Sorts elements digit by digit, from least significant digit (LSD) to most significant digit (MSD), using a **stable** subroutine (typically Counting Sort).
* **Time Complexity**: $\Theta(d(n + k))$, where $d$ is number of digits and $k$ is the base/radix.
  * For $n$ numbers in range $[1, n^c]$ with base $n$: $d = c$, $k = n \implies \mathbf{O(c \cdot n) = O(n)}$ time.
* **Space Complexity**: $O(n + k)$.

---

## 9. IOCL Rapid-Fire Comparison Questions

1. **Lower Bound for Comparison Sorts**:
   * Any comparison-based sorting algorithm requires at least **$\lceil \log_2(n!) \rceil = \Omega(n \log n)$** comparisons in the worst case (derived from decision tree height).
2. **Sort with Minimum Data Movement (Swaps)**:
   * **Selection Sort** (at most $n - 1$ swaps).
3. **Sort Best for Small Arrays / Almost Sorted Data**:
   * **Insertion Sort** ($O(n)$ time when inversions $I = O(n)$).
4. **Sort with $O(n \log n)$ Worst-Case and $O(1)$ Space**:
   * **Heap Sort** (Merge sort requires $O(n)$ space; Quick sort is $O(n^2)$ worst-case).
5. **Which Sorts are Stable by Default?**
   * Bubble Sort, Insertion Sort, Merge Sort, Counting Sort, Radix Sort.
6. **Which Sorts are Unstable?**
   * Selection Sort, Quick Sort, Heap Sort.
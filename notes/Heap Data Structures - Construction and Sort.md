[!definition] A Binary Heap is a complete binary tree implemented within a contiguous array satisfying the Heap Property:
Max Heap: $\text{Key}(\text{Parent}) \ge \text{Key}(\text{Children})$ for all nodes.
Min Heap: $\text{Key}(\text{Parent}) \le \text{Key}(\text{Children})$ for all nodes.
[!formula]
Array Representation (1-based indexing):
Parent of node $i$: $\lfloor i / 2 \rfloor$
[cite: 11]
Left Child of node $i$: $2i$
[cite: 11]
Right Child of node $i$: $2i + 1$
[cite: 11]
Operational Complexities:
Finding Min/Max: $O(1)$


Insert Operation: $O(\log n)$


Extract Min/Max (Delete Root): $O(\log n)$


Build Heap (Bottom-up Heapify): $O(n)$


Heap Sort: $O(n \log n)$ time and $O(1)$ auxiliary space



Code snippet
flowchart TD
    Build["Unsorted Array of n Elements"] --> BottomUp["Bottom-Up Heapify: Non-leaf nodes downto 1"]
    BottomUp --> Linear["Build Heap Completes in O(n) Time"]
    Linear --> Extract["Extract Root: Swap A[1] with A[size], Heapify(A[1])"]
    Extract --> LogN["Per-Extraction Time: O(log n)"]


[!trap] BST vs. Heap Invariance Trap: In a Max Heap, the left child is not necessarily smaller than the right child. Any child configuration is valid as long as both children are $\le$ Parent. A heap does not support $O(\log n)$ arbitrary search (searching takes $O(n)$).
[!question] GATE / PSU Practice Drill: A Max Heap is stored in an array: [90, 70, 80, 40, 50, 60, 30]. If the maximum element is deleted, what is the resulting level-order array? (A) [80, 70, 60, 40, 50, 30]
(B) [80, 70, 30, 40, 50, 60]

(C) [70, 80, 60, 40, 50, 30]

(D) [80, 60, 70, 40, 50, 30]

Step-by-Step Resolution:
Delete root ($90$) and replace it with the last element ($30$):
$$\text{Array: } [30, 70, 80, 40, 50, 60]$$


Heapify root at index 1:
Children of $30$: Left child = index 2 ($70$), Right child = index 3 ($80$).
Largest child is $80$ at index 3.
Swap $30$ with $80$:
$$\text{Array: } [80, 70, 30, 40, 50, 60]$$


Continue Heapify at index 3:
Child of index 3: Left child = index 6 ($60$).
Compare $30$ with $60$: $60 > 30$, swap.
Result:
$$\text{Array: } [80, 70, 60, 40, 50, 30]$$


Correct Answer: (A) [80, 70, 60, 40, 50, 30]

# PSU & Competitive Exam Question Bank: Sorting Algorithms

> [!info] Structure
> This collection covers high-yield sorting concepts frequently tested in technical PSU examinations (ISRO, BARC, BEL, CIL, DRDO, NIC, IOCL). Click each question arrow to expand the complete derivation and verified answers.

---

## 1. Classical Comparison Sorts

> [!question]- SORT-01: Minimum Swaps to Sort an Arbitrary Array
> What is the minimum number of swaps required to sort an unsorted array of $n$ distinct elements into ascending order?
> > **Answer:** $\sum_{i=1}^k (c_i - 1) = n - k$, where $k$ is the number of disjoint permutation cycles in the array.  
> > **Explanation:**  
> > Any permutation can be uniquely decomposed into disjoint cycles. A cycle of length $c_i$ requires exactly $c_i - 1$ swaps to place every element into its correct target position. Summing across all $k$ disjoint cycles gives $\sum (c_i - 1) = (\sum c_i) - k = n - k$.  
> > Cycle sort achieves this theoretical minimum number of memory writes.

> [!question]- SORT-02: Insertion Sort vs. Bubble Sort on Partially Inverted Inputs
> If an array of size $n$ has exactly $I$ inversions:
> 1. What is the exact number of swaps performed by Bubble Sort?
> 2. What is the running time of Insertion Sort in terms of $n$ and $I$?
> > **Answer:**  
> > 1. Bubble Sort performs **exactly $I$ swaps**. Every adjacent swap eliminates exactly one inversion.  
> > 2. Insertion Sort runs in **$\mathcal{O}(n + I)$** time.  
> > **Key Rule:** When $I = \mathcal{O}(n)$ (nearly sorted array), Insertion Sort executes in linear $\mathcal{O}(n)$ time.

> [!question]- SORT-03: Selection Sort Stability Transformation
> Why is Selection Sort inherently unstable, and how can it be made stable without changing its comparison logic?
> > **Answer:**  
> > - **Why Unstable:** In an array like `[4a, 4b, 2]`, the minimum element `2` is swapped with index 0 (`4a`), placing `4a` after `4b` $\to [2, 4b, 4a]$.  
> > - **Making it Stable:** Instead of **swapping** the minimum element with the current position, **shift** all intermediate elements one position to the right and insert the minimum element into place. (This maintains stability but increases write operations from $\mathcal{O}(n)$ swaps to $\mathcal{O}(n^2)$ shifts).

> [!question]- SORT-04: Merge Sort Auxiliary Space Nuances
> Why does standard Merge Sort on an array take $\mathcal{O}(n)$ auxiliary space, whereas Merge Sort on a singly linked list can be done in $\mathcal{O}(1)$ auxiliary space?
> > **Answer:**  
> > - **Arrays:** Elements reside in contiguous memory locations. Merging two subarrays in-place without overwriting unmerged elements requires an extra buffer of size $n$.  
> > - **Linked Lists:** Merging is performed purely by rearranging pointer links (`next` pointers) between existing nodes. No new nodes or auxiliary data arrays need to be allocated, requiring $\mathcal{O}(1)$ space (ignoring call stack depth, or $\mathcal{O}(1)$ strict space if implemented iteratively).

---

## 2. Advanced Divide-and-Conquer & Heap Sort

> [!question]- SORT-05: Median-of-Three Quick Sort Resistance
> How does the "Median-of-Three" pivot selection strategy affect the worst-case time complexity of Quick Sort?
> > **Answer:** The worst-case time complexity remains **$\mathcal{O}(n^2)$**.  
> > **Explanation:**  
> > Median-of-three (choosing the median of the first, middle, and last elements) prevents worst-case degradation on strictly sorted or reverse-sorted inputs. However, an adversary can deliberately construct an "anti-median-of-three" permutation that still yields $0$ and $n-1$ splits at every recursive step, maintaining the worst-case $\mathcal{O}(n^2)$ bound.

> [!question]- SORT-06: Linear Time Heap Construction Proof
> Why does `Build-Max-Heap` take $\mathcal{O}(n)$ time instead of $\mathcal{O}(n \log n)$?
> > **Answer:** Because most nodes reside close to the bottom of the tree where the subtree height is very small.  
> > **Derivation:**  
> > A heap of size $n$ has at most $\lceil n / 2^{h+1} \rceil$ nodes at height $h$.  
> > The total cost is:  
> > $$\sum_{h=0}^{\lfloor \log_2 n \rfloor} \left\lceil \frac{n}{2^{h+1}} \right\rceil \mathcal{O}(h) = \mathcal{O}\left( n \sum_{h=0}^{\infty} \frac{h}{2^h} \right)$$  
> > Since the infinite arithmetic-geometric series $\sum_{h=0}^{\infty} \frac{h}{2^h} = 2$ (a constant):  
> > $$\text{Cost} = \mathcal{O}(n \cdot 2) = \mathcal{O}(n)$$

> [!question]- SORT-07: Heap Sort Best-Case Behavior
> Can standard Heap Sort ever run in $\mathcal{O}(n)$ time?
> > **Answer:** Yes, if all elements in the input array are identical (duplicates).  
> > **Explanation:**  
> > When all elements are identical, building the heap takes $\mathcal{O}(n)$. During the extraction phase, every call to `maxHeapify` terminates in $\mathcal{O}(1)$ because the root element is already equal to both of its children. Thus, $n$ extractions take $n \times \mathcal{O}(1) = \mathcal{O}(n)$ time.  
> > If elements are distinct, the best case remains $\Omega(n \log n)$.

> [!question]- SORT-08: Quick Sort Recursion Depth Bounding
> How can Quick Sort's worst-case auxiliary recursion stack space be reduced from $\mathcal{O}(n)$ down to guaranteed $\mathcal{O}(\log n)$?
> > **Answer:** By using **tail call optimization** and always recursing on the **smaller partition first**.  
> > **Method:**  
> > After partitioning into left and right subarrays, make the recursive function call on the smaller subarray (size $\le n/2$). Use an iterative `while` loop to process the larger partition. Because the smaller half is at most size $n/2$, the maximum recursion call depth is strictly bounded by $\lfloor \log_2 n \rfloor$.

---

## 3. Linear Time (Non-Comparison) Sorts

> [!question]- SORT-09: Counting Sort Stability & Negative Values
> 1. Why must the final placement loop in Counting Sort iterate backwards (from index $n-1$ down to $0$)?
> 2. How can Counting Sort handle an array containing negative numbers?
> > **Answer:**  
> > 1. **Stability:** The count array stores cumulative positions indicating the *last* valid index for each key. Iterating backwards ensures that the element appearing last in the input array gets placed at that highest index, preserving the original relative order of duplicate keys.  
> > 2. **Negative Numbers:** Find the minimum element $min$. Shift every element by subtracting $min$ (i.e., $arr[i] - min \ge 0$), run standard Counting Sort, and add $min$ back when writing the output.

> [!question]- SORT-10: Radix Sort Base Selection
> To sort $n$ integers in the range $[0, n^k - 1]$ in optimal linear time $\mathcal{O}(n)$, what base $b$ should be chosen for Radix Sort?
> > **Answer:** Choose base $b = n$.  
> > **Explanation:**  
> > Time complexity of Radix Sort using Counting Sort per pass:  
> > $$T(n) = \Theta(d(n + b)) \quad \text{where } d = \log_b(n^k) = k \log_b n$$  
> > Setting $b = n \implies d = k \log_n n = k$ passes.  
> > Total time $= \Theta(k(n + n)) = \Theta(k \cdot n)$. Since $k$ is a constant, $T(n) = \Theta(n)$.

> [!question]- SORT-11: Bucket Sort Distribution Requirement
> What condition on the input distribution is necessary for Bucket Sort to achieve an average running time of $\mathcal{O}(n)$?
> > **Answer:** The input values must be drawn independently from a **uniform distribution** over the interval $[0, 1)$ (or $[a, b]$).  
> > **Explanation:**  
> > Under uniform distribution, the number of elements falling into each bucket follows a binomial distribution with expected value $\mathcal{O}(1)$. The sum of squares of bucket sizes $\sum E[n_i^2]$ evaluates to $\mathcal{O}(n)$, allowing the inner sorting (typically Insertion Sort) to run in linear total time.

---

## 4. Lower Bounds & Sorting Limits

> [!question]- SORT-12: Decision Tree Height for $n!$ Permutations
> Prove mathematically why any comparison-based sorting algorithm requires at least $\Omega(n \log n)$ comparisons in the worst case.
> > **Answer:**  
> > 1. For an array of $n$ distinct elements, there are $n!$ possible permutations.  
> > 2. A decision tree performing binary comparisons must have at least $l \ge n!$ leaf nodes to distinguish every possible outcome.  
> > 3. A binary tree of height $h$ has at most $2^h$ leaves:  
> >    $$2^h \ge n! \implies h \ge \log_2(n!)$$  
> > 4. By Stirling's Approximation ($\ln(n!) \approx n \ln n - n$):  
> >    $$h \ge \sum_{i=1}^n \log_2 i \ge \sum_{i=n/2}^n \log_2(n/2) = \frac{n}{2} \log_2\left(\frac{n}{2}\right) = \Omega(n \log n)$$

> [!question]- SORT-13: Sorting $n$ Elements with $k$ Distinct Values
> An array of size $n$ contains elements with only $k$ distinct values ($k \ll n$). What is the information-theoretic lower bound on the number of comparisons needed to sort it?
> > **Answer:** $\Omega(n \log k)$  
> > **Explanation:**  
> > The number of unique arrangements of $n$ elements with multiplicities $n_1, n_2, \dots, n_k$ (where $\sum n_i = n$) is given by the multinomial coefficient $\frac{n!}{n_1! n_2! \dots n_k!}$. Taking the base-2 logarithm of this value maximizes when each distinct element appears roughly $n/k$ times, yielding a lower bound of $\Omega(n \log k)$. (Algorithms like 3-Way Quick Sort or Balanced BST Sort achieve this bound).
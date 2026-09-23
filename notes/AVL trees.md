---

## subject: "DS" topic: "AVL Trees" source: "https://www.youtube.com/watch?v=9QSN62vo-l0&list=PLIPZ2_p3RNHgsP1q_r_7af_Sii_aZZ8aa"

# AVL Trees

---
[https://www.youtube.com/watch?v=9QSN62vo-l0&list=PLIPZ2_p3RNHgsP1q_r_7af_Sii_aZZ8aa](https://www.youtube.com/watch?v=9QSN62vo-l0&list=PLIPZ2_p3RNHgsP1q_r_7af_Sii_aZZ8aa)"
## 1. Core Concept & Properties

- **Definition:** Self-balancing BSTs
- **Height:** Number of **edges** on the longest path from root to leaf
- **Density vs Height:** More nodes per level = less height. Sparse levels = more height
- **Tree Counting:** To count unique AVL trees for a given key set — analyze possibilities for each root key separately

---

## 2. Balance Operations (Rotations)

> Rotations are just **pointer reassignments** — $O(1)$ time. Not actually "shifting shapes."

`INVARIANT`: **The Middle Value Always Becomes the Root.**
	An AVL tree is a Binary Search Tree. The sorted order $(A < B < C)$ can never change. When three nodes fall out of balance, the **middle value (median) must become the parent**, while the smallest goes left and the largest goes right.

### The Signs (Balance Factor)

Every node calculates a Balance Factor ($BF$):

$$BF = \text{Height}(\text{Left Subtree}) - \text{Height}(\text{Right Subtree})$$

- A node is **balanced** if $BF \in \{-1, 0, +1\}$.
- A node is **unbalanced** the moment $BF$ hits **$+2$** or **$-2$**.
    - **$+2$** means the node is **Left-Heavy** (leaning left)
    - **$-2$** means the node is **Right-Heavy** (leaning right).

After every insertion, walk back up toward the root. Find the **first node with $BF = +2$ or $-2$**. Stop right there—that is the node you must fix.

### The 4 Imbalances & Their Exact Fixes

Look at the unbalanced node ($z$) and its child ($y$):

|**Case**|**BF(Node z)**|**BF(Child y)**|**What Happened**|**What You Do**|
|---|---|---|---|---|
|**LL**|**$+2$**|**$+1$**|Line slanting left|**Right Rotate** on $z$|
|**RR**|**$-2$**|**$-1$**|Line slanting right|**Left Rotate** on $z$|
|**LR**|**$+2$**|**$-1$**|"Elbow" (left then right)|**Left Rotate** on $y$, then **Right Rotate** on $z$|
|**RL**|**$-2$**|**$+1$**|"Elbow" (right then left)|**Right Rotate** on $y$, then **Left Rotate** on $z$|

### Stick → Mountain (Single Rotation)

- Triggered by **straight line** imbalance: LL or RR insertion
- Middle node shifts up to become new subtree root

### Elbow → Mountain (Double Rotation)

- Triggered by **zigzag** imbalance: LR or RL insertion
- Last node shifts to middle
- Step 1: Rotate bottom edge → turn elbow into stick
- Step 2: Rotate again → form balanced mountain

---

## 3. Mathematical Bounds

**Minimum nodes for height $h$:** $$n(h) = n(h-1) + n(h-2) + 1$$

> $n(0) = 1$, $n(1) = 2$ — mirrors Fibonacci growth

**Maximum nodes for height $h$:** $$n_{max} = 2^{h+1} - 1$$

> Perfectly complete binary tree

---

## 4. Operations

### Left Rotation (Right-Heavy Imbalance)

```java
function leftRotate(X):
    Y = X.right
    T2 = Y.left

    Y.left = X
    X.right = T2

    X.height = max(height(X.left), height(X.right)) + 1
    Y.height = max(height(Y.left), height(Y.right)) + 1

    return Y  // new subtree root
```

---

### Insertion

> Standard BST insert → backtrack → check balance → **first imbalanced node** → rotate Shape is determined by that node + path to insertion point

```c
function insert(node, key):
    // 1. Standard BST Insert
    if node is null: return newNode(key)
    if key < node.key:     node.left  = insert(node.left, key)
    else if key > node.key: node.right = insert(node.right, key)
    else: return node  // no duplicates

    // 2. Update Height
    node.height = 1 + max(height(node.left), height(node.right))

    // 3. Balance Factor
    balance = height(node.left) - height(node.right)

    // 4. Rebalance
    if balance > 1  and key < node.left.key:   return rightRotate(node)          // LL
    if balance < -1 and key > node.right.key:  return leftRotate(node)           // RR
    if balance > 1  and key > node.left.key:                                     // LR
        node.left = leftRotate(node.left)
        return rightRotate(node)
    if balance < -1 and key < node.right.key:                                    // RL
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node
```

> ⚠️ Even after rotating, backtracking continues to root to update heights

> ⚠️ Rebalancing may decrease height or keep it same — but **insertion never decreases height**. It can't — that would break the minimum node-height relation.
---

### Deletion

> Delete as usual → backtrack → first imbalanced node → rotate **towards longer height side** (use balance factor to find it).
> Unlike insertion, we do NOT move towards point of deletion.
>  
>  Keep backtracking — imbalance can cascade. May rotate multiple times. 
>   
>  **Same height case → make a stick** (not for convenience —it's required for correctness)

```c
function delete(node, key):
    // 1. Standard BST Delete
    if node is null: 
	    return node
    if key < node.key:      
	    node.left  = delete(node.left, key)
    else if key > node.key: 
	    node.right = delete(node.right, key)
    else:
        if node.left is null or node.right is null:
            temp = node.left if node.left else node.right
            if temp is null: node = null
            else: node = temp
        else:
            temp = minValueNode(node.right)
            node.key = temp.key
            node.right = delete(node.right, temp.key)

    // 2. Update Height
    node.height = 1 + max(height(node.left), height(node.right))

    // 3. Balance Factor
    balance = height(node.left) - height(node.right)

    // 4. Rebalance (can cascade up to root)
    // LL
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)
    // LR
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    // RR
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)
    // RL
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node
```


---

## 5. Complexity

Here is the complete reference table of complexities, memory costs, and operational bounds for an **AVL Tree** (where $n$ is the total number of nodes, and $h$ is the height).

### Time & Space Complexity

| **Operation**         | **Best Case** | **Average Case** | **Worst Case** | **Notes / Mechanism**                                                           |
| --------------------- | ------------- | ---------------- | -------------- | ------------------------------------------------------------------------------- |
| **Search / Lookup**   | $O(1)$        | $O(\log n)$      | $O(\log n)$    | Strict height-balanced property guarantees search never degrades to $O(n)$.     |
| **Insertion**         | $O(1)$        | $O(\log n)$      | $O(\log n)$    | Standard BST insertion ($O(\log n)$) $+$ backtracking up to root ($O(\log n)$). |
| **Deletion**          | $O(1)$        | $O(\log n)$      | $O(\log n)$    | Standard BST removal ($O(\log n)$) $+$ potential rebalancing up the path.       |
| **Find Min / Max**    | $O(1)$        | $O(\log n)$      | $O(\log n)$    | Walk leftmost or rightmost branch down from the root.                           |
| **Inorder Traversal** | $O(n)$        | $O(n)$           | $O(n)$         | Visits all $n$ nodes in strictly sorted ascending order.                        |
| **Space Complexity**  | $O(n)$        | $O(n)$           | $O(n)$         | Stores $n$ nodes. Each node requires auxiliary balance data (see below).        |

### Rotation Bounds & Operational Costs

|**Metric / Parameter**|**Value / Bound**|**Explanation / GATE High-Yield Fact**|
|---|---|---|
|**Max Rotations on Insert**|**$1$ (Single or Double)**|Once the lowest unbalanced ancestor is rotated, the original subtree height is restored. Rebalancing **terminates immediately**.|
|**Max Rotations on Delete**|**$O(\log n)$**|Rebalancing a subtree can reduce its height by $1$, propagating an imbalance up to the parent. In the worst case, rotations occur at every level up to the root.|
|**Time per Single Rotation**|$O(1)$|Constant number of pointer reassignments ($3$ to $4$ pointer swaps).|
|**Auxiliary Space per Node**|$\mathbf{2\text{ bits}}$ (or $1\text{ byte}$)|Minimal requirement to store Balance Factor $\in \{-1, 0, +1\}$ (or $4$ bytes if storing integer height explicitly).|

### Height & Structural Bounds

|**Structural Metric**|**Formula / Exact Bound**|**Practical Consequence**|
|---|---|---|
|**Max Height ($h_{\max}$)**|$\approx 1.4404 \log_2(n + 2) - 0.328$|At most $\approx 44\%$ taller than a perfectly balanced complete binary tree.|
|**Min Height ($h_{\min}$)**|$\lfloor \log_2 n \rfloor$|Occurs when the AVL tree is a complete/perfect binary tree.|
|**Min Nodes for Height $h$ ($N_h$)**|$N_h = N_{h-1} + N_{h-2} + 1$|Follows the Fibonacci-like recurrence with base cases: $N_0 = 1, N_1 = 2, N_2 = 4, N_3 = 7, N_4 = 12$.|
|**Max Nodes for Height $h$**|$2^{h+1} - 1$|When all levels are completely saturated (perfect tree).|

### AVL vs. Red-Black Tree Efficiency Tradeoff

|**Dimension**|**AVL Tree**|**Red-Black Tree**|**Winner / Practical Usage**|
|---|---|---|---|
|**Height Balance**|Strict ($\Vert{}BF\Vert{} \le 1$)|Relaxed ($h \le 2 \log_2(n + 1)$)|**AVL** is shorter $\implies$ faster lookups.|
|**Search Speed**|Faster|Slightly slower|**AVL** wins for read-heavy workloads (databases, lookups).|
|**Insertion Cost**|At most 1 rotation|At most 2 rotations|**Tie** ($O(1)$ rotations for both).|
|**Deletion Cost**|Up to $O(\log n)$ rotations|At most 3 rotations ($O(1)$)|**Red-Black** wins for write/delete-heavy workloads (e.g., `std::map`, Java `TreeMap`, Linux kernel CFS).|
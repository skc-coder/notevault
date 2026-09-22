[!definition]
Strict (Full) Binary Tree: Every internal node has exactly 2 children.
Complete Binary Tree: All levels are completely filled except possibly the last, which is filled from left to right.
Binary Search Tree (BST): For every node $X$, all keys in the left subtree are $< \text{Key}(X)$ and all keys in the right subtree are $> \text{Key}(X)$.
[!theorem] Strict Binary Tree Invariants: For any strict binary tree with $L$ leaves, $I$ internal nodes, and $N$ total nodes:
$L = I + 1$


$N = 2I + 1 = 2L - 1$


$\text{Total Edges } E = N - 1 = 2I = 2L - 2$


[!formula] Catalan Numbers in Binary Tree Counting: Total structurally distinct binary trees (or distinct BSTs) possible with $n$ unlabelled nodes:

$$C_n = \frac{1}{n + 1}\binom{2n}{n}$$

For $n = 4$: $C_4 = \frac{1}{5}\binom{8}{4} = \frac{70}{5} = 14$


For $n = 5$: $C_5 = \frac{1}{6}\binom{10}{5} = \frac{252}{6} = 42$


[!trap]
Unique Tree Reconstruction Traps:
Preorder + Postorder cannot uniquely reconstruct a general binary tree (requires strict binary property).
Preorder + Inorder uniquely reconstructs any binary tree.
Postorder + Inorder uniquely reconstructs any binary tree.
In a BST, the Inorder traversal is always sorted in ascending order. Therefore, giving only Preorder or only Postorder for a BST is sufficient for unique reconstruction.
[!question] PSU CBT Practice Drill: A full (strict) binary tree contains 15 internal nodes. What is the total number of nodes in the tree? (A) 29
(B) 30
(C) 31
(D) 32
Step-by-Step Resolution:
Number of internal nodes $I = 15$.
Apply leaf-internal relation: $L = I + 1 = 15 + 1 = 16$.
Total nodes $N = I + L = 15 + 16 = 31$.
Shortcut formula check: $N = 2I + 1 = 2(15) + 1 = 31$.
Correct Answer: (C) 31

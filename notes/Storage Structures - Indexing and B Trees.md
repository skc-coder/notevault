> [!definition]
> * **Blocking Factor ($Bfr$):** The maximum number of records or index entries stored in a single disk block[cite: 2].
> * **Primary Index:** Defined on an **ordered** file on a **key** attribute[cite: 2]. Typically sparse[cite: 2].
> * **Clustering Index:** Defined on an **ordered** file on a **non-key** attribute[cite: 2].
> * **Secondary Index:** Defined on an **unordered** file over a key or non-key attribute[cite: 2]. Must be dense when created over candidate keys[cite: 2].

> [!formula]
> **Node Capacity and Order Equations:**
> Let $B$ be block size, $K$ be search key size, $P_b$ be block pointer size, and $R_p$ be record pointer size[cite: 2].
>
> **1. B-Tree Node (Order $P$):**
> Contains $P$ block pointers, $(P - 1)$ search keys, and $(P - 1)$ record pointers[cite: 2]:
> $$P \cdot P_b + (P - 1) \cdot (K + R_p) \le B$$[cite: 2]
>
> **2. $B^+$-Tree Internal Node (Order $P$):**
> Contains $P$ child block pointers and $(P - 1)$ search keys (no record pointers)[cite: 2]:
> $$P \cdot P_b + (P - 1) \cdot K \le B$$[cite: 1, 2]
>
> **3. $B^+$-Tree Leaf Node (Order $P_{\text{leaf}}$):**
> Contains key-pointer pairs $(K, R_p)$ and one block pointer $P_b$ to the sibling leaf[cite: 2]:
> $$P_{\text{leaf}} \cdot (K + R_p) + P_b \le B$$[cite: 2]

| Node Type | Minimum Pointers (Non-Root) | Minimum Keys (Non-Root) | Maximum Pointers | Maximum Keys |
| :--- | :--- | :--- | :--- | :--- |
| **B-Tree Internal Node** | $\lceil P/2 \rceil$[cite: 2] | $\lceil P/2 \rceil - 1$[cite: 2] | $P$[cite: 2] | $P - 1$[cite: 2] |
| **B-Tree Root** | $2$ (if non-leaf)[cite: 2] | $1$[cite: 2] | $P$[cite: 2] | $P - 1$[cite: 2] |
| **$B^+$-Tree Internal Node** | $\lceil P/2 \rceil$[cite: 2] | $\lceil P/2 \rceil - 1$[cite: 2] | $P$[cite: 2] | $P - 1$[cite: 2] |
| **$B^+$-Tree Leaf Node** | $\lceil (P_{\text{leaf}})/2 \rceil$ entries[cite: 2] | $\lceil (P_{\text{leaf}})/2 \rceil$ entries[cite: 2] | $P_{\text{leaf}}$ entries[cite: 2] | $P_{\text{leaf}}$ entries[cite: 2] |

> [!trap]
> **B-Tree vs $B^+$-Tree Node Space Allocation:**
> For identical block size $B$, the order $P$ of a $B^+$-tree internal node is strictly greater than that of a B-tree node because $B^+$-tree internal nodes omit record pointers ($R_p$)[cite: 2]. This yields higher fan-out, reduced tree height, and fewer disk I/O accesses[cite: 2].

> [!question]
> **GATE / PSU Practice Drill:**
> In a $B^+$ tree, the search-key value is $8\text{ bytes}$ long, the block size is $512\text{ bytes}$, and the block pointer is $2\text{ bytes}$[cite: 1]. Compute the maximum order of the internal node of this $B^+$ tree[cite: 1].
>
> **Step-by-Step Resolution:**
> 1. Formulate internal node inequality:
>    $$P \cdot P_b + (P - 1) \cdot K \le B$$[cite: 1, 2]
> 2. Substitute parameters: $K = 8\text{ bytes}$, $P_b = 2\text{ bytes}$, $B = 512\text{ bytes}$[cite: 1]:
>    $$P(2) + (P - 1)(8) \le 512$$[cite: 1]
>    $$2P + 8P - 8 \le 512$$
>    $$10P \le 520 \implies P \le 52$$
> 3. Maximum order $P = 52$[cite: 1].
>
> **Maximum Order:** $52$[cite: 1]

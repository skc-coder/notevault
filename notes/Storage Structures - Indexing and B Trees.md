> [!definition]
> * **Blocking Factor ($Bfr$):** The maximum number of records or index entries stored in a single disk block[cite: 2].
> * **Primary Index:** Defined on an **ordered** file on a **key** attribute[cite: 2]. Typically sparse[cite: 2].
> * **Clustering Index:** Defined on an **ordered** file on a **non-key** attribute[cite: 2].
> * **Secondary Index:** Defined on an **unordered** file over a key or non-key attribute[cite: 2]. Must be dense when created over candidate keys[cite: 2].
### Part 1: Physical Disk Storage & Index Sizing

#### 1. Blocking Factor ($Bfr$)

- **What it is:** The maximum number of records or index entries you can pack into a single disk block without spanning across blocks.
    
- **Variables:**
    
    - $B$ = Block size (in bytes)
        
    - $R$ = Record size (in bytes)
        
- **The Formula:**
    
    $$Bfr = \left\lfloor \frac{B}{R} \right\rfloor$$
    
- **Intuition:** You divide the block size by the record size. You **floor** ($\lfloor \dots \rfloor$) because you cannot fit half a record into a block; partial records get pushed to the next block.
    

#### 2. Number of Blocks Required for a Data File ($b$)

- **What it is:** How many physical disk blocks are needed to hold all rows in a table.
    
- **Variables:**
    
    - $N$ = Total number of records (rows) in the table
        
    - $Bfr$ = Blocking factor of the table
        
- **The Formula:**
    
    $$b = \left\lceil \frac{N}{Bfr} \right\rceil$$
    
- **Intuition:** You **ceiling** ($\lceil \dots \rceil$) because if you have even one leftover record that doesn't fill a block, it still consumes an entire new block on disk.
    

#### 3. Sizing Indexes: Primary vs. Clustering vs. Secondary

An index entry is just a small pair: $(\text{Search Key } K + \text{Pointer } P)$.

- Let the size of one index entry be:
    
    $$R_i = K + P$$
    
- The **Index Blocking Factor** ($Bfr_i$) is:
    
    $$Bfr_i = \left\lfloor \frac{B}{R_i} \right\rfloor = \left\lfloor \frac{B}{K + P} \right\rfloor$$
    

Now, how many index entries ($N_i$) and index blocks ($b_i$) exist?

|**Index Type**|**Number of Index Entries (Ni​)**|**Number of Index Blocks (bi​)**|**Why?**|
|---|---|---|---|
|**Primary Index** (Sparse)|$N_i = b$ (one per data block)|$b_i = \left\lceil \frac{b}{Bfr_i} \right\rceil$|Since data is sorted by primary key, you only store an entry for the **first record of each data block** (anchor record).|
|**Clustering Index** (Sparse)|$N_i = D$ (where $D$ = number of distinct values of the non-key attribute)|$b_i = \left\lceil \frac{D}{Bfr_i} \right\rceil$|All rows with the same value are clustered together on disk, so you only need **one entry per distinct cluster value**.|
|**Secondary Index on Key** (Dense)|$N_i = N$ (one per every single record)|$b_i = \left\lceil \frac{N}{Bfr_i} \right\rceil$|The data file is unordered, so there is no predictable sorting; every row must have an explicit pointer.|


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

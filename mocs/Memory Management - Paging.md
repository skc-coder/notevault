# Paging: Single-Level Paging Architecture & Address Translation

## Lecture & Conceptual Walkthrough

### 1. Motivation: The Evolution from Segmentation to Paging
In variable-partition allocation and pure segmentation, allocating a segment requires free-space management techniques such as First Fit, Best Fit, or Worst Fit. Because processes allocate and deallocate dynamically sized blocks over time, memory develops non-contiguous holes, resulting in **External Fragmentation**.

```
External Fragmentation in Contiguous/Segmented Memory:
+-------+------+-------+------+-------+------+
| Seg 0 | Free | Seg 1 | Free | Seg 2 | Free |
+-------+------+-------+------+-------+------+
Total free memory might be sufficient for an incoming segment,
but no single contiguous hole is large enough!
```

To eliminate external fragmentation without paging, the operating system must employ **Compaction** (relocating active memory chunks into a contiguous block to coalesce free space).

> [!trap] Compaction Overhead
> While compaction reclaims wasted memory, it introduces heavy runtime memory-copy latency and memory-bus traffic. It is computationally prohibitive in high-performance computing systems.

**The Core Idea of Paging:**
What if every allocated chunk is uniform in size? If both virtual space and physical space are partitioned into fixed-sized blocks, any free physical block can accommodate any virtual block.

> [!definition] Paging
> **Paging** is a modern, non-contiguous memory management scheme that divides:
> * **Logical Address Space ($LAS$):** into fixed-sized blocks called **Pages**.
> * **Physical Address Space ($PAS$ / Main Memory):** into fixed-sized blocks of the exact same size called **Frames**.
> 
> $$\text{Page Size} = \text{Frame Size}$$

* **External Fragmentation:** Completely **eliminated** because any available frame can be assigned to any page of any process.
* **Internal Fragmentation:** Present only within the final page of a process (bounded strictly to strictly less than $1\text{ Page}$). Kept minimal by configuring appropriate page sizes (typically $4\text{ KB}$).
* **Book Analogy:** Paging mirrors how a physical textbook functions:
  * Content is split into uniform *pages*.
  * An *index* (or table of contents) acts as the *page table*, mapping logical topic sections to physical book pages.

---

### 2. Paging Hardware Architecture & Mathematical Formulation

Every active process maintains its own independent **Page Table** in physical memory. The operating system tracks the base of this table using the **PTBR (Page Table Base Register)**.

```
Logical Address (LA):                Physical Address (PA):
+---------------------+--------+     +----------------------+--------+
|   Page Number (p)   | Offset |     |   Frame Number (f)   | Offset |
|      (n - k) bits   | k bits |     |     (m - k) bits     | k bits |
+----------+----------+---+----+     +----------+-----------+----+---+
           |              |                     ^                |
           v              |                     |                |
     Page Table           |                     |                |
   +----+-------+         |                     |                |
   | p  |   f   |---------+---------------------+                |
   +----+-------+         |                                      |
   | .. |  ...  |         +--------------------------------------+
```

> [!formula] Fundamental Structural Identities
> Let:
> * Logical Address Space $= 2^n\text{ Bytes} \implies n\text{-bit } LA$
> * Physical Address Space $= 2^m\text{ Bytes} \implies m\text{-bit } PA$
> * Page Size $=$ Frame Size $= 2^k\text{ Bytes} \implies k\text{ offset bits}$
>
> Then:
> 1. $\text{Number of Pages} = \frac{\text{Size of } LAS}{\text{Page Size}} = \frac{2^n}{2^k} = 2^{n-k}$
> 2. $\text{Page Number Bits } (p) = n - k$
> 3. $\text{Number of Frames} = \frac{\text{Size of } PAS}{\text{Frame Size}} = \frac{2^m}{2^k} = 2^{m-k}$
> 4. $\text{Frame Number Bits } (f) = m - k$
> 5. $\text{Number of Page Table Entries (PTEs)} = \text{Number of Pages} = 2^{n-k}$

> [!property] Offset Invariant
> The internal byte offset within a page is identical to the byte offset within the mapped frame:
> $$\text{Page Offset} \equiv \text{Frame Offset} = k\text{ bits}$$
> While total bits in $LA$ and $PA$ usually differ ($n \ne m$), their offset bit-width is identical because $\text{Page Size} = \text{Frame Size}$.

#### Integer Division and Modulo Analogy
Just as dividing a decimal number by $10^k$ yields the prefix via integer division (`//`) and the suffix via remainder (`%`):
* Decimal:
  $$\frac{1234}{10} \implies 1234 \mathbin{/\!/} 10 = 123, \quad 1234 \mathbin{\%} 10 = 4$$
  $$\frac{1234}{100} \implies 1234 \mathbin{/\!/} 100 = 12, \quad 1234 \mathbin{\%} 100 = 34$$
* Binary ($2^k$):
  Dividing an $n$-bit binary address by $2^k$ assigns:
  * The lower $k$ bits to the internal **Offset**: $d = LA \mathbin{\%} 2^k$
  * The remaining upper $(n - k)$ bits to the **Page Number**: $p = LA \mathbin{/\!/} 2^k$

#### Physical Address Calculation
$$\text{Physical Address } (PA) = (\text{Frame Number} \times \text{Frame Size}) + \text{Offset}$$

`Frame Number` is 0 indexed.

---

### 3. Page Table Structure & Entry Anatomy

A Page Table is indexed by the Page Number ($p$). Each entry is called a **Page Table Entry (PTE)**.

```
Typical Page Table Entry (PTE):
+-------------+---------------+---------------+---------------+-----------+
| Frame No.   | Valid/Invalid | Protection    | Reference     | Dirty     |
| (f bits)    | (Present Bit) | (R / W / X)   | (Accessed Bit)| (Mod Bit) |
+-------------+---------------+---------------+---------------+-----------+
```

* **Frame Number ($f$):** The base address bits of physical memory where the page resides. The minimum size of this field is $\lceil \log_2(\text{Number of Frames}) \rceil = (m - k)\text{ bits}$.
* **Valid / Invalid Bit (Present Bit):** Indicates whether the page is currently loaded in Main Memory ($1$) or still on secondary storage / unallocated ($0$).
* **Protection Bits:** Enforce access control ($R, W, X$).
* **Reference Bit (Accessed Bit):** Set by hardware whenever the page is read or written (used by page replacement algorithms like Clock/LRU).
* **Dirty Bit (Modified Bit):** Set by hardware whenever a write access modifies the page contents in memory (indicates the page must be written back to disk on eviction).

> [!trap] Minimum PTE Size vs. Real-World Alignment
> While the theoretical minimum bits required for a PTE is the number of bits needed to index all frames ($m - k$), in actual operating systems:
> $$\text{PTE Size} \ge (m - k) + \text{Control Bits}$$
> Furthermore, memory controllers require PTE sizes to be rounded up to byte-aligned or power-of-two boundaries (e.g., $2\text{ Bytes}$, $4\text{ Bytes}$, or $8\text{ Bytes}$).
> 
> $$\text{Page Table Size} = (\text{Number of Pages}) \times (\text{PTE Size}) = 2^{n-k} \times \text{PTE Size}$$

---

### 4. The Scale Problem of Single-Level Paging

In modern 32-bit and 64-bit architectures, single-level paging tables become prohibitively large to store in contiguous physical memory:

Consider a 32-bit logical address space ($LA = 32\text{ bits}$), with standard $4\text{ KB}$ pages ($2^{12}\text{ B}$):
$$\text{Number of Pages} = \frac{2^{32}}{2^{12}} = 2^{20}\text{ pages}$$
Assuming each $\text{PTE} = 4\text{ Bytes}$:
$$\text{Page Table Size} = 2^{20} \times 4\text{ Bytes} = 4\text{ MB per process}$$

If an OS runs hundreds of active processes, hundreds of megabytes of physical RAM are wasted purely storing page tables. Moreover, because compilers separate code, stack, and heap across a vast sparse logical address range, most of those $2^{20}$ entries are marked invalid/empty.

> [!theorem] The Need for Multi-Level Paging
> Single-level page tables must be allocated contiguously in physical memory. When the table grows to multiple megabytes per process, allocating contiguous physical space for the table itself reintroduces the very contiguous-allocation problems paging was designed to solve. 
> 
> This necessitates **Multi-Level Paging**, where the page table itself is split into pages and dynamically allocated on demand.

---

### 5. Memory Units Conversion Reference

$$\begin{array}{rcl\|rcl} 1\text{ KB} &=& 2^{10}\text{ Bytes} & 1\text{ Kbps} &=& 10^3\text{ bps} \quad (\text{Networking}) \\ 1\text{ MB} &=& 2^{20}\text{ Bytes} & 1\text{ Mbps} &=& 10^6\text{ bps} \quad (\text{Data Rates}) \\ 1\text{ GB} &=& 2^{30}\text{ Bytes} & 1\text{ Gbps} &=& 10^9\text{ bps} \\ 1\text{ TB} &=& 2^{40}\text{ Bytes} & 1\text{ Byte (B)} &=& 8\text{ bits (b)} \end{array}$$

---

## Classroom Practice Problems & Derivations

### Problem Set 1: Basic Address Computation & Verification

#### Question 1.1: Small Memory System Mapping
**Given:**
* Logical Address Space: $LAS = 1024\text{ B}$
* Page Size: $\text{Page Size} = 8\text{ B}$
* Segment of Process Page Table:

| Page No. | Frame No. |
| :---: | :---: |
| $0$ | $3$ |
| $1$ | $6$ |
| $\dots$ | $\dots$ |
| $113$ | $10$ |
| $\dots$ | $\dots$ |
| $127$ | $\dots$ |

1. Find the total number of pages.
2. Find the physical address for Logical Address $LA = 905$.

**Step-by-step Solution:**
1. **Total Number of Pages:**
   $$\text{Number of Pages} = \frac{LAS}{\text{Page Size}} = \frac{1024\text{ B}}{8\text{ B}} = 128\text{ Pages} \quad (\text{Indexed } 0 \text{ to } 127)$$

2. **Compute Page Number and Offset for $LA = 905$:**
   Using integer division and modulo with page size $8$:
   $$\text{Page Number } (p) = 905 \mathbin{/\!/} 8 = 113$$
   $$\text{Offset } (d) = 905 \mathbin{\%} 8 = 1\text{ Byte}$$

3. **Compute Physical Address ($PA$):**
   * From the page table, Page $113$ resides in Frame $10$.
   * $$PA = (\text{Frame Number} \times \text{Frame Size}) + \text{Offset} = (10 \times 8) + 1 = 80 + 1 = \mathbf{81}$$

*(Note: For $LA = 904$, offset is $0$, resulting in $PA = 80$. For $LA = 905$, $PA = 81$. All addresses from $904$ to $911$ map to Page $113$).*

---

#### Question 1.2: Translation with Symbolic Mapping
**Given:**
* Logical Address Space: $LAS = 1024\text{ B}$
* Page Size: $\text{Page Size} = 8\text{ B}$
* Target Logical Address: $LA = 807$
* Page Table maps: $\text{Page } 100 \longrightarrow \text{Frame } 3$

Find the corresponding Physical Address ($PA$).

**Step-by-step Solution:**
1. **Deconstruct $LA = 807$:**
   $$807 = (100 \times 8) + 7$$
   * $\text{Page Number } (p) = 807 \mathbin{/\!/} 8 = 100$
   * $\text{Offset } (d) = 807 \mathbin{\%} 8 = 7$
2. **Translate:**
   * Page $100$ resides in Frame $3$.
   * $$PA = (\text{Frame Number} \times \text{Frame Size}) + \text{Offset} = (3 \times 8) + 7 = 24 + 7 = \mathbf{31}$$

---

### Problem Set 2: Binary Formats and Page Sizing

#### Question 2.1: 8-bit Virtual to 10-bit Physical Address
**Given:**
* Virtual Address: $VA = 8\text{ bits}$
* Physical Address: $PA = 10\text{ bits}$
* Page Size: $2^6\text{ B} = 64\text{ B}$
* Page Table: $[2, 5, 1, 8]$ (where index represents page number)

Compute:
a) Number of pages  
b) Number of frames  
c) Number of entries in page table  
d) Physical Address for $VA = 241$ (via both arithmetic and binary)

**Step-by-step Solution:**
a) **Number of Pages:**
   $$\text{Number of Pages} = \frac{2^{VA\text{ bits}}}{2^{\text{offset bits}}} = \frac{2^8}{2^6} = 2^{8-6} = 2^2 = \mathbf{4\text{ Pages}}$$

b) **Number of Frames:**
   $$\text{Number of Frames} = \frac{2^{PA\text{ bits}}}{2^{\text{offset bits}}} = \frac{2^{10}}{2^6} = 2^{10-6} = 2^4 = \mathbf{16\text{ Frames}}$$

c) **Number of Entries in Page Table:**
   $$\text{Number of Entries} = \text{Number of Pages} = \mathbf{4\text{ Entries}}$$

d) **Translate $VA = 241$:**
* **Arithmetic Method:**
  * $\text{Page Number} = 241 \mathbin{/\!/} 64 = 3$
  * $\text{Offset} = 241 \mathbin{\%} 64 = 49$
  * From Page Table: $\text{Entry}[3] = \text{Frame } 8$
  * $$PA = (8 \times 64) + 49 = 512 + 49 = \mathbf{561}$$

* **Binary Representation Method:**
  * $VA = 241_{10} = 11\,110001_2$
  * Upper $2$ bits: $11_2 = 3$ (Page $3$)
  * Lower $6$ bits: $110001_2 = 49_{10}$ (Offset $49$)
  * Frame number $8 = 1000_2$ ($4$ bits)
  * Concatenate frame bits with offset bits:
    $$PA = 1000\,110001_2 = 512 + 32 + 16 + 1 = \mathbf{561_{10}}$$

---

#### Question 2.2: Memory Hierarchy with Large Address Bounds
**Given:**
* Logical Address Space: $LAS = 1\text{ TB} = 2^{40}\text{ Bytes}$
* Number of Pages: $2^{16}$
* Number of Frames: $2^{11}$

Find:
a) Physical Address Space ($PAS$) size  
b) Physical Address ($PA$) bit-width

**Step-by-step Solution:**
1. **Find Page Size:**
   $$\text{Page Size} = \frac{LAS}{\text{Number of Pages}} = \frac{2^{40}\text{ Bytes}}{2^{16}} = 2^{24}\text{ Bytes} \implies \text{Offset } (k) = 24\text{ bits}$$
2. **Find PAS Size:**
   $$\text{Frame Size} = \text{Page Size} = 2^{24}\text{ Bytes}$$
   $$PAS = (\text{Number of Frames}) \times (\text{Frame Size}) = 2^{11} \times 2^{24}\text{ Bytes} = \mathbf{2^{35}\text{ Bytes} = 32\text{ GB}}$$
3. **Physical Address Width:**
   $$m = \log_2(PAS) = \mathbf{35\text{ bits}}$$

---

### Problem Set 3: Decimal & Hexadecimal Translation Mechanics

#### Question 3.1: Complete Lookup from Linear Table
**Given:**
* Page Size $= 1024\text{ Bytes}$
* Page Table:

| Index ($p$) | 0 | 1 | 2 | 3 | 4 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Frame ($f$)** | 3 | 10 | 9 | 2 | 0 |

Compute:
a) Physical Address for $VA = 697$  
b) Physical Address for $VA = 1024$  
c) Logical Address corresponding to Physical Address $PA = 2075$

**Step-by-step Solution:**
* **a) $VA = 697$:**
  * $\text{Page Number} = 697 \mathbin{/\!/} 1024 = 0$
  * $\text{Offset} = 697 \mathbin{\%} 1024 = 697$
  * $\text{Frame} = \text{Table}[0] = 3$
  * $$PA = (3 \times 1024) + 697 = 3072 + 697 = \mathbf{3769}$$

* **b) $VA = 1024$:**
  * $\text{Page Number} = 1024 \mathbin{/\!/} 1024 = 1$
  * $\text{Offset} = 1024 \mathbin{\%} 1024 = 0$
  * $\text{Frame} = \text{Table}[1] = 10$
  * $$PA = (10 \times 1024) + 0 = \mathbf{10240}$$

* **c) Reverse Translation for $PA = 2075$:**
  * $\text{Frame Number} = 2075 \mathbin{/\!/} 1024 = 2$
  * $\text{Offset} = 2075 \mathbin{\%} 1024 = 27$
  * Scan page table for Frame value $2$: found at Page Index $3$ ($\text{Table}[3] = 2$).
  * $$LA = (\text{Page Number} \times \text{Page Size}) + \text{Offset} = (3 \times 1024) + 27 = 3072 + 27 = \mathbf{3099}$$

---

#### Question 3.2: 12-bit VA System Entry Bounds
**Given:** A single-level paging system has:
* Virtual Address: $12\text{ bits}$
* Physical Address: $24\text{ bits}$
* Page Size: $2^8\text{ Bytes} = 256\text{ Bytes}$

Find the maximum possible number of page table entries.

**Step-by-step Solution:**
* Number of page table entries is determined solely by the number of pages in the logical address space:
  $$\text{Offset bits } (k) = 8$$
  $$\text{Page bits } (p) = 12 - 8 = 4\text{ bits}$$
  $$\text{Max Page Table Entries} = 2^p = 2^4 = \mathbf{16\text{ Entries}}$$

---

#### Question 3.3: Hexadecimal Paging System Lookups
**Given:**
* Virtual Address ($VA$) = Physical Address ($PA$) = $32\text{ bits}$
* Page Size = Frame Size = $2^{12}\text{ Bytes} = 4\text{ KB}$
* Segment of Process Page Table:

| Page Index (Hex) | Frame Number (Hex) |
| :---: | :---: |
| `0x00000` | `0x005BB` |
| `0x00001` | `0x00249` |
| `0x00002` | `0x0013F` |
| `0x00003` | `0x009CE` |
| `0x00004` | `0x00B0D` |

Evaluate:
a) Physical Address for $LA = \text{0x00001A60}$  
b) Physical Address for $LA = \text{0x00005114}$  
c) Logical Address corresponding to $PA = \text{0x009CE41C}$  
d) Translation status for $PA = \text{0x00000BD7}$

**Step-by-step Solution:**
* **Bit Partitioning in Hex:**
  * Offset $= 12\text{ bits} = \frac{12}{4} = 3\text{ hex nibbles}$ (least significant $3$ characters).
  * Page / Frame Number $= 32 - 12 = 20\text{ bits} = \frac{20}{4} = 5\text{ hex nibbles}$.

* **a) $LA = \text{0x00001A60}$:**
  * Page Number $= \text{0x00001}$
  * Offset $= \text{0xA60}$
  * From Table: Page `0x00001` maps to Frame `0x00249`.
  * Preserving offset:
    $$PA = \mathbf{\text{0x00249A60}}$$

* **b) $LA = \text{0x00005114}$:**
  * Page Number $= \text{0x00005}$
  * Offset $= \text{0x114}$
  * Page `0x00005` is not listed in the table entries provided.
  * **Result:** **Translation not possible with given information** (triggers a Page Fault if page is non-resident).

* **c) $PA = \text{0x009CE41C}$:**
  * Frame Number $= \text{0x009CE}$
  * Offset $= \text{0x41C}$
  * Reverse lookup in table: Frame `0x009CE` is mapped to Page `0x00003`.
  * Preserving offset:
    $$LA = \mathbf{\text{0x0000341C}}$$

* **d) $PA = \text{0x00000BD7}$:**
  * Frame Number $= \text{0x00000}$
  * Scanning the page table reveals no page currently mapped to Frame `0x00000`.
  * **Result:** **Reverse translation not possible** (frame is either free, operating system reserved, or unmapped).

---

### Problem Set 4: Comprehensive GATE Exam Questions

#### Question 4.1: Page Table Size with Explicit PTE Width
**Problem:**
A system features:
* $LA = 256\text{ KB}$
* $PA = 64\text{ KB}$
* $\text{Page Size} = 4\text{ KB}$
* $\text{PTE Size} = 2^B\text{ Bytes}$

Find:
a) Number of pages  
b) Number of bits in page offset  
c) Number of frames  
d) Total size of the page table

**Step-by-step Solution:**
* $LAS = 256\text{ KB} = 2^{18}\text{ Bytes} \implies n = 18\text{ bits}$
* $PAS = 64\text{ KB} = 2^{16}\text{ Bytes} \implies m = 16\text{ bits}$
* $\text{Page Size} = 4\text{ KB} = 2^{12}\text{ Bytes} \implies k = 12\text{ bits}$

a) **Number of Pages:**
   $$\text{Number of Pages} = \frac{2^{18}}{2^{12}} = 2^6 = \mathbf{64\text{ Pages}}$$

b) **Page Offset Bits:**
   $$k = \mathbf{12\text{ bits}}$$

c) **Number of Frames:**
   $$\text{Number of Frames} = \frac{2^{16}}{2^{12}} = 2^4 = \mathbf{16\text{ Frames}}$$

d) **Size of Page Table:**
   $$\text{Page Table Size} = (\text{Number of Entries}) \times (\text{PTE Size}) = 2^6 \times 2^B\text{ Bytes} = \mathbf{2^{6+B}\text{ Bytes}}$$

---

#### Question 4.2: GATE 2002 Architecture Problem
**Problem:**
A computer system employs:
* Virtual Address: $32\text{ bits}$
* Physical Memory: $64\text{ MB}$
* Page Size: $4\text{ KB}$
* $\text{PTE Size} = \text{Bits strictly required to index all physical frames}$

Calculate:
1. Total number of PTEs
2. Total number of physical frames
3. Minimum PTE size
4. Total Page Table Size

**Step-by-step Solution:**
1. **Total Number of PTEs:**
   $$\text{Number of Pages} = \frac{2^{32}\text{ Bytes}}{4\text{ KB}} = \frac{2^{32}}{2^{12}} = 2^{20} = \mathbf{1{,}048{,}576\text{ Entries}}$$

2. **Total Number of Frames:**
   $$PAS = 64\text{ MB} = 2^{26}\text{ Bytes}$$
   $$\text{Number of Frames} = \frac{2^{26}\text{ Bytes}}{2^{12}\text{ Bytes}} = 2^{14} = \mathbf{16{,}384\text{ Frames}}$$

3. **Bits required for Frame Number in PTE:**
   $$\text{Frame bits} = \log_2(2^{14}) = \mathbf{14\text{ bits}}$$

4. **Page Table Size:**
   * **In raw bits:**
     $$\text{Size} = 2^{20} \times 14\text{ bits} = 14 \times 2^{20}\text{ bits} = \mathbf{14\text{ Mbits}}$$
   * **In byte-aligned storage (rounded up to $2\text{ Bytes} = 16\text{ bits}$ per entry):**
     $$\text{Size} = 2^{20} \times 2\text{ Bytes} = \mathbf{2\text{ MB}}$$

---

#### Question 4.3: GATE 2015 Set-2 Architecture Problem
**Problem:**
A 64-bit computing architecture utilizes:
* Virtual Address: $40\text{ bits}$
* Page Size: $16\text{ KB}$
* Page Table Entry Size: $48\text{ bits}$

Calculate the total size of the process page table.

**Step-by-step Solution:**
1. **Find Page Offset and Page Count:**
   $$\text{Page Size} = 16\text{ KB} = 16 \times 2^{10}\text{ Bytes} = 2^{14}\text{ Bytes} \implies k = 14\text{ bits}$$
   $$\text{Number of Pages} = \frac{2^{40}}{2^{14}} = 2^{26}\text{ Pages}$$

2. **Calculate Total Page Table Size:**
   $$\text{Page Table Entries} = 2^{26}\text{ entries}$$
   $$\text{PTE Size} = 48\text{ bits} = \frac{48}{8}\text{ Bytes} = 6\text{ Bytes}$$
   $$\text{Size} = 2^{26} \times 48\text{ bits} = 2^{26} \times 6\text{ Bytes} = 6 \times 2^{26}\text{ Bytes}$$
   $$6 \times 2^{26}\text{ Bytes} = 6 \times 64\text{ MB} = \mathbf{384\text{ MB}}$$

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->
3.1
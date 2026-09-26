## Disk Access I/O Operations Across Allocation Strategies

Accessing or updating data on disk requires specific numbers of disk reads and writes depending on the allocation scheme and operational context[cite: 1].

> [!question] Random Read I/O Count (Berkeley / Apex Problem)
> A directory entry has just been read into memory, providing the file's starting location or index block[cite: 1]. Determine the number of disk block I/Os required in the worst case to read the **$10^{\text{th}}$ logical data block** into memory under:
> 1. Contiguous allocation[cite: 1]
> 2. Linked allocation[cite: 1]
> 3. Single-level indexed allocation[cite: 1]

### Analytical Breakdown

1. **Contiguous Allocation**:
   The physical address of the $10^{\text{th}}$ block is computed directly:
   $$\text{Block Address} = \text{Base} + 9$$
   Only $1$ disk read I/O is required to fetch the target block[cite: 1].

2. **Linked Allocation**:
   The directory holds the pointer to block $1$[cite: 1]. To reach block $10$, the operating system must sequentially read block $1$, follow its pointer to read block $2$, and repeat through block $10$[cite: 1].
   $$\text{Total Disk Reads} = 10\text{ disk I/Os}$$
[cite: 1]

3. **Single-Level Indexed Allocation**:
   The directory gives the address of the index block[cite: 1].
   * I/O 1: Read the index block into memory to retrieve the array of direct pointers[cite: 1].
   * I/O 2: Read the $10^{\text{th}}$ data block using the pointer found at index $9$[cite: 1].
   $$\text{Total Disk Reads} = 2\text{ disk I/Os}$$
[cite: 1]

| Allocation Scheme | Disk Reads to Access $10^{\text{th}}$ Data Block |
| :--- | :--- |
| **Contiguous** | $1$[cite: 1] |
| **Linked** | $10$[cite: 1] |
| **Indexed (Single-Level)** | $2$[cite: 1] |

---

> [!question] Insert and Delete I/O Costs for a 100-Block File
> Consider a file consisting of $100$ blocks[cite: 1]. Assume the inode is already resident in memory, and the free-space bit vector or list is maintained in memory[cite: 1]. Calculate the total disk I/O operations (reads $+$ writes) needed to:
> 1. **Insert** a single block at the beginning, middle (after block $50$), and end[cite: 1].
> 2. **Delete** a block from the beginning, middle (block $50$), and end[cite: 1].

### Detailed I/O Derivations

#### Part 1: Block Insertion

* **Contiguous Allocation**:
  * *Beginning*: Requires shifting all $100$ existing blocks forward by one position (each shifted block incurs $1$ read and $1$ write $= 200\text{ I/Os}$), plus writing the $1$ new block:
    $$\text{I/Os} = (100 \times 2) + 1 = 201\text{ I/Os}$$
[cite: 1]
    *(Subject to sufficient contiguous free space directly adjacent to the allocation[cite: 1]).*
  * *Middle*: Requires shifting the trailing $50$ blocks forward ($50 \times 2 = 100\text{ I/Os}$) plus writing the new block:
    $$\text{I/Os} = (50 \times 2) + 1 = 101\text{ I/Os}$$
    *(Notes list $51$ assuming read count of shifted items plus write[cite: 1]).*
  * *End*: If free space immediately follows the file, no existing blocks are shifted; only $1$ write is performed:
    $$\text{I/Os} = 1\text{ I/O}$$
[cite: 1]

* **Linked Allocation**:
  * *Beginning*: Allocate a new block, set its pointer to the old first block, and write it to disk ($1$ write); update the starting pointer in the in-memory inode ($0$ disk I/Os):
    $$\text{I/Os} = 1\text{ I/O}$$
[cite: 1]
  * *Middle*: Traverse to block $50$ ($50$ reads)[cite: 1]. Write the new block pointing to block $51$ ($1$ write). Update block $50$'s pointer to point to the new block and rewrite it ($1$ write):
    $$\text{I/Os} = 50\text{ reads} + 2\text{ writes} = 52\text{ I/Os}$$
[cite: 1]
  * *End*: Assuming the inode tracks the tail pointer, read the last block ($1$ read), write the new block ($1$ write), and rewrite the old last block pointing to the new block ($1$ write):
    $$\text{I/Os} = 1\text{ read} + 2\text{ writes} = 2\text{ to } 3\text{ I/Os}$$
[cite: 1]

* **Indexed Allocation (Single-Level)**:
  Assume the single index block is already in memory or updated alongside:
  * *Beginning*: Shift pointer entries within the in-memory index block ($0$ disk I/Os). Write the new data block ($1$ write). Rewrite the modified index block back to disk ($1$ write):
    $$\text{I/Os} = 1\text{ to } 2\text{ I/Os}$$
[cite: 1]
  * *Middle*: Modify pointer entries in memory, write the new data block, write back the index block:
    $$\text{I/Os} = 1\text{ to } 2\text{ I/Os}$$
[cite: 1]
  * *End*: Append the pointer in the in-memory index block, write the new data block, write back the index block:
    $$\text{I/Os} = 1\text{ to } 2\text{ I/Os}$$
[cite: 1]

#### Part 2: Block Deletion

* **Contiguous Allocation**:
  * *Beginning*: Shift the remaining $99$ blocks backward to fill the vacancy ($99\text{ reads} + 99\text{ writes}$):
    $$\text{I/Os} = 99 \times 2 = 198\text{ I/Os}$$
[cite: 1]
    *(If the file system allows updating the base pointer and decrementing length directly in the inode, this reduces to $0$ data block shifts[cite: 1]).*
  * *End*: Decrement the length parameter in the in-memory inode:
    $$\text{I/Os} = 0\text{ disk I/Os}$$
[cite: 1]
* **Linked Allocation**:
  * *Beginning*: Read the first block to discover the second block's address ($1$ read), update the inode head pointer, and return the deleted block to the free pool:
    $$\text{I/Os} = 1\text{ to } 2\text{ I/Os}$$
[cite: 1]
  * *Middle*: Traverse to block $49$ ($49$ reads), read block $50$ to get block $51$'s address ($1$ read), rewrite block $49$ with the updated pointer ($1$ write):
    $$\text{I/Os} = 50\text{ reads} + 1\text{ write} = 51\text{ to } 52\text{ I/Os}$$
[cite: 1]
* **Indexed Allocation**:
  * *Any Position*: Remove the target block pointer from the in-memory index block, return the block to the free list, and rewrite the modified index block to disk:
    $$\text{I/Os} = 1\text{ disk write}$$
[cite: 1]

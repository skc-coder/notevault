## Linked Allocation and the File Allocation Table (FAT)

### Pure Linked Allocation

In linked allocation, each file is organized as a linked list of disk blocks scattered across the disk.

* **Disk Block Structure**: Each physical disk block contains data bytes and a pointer to the next disk block in the chain.
* **Inode Structure**: The inode stores only two pointers: a pointer to the first block (`Start`) and a pointer to the terminal block (`End`), or just the start pointer.
* **End-of-File**: The final data block stores an explicit End-of-File marker (such as `EOF` or `NULL`) in its pointer field.

#### Trade-offs

* **Advantages**:
  * Completely eliminates external fragmentation; any free block satisfies an allocation request.
  * Dynamic file growth requires no advance declaration of size.
  * Simple directory implementation.
* **Disadvantages**:
  * **No Direct/Random Access**: Locating logical block $k$ requires traversing the preceding $k-1$ blocks sequentially from disk, causing severe seek latencies.
  * **Large Storage Overhead**: Every physical block sacrifices internal capacity to store the pointer field.
  * **Reliability Risk**: A single corrupt pointer or damaged block breaks the entire remaining file chain.

### File Allocation Table (FAT)

FAT is a variation of linked allocation that moves all block pointers out of the physical data blocks into an in-memory or dedicated disk table.

* **Structure**: A centralized table where every entry corresponds to one physical disk block.
* **Chaining**: Entry $i$ contains the block number of the next block in the file's sequence.
* **Directory / Inode Entry**: Stores only the starting block number of the file.
![[File Allocation - Linked and FAT-1790427722623.webp]]

#### Operational Mechanics and Invariants

* **Pointer Chasing Without Disk I/O**: Following a file chain does not require reading physical data blocks into main memory. Pointer chasing is performed entirely within the FAT.
* **Caching Requirement**: For optimal throughput, the FAT must be cached in RAM.
* **Random Access**: Faster than pure linked allocation because pointer traversal occurs in RAM rather than across mechanical disk sectors, though still slower than contiguous or direct indexed lookups.
* **Large storage overhead** for the FAT table

#### Trade-offs
- Worse sequentiality than the normal linked implemntation
	(sequential mean is there a intepretation logically from going from one data block to next or not)

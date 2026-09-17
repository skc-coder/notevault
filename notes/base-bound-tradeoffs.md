## Trade-off Analysis: Base & Bound Approach

### Advantages
* **Dynamic Relocation:** Processes can be placed in any contiguous chunk of free RAM; the loader merely writes the allocated physical start address into the PCB/Base register.
* **Fast & Inexpensive Hardware Implementation:** Requires only two fast registers (Base, Bound), one comparator ($<$), and one adder ($+$).
* **Low Context Switch Overhead:** Saving and restoring process state requires preserving only two register values (Base and Bound) in the PCB.
* **Protection:** Guarantees isolation between user processes and protects the OS kernel space.

### Disadvantages
* **Contiguous Allocation Requirement:** The entire process must be placed in a single contiguous block of physical RAM.
* **External Fragmentation:** Over time, allocating and deallocating variable-sized contiguous chunks leaves small, unusable holes scattered across physical memory.
* **Entire Process in Memory:** The complete process image must reside entirely in RAM before execution begins (a limitation later eliminated via Demand Paging).
* **Size of process is fixed** hence when size is increased by dynamic memory then costly reallocation needs to be done.

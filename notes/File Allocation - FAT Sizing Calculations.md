## Mathematical Calculations for FAT Architectures

> [!formula] FAT Architecture Bounds
> For a FAT file system with block size $B$, entry width $e$ bits, and partition capacity $S$:
> 1. $\text{Maximum Addressable Blocks} = 2^e$
> 2. $\text{Maximum File System Size} = 2^e \times B$
> 3. $\text{Total FAT Entries} = \frac{\text{Total Disk Size}}{\text{Block Size}}$
> 4. $\text{FAT Table Size} = \text{Total FAT Entries} \times (\text{Entry Size in Bytes})$
> 5. $\text{Usable Data Capacity} = \text{Total Disk Size} - \text{FAT Table Size}$

> [!question] Maximum File System Size with 16-bit FAT Entries
> In a file system using $16$-bit FAT entries and a block size of $512\text{ B}$, determine the maximum addressable file system capacity.

With a $16$-bit entry size, the table can index at most $2^{16}$ distinct blocks:

$$\text{Total Blocks} = 2^{16} = 65{,}536\text{ blocks}$$


Each block contains $512\text{ B} = 2^9\text{ B}$. Therefore:

$$\text{Max FS Size} = 2^{16} \times 2^9\text{ B} = 2^{25}\text{ B} = 32\text{ MB}$$


> [!question] GATE Problem: Usable Data Space in a FAT File System
> Consider a disk of size $100 \times 10^6\text{ B}$ with a block size of $10^3\text{ B}$. The file system uses a FAT architecture where each FAT entry occupies $4\text{ B}$. Calculate the maximum storage available for user data files.

The total number of physical disk blocks is:

$$\text{Total Disk Blocks} = \frac{\text{Disk Size}}{\text{Block Size}} = \frac{100 \times 10^6\text{ B}}{10^3\text{ B}} = 10^5\text{ blocks}$$


Since the FAT must maintain exactly one entry for each physical block:

$$\text{Total Entries} = 10^5\text{ entries}$$


With an entry size of $4\text{ B}$, the storage overhead consumed by the FAT itself is:

$$\text{FAT Size} = 10^5 \times 4\text{ B} = 400 \times 10^3\text{ B} = 0.4 \times 10^6\text{ B}$$


The maximum capacity available for actual data files is the total disk size minus the FAT overhead:

$$\text{Data Capacity} = 100 \times 10^6\text{ B} - (4 \times 10^5\text{ B})$$

$$\text{Data Capacity} = 100 \times 10^6\text{ B} - 0.4 \times 10^6\text{ B} = 99.6 \times 10^6\text{ B}$$


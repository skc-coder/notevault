# Multilevel Inode Data Structure: General Framework & Problem Solution

## 🛠️ General Algorithm for Inode Problems

Follow these steps in exact order to solve any file system inode capacity problem:

### Step 1: Find the Disk Pointer Size
- Calculate total disk blocks:
  $$\text{Total Blocks} = \frac{\text{Disk Size}}{\text{Block Size}}$$
- Calculate block address size (pointer size):
  $$\text{Pointer Size (bits)} = \lceil \log_2(\text{Total Blocks}) \rceil$$
- Convert pointer size to **Bytes** (round up to the nearest whole byte or standard word boundary if required, usually standard byte alignment is assumed):
  $$\text{Pointer Size (Bytes)} = \left\lceil \frac{\text{Pointer Size (bits)}}{8} \right\rceil$$

---

### Step 2: Find Pointer Capacity per Block
- Determine how many disk pointers a single block can hold:
  $$N = \frac{\text{Block Size}}{\text{Pointer Size}}$$

---

### Step 3: Breakdown the Inode Space
- Determine total direct and indirect pointers:
  $$\text{Total Inode Pointer Space} = (\text{Direct Pointers} + \text{Indirect Pointers}) \times \text{Pointer Size}$$
- Find the number of Direct Pointers ($D$):
  $$D = \frac{\text{Inode Pointer Space}}{\text{Pointer Size}} - (\text{Sum of Indirect Pointer Entries})$$

---

### Step 4: Calculate Total Addressable Data Blocks
Sum the total data blocks accessible across all pointer levels:

1. **Direct Blocks:** Address $D$ blocks $\rightarrow D$
2. **Single Indirect (SI):** Addresses $N$ blocks $\rightarrow N$
3. **Double Indirect (DI):** Addresses $N^2$ blocks $\rightarrow N^2$
4. **Triple Indirect (TI):** Addresses $N^3$ blocks $\rightarrow N^3$

$$\text{Total Addressable Blocks} = D + N + N^2 + N^3 + \dots$$

---

### Step 5: Calculate Maximum File Size
$$\text{Max File Size} = \text{Total Addressable Blocks} \times \text{Block Size}$$

---

## 📝 Problem Solution

### Given Data:
- **Disk Size:** $2\text{ TB} = 2^{41}\text{ Bytes}$
- **Block Size:** $512\text{ Bytes} = 2^9\text{ Bytes}$
- **Total Inode Space for Pointers:** $64\text{ Bytes}$
- **Indirect Structures:** 1 Single Indirect block, 1 Double Indirect block, and $D$ Direct blocks

---

### Step-by-Step Calculation:

#### 1. Calculate Block Address/Pointer Size
- $\text{Total Blocks} = \frac{2^{41}\text{ Bytes}}{2^9\text{ Bytes}} = 2^{32}\text{ blocks}$
- $\text{Pointer Size (bits)} = \log_2(2^{32}) = 32\text{ bits}$
- $\text{Pointer Size (Bytes)} = \frac{32}{8} = 4\text{ Bytes}$

#### 2. Calculate Pointers per Block ($N$)
- $N = \frac{\text{Block Size}}{\text{Pointer Size}} = \frac{512\text{ Bytes}}{4\text{ Bytes}} = 128\text{ pointers} = 2^7\text{ pointers}$

#### 3. Determine Number of Direct Pointers ($D$)
- $\text{Total Inode Pointers} = \frac{64\text{ Bytes}}{4\text{ Bytes}} = 16\text{ pointers}$
- Pointers used for indirect blocks = $1\text{ (SI)} + 1\text{ (DI)} = 2\text{ pointers}$
- $\text{Direct Pointers } (D) = 16 - 2 = 14\text{ pointers}$

#### 4. Calculate Total Data Blocks Accessible
- **Direct Pointers:** $14\text{ blocks}$
- **Single Indirect:** $N = 128 = 2^7\text{ blocks}$
- **Double Indirect:** $N^2 = 128^2 = 16,384 = 2^{14}\text{ blocks}$

$$\text{Total Data Blocks} = 14 + 128 + 16,384 = 16,526\text{ blocks}$$

#### 5. Calculate Maximum File Size
$$\text{Max File Size} = 16,526 \times 512\text{ Bytes}$$
$$\text{Max File Size} = 8,461,312\text{ Bytes} \approx 8.46\text{ MB} \text{ (or } 8.0693\text{ MiB)}$$

---

## 🎯 Final Answer
The maximum file size that can be stored in the file system is **$8,461,312\text{ Bytes}$** (or **$8.0693\text{ MiB}$ / $8.46\text{ MB}$**).
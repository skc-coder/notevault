## 1. Endianness Architecture

> [!definition] Endianness
> Endianness dictates byte-level ordering of multi-byte scalar primitives in memory:
> * **Little-Endian:** Least Significant Byte (LSB) stored at lowest memory address.
> * **Big-Endian:** Most Significant Byte (MSB) stored at lowest memory address.

For $32$-bit value `0x12345678` stored at base address `0x00`:

| Architecture | Address `0x00` | Address `0x01` | Address `0x02` | Address `0x03` |
| :--- | :---: | :---: | :---: | :---: |
| **Little-Endian** (x86, ARM) | `0x78` (LSB) | `0x56` | `0x34` | `0x12` (MSB) |
| **Big-Endian** (Network Byte Order) | `0x12` (MSB) | `0x34` | `0x56` | `0x78` (LSB) |

> [!trap] Endianness Applies Only to Scalar Primitives
> Endianness applies solely to bytes within primitive scalars (`int`, `float`, `short`). Array element order is unaffected (`arr[0]` always sits at the lowest physical memory address).

---

## 2. Strings and Memory Segments

```c
// Stack-allocated mutable character array
char str[] = "hello"; 
str[0] = 'H'; // Valid!

// Pointer to string literal in read-only memory (.rodata)
char *ptr = "hello"; 
// ptr[0] = 'H'; // UNDEFINED BEHAVIOR: Segfault (write to read-only section)
```

### Memory Segments Allocation
* **`.rodata` (Text segment):** Houses immutable string literals.
* **`.data` Segment:** Houses initialized global and `static` variables.
* **`.bss` Segment:** Houses uninitialized global and `static` variables (zero-initialized).
* **Stack:** Houses local automatic variables and activation frames.

### Three Ways to Represent Array of Strings
```c
// Method 1: Array of pointers to string literals (.rodata)
const char *p1[3] = {"he", "you", "they"};

// Method 2: 2D rectangular character array (Stack / Data segment)
char p2[3][6] = {"hello", "hole", "world"};

// Method 3: Array of pointers to independent buffers
char buf1[] = "cat", buf2[] = "dog", buf3[] = "fox";
char *p3[3] = {buf1, buf2, buf3};
```

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->

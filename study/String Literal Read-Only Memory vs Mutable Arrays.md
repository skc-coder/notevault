---
title: String Literal Read-Only Memory vs Mutable Arrays
tags:
  - clang
  - c-language
  - strings
  - memory
  - study
---


---

## Code Comparison: Array vs Pointer Initialization

```c
// Stack-allocated mutable character array
char str[] = "hello"; 
str[0] = 'H'; // Valid!

// Pointer to string literal in read-only memory (.rodata)
char *ptr = "hello"; 
// ptr[0] = 'H'; // UNDEFINED BEHAVIOR: Segfault (write to read-only section)
```

---

## Representation Methods for String Arrays

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

## Related Notes
- [[Endianness Architecture & Byte Ordering]]
- [[Process Memory Layout - Segments & Stack]]

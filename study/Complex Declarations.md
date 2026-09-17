---
tags:
  - clang
  - c-language
  - declarations
  - study
---


To parse complex C declarations, start from the identifier and spiral outward clockwise, adhering to operator precedence.

---

## Spiral Parser Token Table

- `[ ]`: Array of...
- `( )`: Function returning...
- `*`: Pointer to...

---

## Declaration Examples

### Example 1: Function Pointer
```c
int (*fp1)(int);
// fp1 is a pointer (*) to a function taking (int) returning int
```

### Example 2: Array of Pointers to Arrays
```c
int (*apa[5])[10];
// apa is an array [5] of pointers (*) to an array [10] of int
```


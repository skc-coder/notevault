---
tags:
  - clang
  - c-language
  - memory-layout
  - study
---


Objects declared with static storage duration (`static` variables and global variables) must be initialized with compile-time constants prior to program execution.

---

## Allowed Initializer Categories

1. **Arithmetic Constant Expressions:** Integer or floating-point literals.
2. **Address Constants:** Pointers to static objects, functions, or string literals, plus or minus integer offset expressions, or null pointer constants.

```c
static int global_arr[100];
static int *ptr = &global_arr[5]; // Valid: Address constant + integer offset
```

---

## Related Notes
- [[Integer Constant Expressions (ICE)]]
- [[Storage Classes - Static & Extern]]
- [[Process Memory Layout - Segments & Stack]]

---
tags:
  - clang
  - c-language
  - operators
  - study
---


The `sizeof` operator yields the size in bytes of its operand.

---

## Key Mechanics

- **Unevaluated Operand:** In standard C (non-VLA), `sizeof` operand expression is **unevaluated** at runtime:
  ```c
  int i = 5;
  sizeof(i++); // i remains 5 (i++ is NOT executed at runtime)
  ```
- **Floating Literals Default:** Floating-point literals default to `double`:
  $$\text{sizeof}(1.3) == 8$$


---
tags:
  - clang
  - c-language
  - undefined-behavior
  - sequence-points
  - study
---
## Unsequenced Scalar Modification Rule

> [!trap] Undefined Behavior Trap
> Modifying a scalar variable more than once between two consecutive sequence points, or reading it to determine both its value and store a new value without an intervening sequence point, results in **Undefined Behavior (UB)**.

---

## Classic Unsequenced UB Code Examples

```c
arr[i] = i++;      // Undefined Behavior: unsequenced modification and access of i
f(i++, i++);       // Undefined Behavior: unsequenced modifications of i
i = ++i + 1;       // Undefined Behavior: multiple unsequenced writes to i
```


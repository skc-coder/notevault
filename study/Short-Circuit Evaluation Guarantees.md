---
title: Short-Circuit Evaluation Guarantees
tags:
  - clang
  - c-language
  - logic
  - sequence-points
  - study
---

# Short-Circuit Evaluation Guarantees

Logical operators in C (`&&`, `||`) evaluate strictly left-to-right and introduce an explicit sequence point between operand evaluations.

---

## Evaluation Guarantees

- **In $E_1 \ \&\&\ E_2$:** $E_1$ is evaluated first. If $E_1 = 0$, $E_2$ is **never** evaluated.
- **In $E_1 \ \|\|\ E_2$:** $E_1$ is evaluated first. If $E_1 \ne 0$, $E_2$ is **never** evaluated.

---

## Execution Traces

### Example 1: `if (i++ && i == 1)`
```c
int i = 1;
if (i++ && i == 1) {
    // Trace:
    // 1. i++ evaluates to 1 (true).
    // 2. Sequence point passed: side effect commits (i becomes 2).
    // 3. Right operand evaluates: i == 1 -> 2 == 1 -> evaluates to 0 (false).
    // Entire condition evaluates to false (0).
}
```

### Example 2: `int result = i++ || j++ || k++;`
```c
int i = 0, j = 1, k = 2;
int result = i++ || j++ || k++;
// 1. i++ evaluates to 0, side effect i=1.
// 2. j++ evaluates to 1, side effect j=2. Expression becomes true.
// 3. k++ is SHORT-CIRCUITED (skipped entirely).
// Final state: i=1, j=2, k=2, result=1.
```

---

## Related Notes
- [[Sequence Points Definition & Canonical Locations]]
- [[Undefined Behavior Between Sequence Points]]

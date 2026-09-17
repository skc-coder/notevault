---
tags:
  - clang
  - c-language
  - arrays
  - pointers
  - study
---


Multidimensional arrays are stored in contiguous flat linear memory in **row-major order** (rightmost index changes most rapidly).

---

## Decay Hierarchy

When a multidimensional array decays, only the outermost dimension is stripped away:
- `int a[5]` decays to `int *`.
- `int a[5][6]` decays to `int (*)[6]` (pointer to an array of 6 integers), **never** `int **`.
- Function parameter headers require all dimensions except the first:
  ```c
  void process(int arr[][6]); // Valid parameter decay prototype
  ```

---

## Linear Offset Calculation

$$\text{Address of } arr[i][j] = \text{Base} + (i \cdot N + j) \cdot \text{sizeof}(\text{element})$$

---

## Related Notes
- [[Array Decay Rule & Exceptions]]
- [[Function Pointers & Canonical Invocation]]
- [[Complex Declarations & Clockwise Spiral Rule]]

---
title: Array Decay Rule & Exceptions
tags:
  - clang
  - c-language
  - arrays
  - pointers
  - study
---


> [!definition] Array Decay Rule
> In almost all value contexts and expressions, an expression of array type `T[N]` automatically converts (**decays**) into a pointer to its first element:
> $$\text{Array of type } T[N] \xrightarrow{\text{decay}} \text{Pointer of type } T*$$

---

## The Three Exceptions to Array Decay

1. **Operand of `sizeof`:** `sizeof(arr)` yields total memory footprint: $N \times \text{sizeof}(T)$.
2. **Operand of Unary `&` (Address-Of):**
   - `arr` decays to `T*` (pointer to first element).
   - `&arr` yields a pointer to the **entire array block**, type `T (*)[N]`.
   - Stride difference: `arr + 1` advances by $\text{sizeof}(T)$; `&arr + 1` advances by $N \times \text{sizeof}(T)$.
3. **String Literal Initialization:** `char str[] = "hello";` initializes array memory directly.

---

## Related Notes
- [[Pointer Basics & Addressability]]
- [[Array Indexing & Pointer Arithmetic]]
- [[Multidimensional Array Decay & Pointer Types]]

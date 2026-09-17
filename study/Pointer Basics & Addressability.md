---
tags:
  - clang
  - c-language
  - pointers
  - study
---


A pointer variable stores the memory address of an object. Address size is uniform across compilation targets ($4$ bytes on 32-bit systems, $8$ bytes on 64-bit systems).

> [!property] Uniformity of Pointer Sizing
> $$\text{sizeof}(\text{int}*) = \text{sizeof}(\text{char}*) = \text{sizeof}(\text{double}*) = \text{sizeof}(\text{void}*) = 8 \text{ bytes (64-bit)}$$

---

## Non-Addressable Operands

> [!trap] Unary Address-Of Restrictions
> The unary address-of operator `&` requires an addressable lvalue. It is a compile-time error to apply `&` to literal constants (`&125`), expressions (`&(x + y)`), or `register` variables.

---

## Related Notes
- [[Array Decay Rule & Exceptions]]
- [[Array Indexing & Pointer Arithmetic]]
- [[Sizeof Operator Mechanics]]

---
title: Bit-Width Extensions & Sign vs Zero Extension
tags:
  - clang
  - c-language
  - type-conversion
  - bit-manipulation
  - study
---


When converting a narrower integer type to a wider integer type (widening conversion), numeric value preservation is guaranteed. However, the mechanism used to fill upper bits depends on the operand source type.

> [!property] Extension Invariant
> Extension mechanism is determined **purely by the source variable type (RHS)**, never by the destination variable type (LHS).

---

## Extension Rules

1. **Zero-Extension (Source is `unsigned`):** High-order bit positions are padded exclusively with zeroes (`0`).
2. **Sign-Extension (Source is `signed`):** High-order bit positions are filled by replicating the source's Most Significant Bit (MSB).

---

## Code Examples & Case Studies

### Example 1: Signed Source Widening
```c
short int x = 9;          // 16-bit: 0000 0000 0000 1001 (MSB = 0)
int y = x;                // 32-bit: 00000000 00000000 00000000 00001001 (Padded with 0s)

short int x_neg = -9;     // 16-bit: 1111 1111 1111 0111 (MSB = 1)
unsigned int y_u = x_neg; // 32-bit: 11111111 11111111 11111111 11110111
                          // Sign-extended because source (short int) is SIGNED!
```

### Example 2: Unsigned Source Assigned to Signed Destination
```c
unsigned short x = -9;    // Value is 65527: 1111 1111 1111 0111
int y = x;                // Source is UNSIGNED -> Padded with zeros:
                          // 00000000 00000000 11111111 11110111 = 65527
```

---

## Related Notes
- [[Two's Complement Fundamentals & Weight Method]]
- [[Integer Promotion Rules in C]]
- [[Narrowing & Truncation Mechanics]]
- [[C Integer Conversion & Printf Formatting Case Studies]]

---
tags:
  - clang
  - c-language
  - endianness
  - memory
  - study
---


> [!definition] Endianness
> Endianness dictates byte-level ordering of multi-byte scalar primitives in memory:
> - **Little-Endian:** Least Significant Byte (LSB) stored at lowest memory address.
> - **Big-Endian:** Most Significant Byte (MSB) stored at lowest memory address.

---

## Memory Byte Layout Comparison

For $32$-bit value `0x12345678` stored at base address `0x00`:

| Architecture | Address `0x00` | Address `0x01` | Address `0x02` | Address `0x03` |
| :--- | :---: | :---: | :---: | :---: |
| **Little-Endian** (x86, ARM) | `0x78` (LSB) | `0x56` | `0x34` | `0x12` (MSB) |
| **Big-Endian** (Network Byte Order) | `0x12` (MSB) | `0x34` | `0x56` | `0x78` (LSB) |

> [!trap] Endianness Applies Only to Scalar Primitives
> Endianness applies solely to bytes within primitive scalars (`int`, `float`, `short`). Array element order is unaffected (`arr[0]` always sits at the lowest physical memory address).

---

## Related Notes
- [[String Literal Read-Only Memory vs Mutable Arrays]]
- [[Process Memory Layout - Segments & Stack]]

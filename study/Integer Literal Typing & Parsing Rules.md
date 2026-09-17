---
title: Integer Literal Typing & Parsing Rules
tags:
  - clang
  - c-language
  - literal-constants
  - study
---


When an integer constant is written in C code without explicit type suffixes, the compiler assigns it the first type from the standard hierarchy capable of representing its value:

$$\text{int} \longrightarrow \text{long int} \longrightarrow \text{long long int}$$

The internal memory representation of a literal depends strictly on its constant properties and suffixes, **not** on the target variable type to which it is assigned.

---

## Literal Suffixes Matrix

To enforce specific bit-widths and signedness directly on literal constants:

| Suffix | Resulting Type |
| :--- | :--- |
| `u` / `U` | `unsigned int` |
| `l` / `L` | `long int` |
| `ll` / `LL` | `long long int` |
| `ull` / `ULL` | `unsigned long long int` |

---

## Lexical Parsing Trap: Unary Negation on Literals

> [!trap] Unary Minus Parsing
> In C, a negative literal like `-42` is **not** a single standalone token. 
> 
> The compiler parses `42` as a positive integer constant first, and subsequently applies the unary negation operator (`-`) via two's complement.

---

## Related Notes
- [[Integer Promotion Rules in C]]
- [[Bit-Width Extensions & Sign vs Zero Extension]]
- [[Narrowing & Truncation Mechanics]]

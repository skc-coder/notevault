---
tags:
  - clang
  - c-language
  - constant-expressions
  - study
---


An Integer Constant Expression (ICE) is an expression of integer type that must evaluate at compile time without invoking runtime side effects or library routines.

---

## Mandatory ICE Contexts

1. `case` label values in `switch` statements.
2. Bit-field widths in `struct` definitions.
3. Enumerator initializers (`enum`).
4. Compile-time static array dimensions (file-scope arrays).

---

## Grammar Restrictions on Casts

C allows casts of arithmetic types to integer types inside an ICE, but syntax rules are strictly enforced:

```c
(int)3.3   // Valid ICE: Casts floating constant literal to integer at compile time
(int)+3.3  // Invalid ICE under strict C grammar: unary operator inside a cast
```

---

## `const` in C vs `const` in C++

> [!trap] `const` Qualifier Discrepancy
> - In **C**, qualifying an object with `const` (e.g., `const int n = 5;`) creates a **read-only variable**, **not** an Integer Constant Expression. Consequently:
>   - `int arr[n];` at file scope causes a compilation error.
>   - `int arr[n];` at local scope defines a C99 Variable Length Array (VLA), not a fixed-size static array.
> - In **C++**, a `const` variable initialized with a compile-time constant is treated natively as an ICE.


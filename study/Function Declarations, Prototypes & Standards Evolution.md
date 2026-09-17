---
title: Function Declarations, Prototypes & Standards Evolution
tags:
  - clang
  - c-language
  - functions
  - study
---


A function declaration introduces the function name and its signature (parameter types and return type).

---

## Parameter Decay & Prototype Rules

- Parameter names in prototypes are optional (`int add(int, int);`).
- **Array Parameter Decay:** An array parameter in a function header automatically decays into a pointer:
  $$\text{void foo(int arr[])} \iff \text{void foo(int *arr)}$$
- **Function Parameter Decay:** A function parameter decays into a pointer to a function:
  $$\text{void bar(void f(void))} \iff \text{void bar(void (*f)(void))}$$

---

## Empty Parameter List: `f()` vs `f(void)`

> [!trap] Prototype Standards Discrepancy
> - **Prior to C23:** An empty parameter list `int f();` means the function takes an **unspecified number of arguments** (not a zero-argument prototype). To enforce zero arguments, write `int f(void);`.
> - **C23 Standard:** `int f()` is now strictly equivalent to `int f(void)`, taking zero arguments.

---

## Return Types & `main` Function Rules

- **Implicit `int` Rule (Pre-C99):** Omitted return type defaulted to `int`. Outlawed in C99+.
- **Return Semantics of `main`:**
  - In hosted C, `main` must return `int`.
  - **C99+:** Reaching `}` in `main` implicitly performs `return 0;`.

---

## Related Notes
- [[Function Scoping & Definition Rules]]
- [[Variadic Printf Argument Pipeline]]

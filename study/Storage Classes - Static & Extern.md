---
tags:
  - clang
  - c-language
  - storage-classes
  - linkage
  - study
---


---

## The `static` Storage Class

- **Scope:** Block scope (inside a function) or file scope (outside all functions).
- **Lifetime:** Spans the entire lifecycle of the program.
- **Initialization:** Initialized exactly **once** prior to runtime in the data segment.
- **Default Value:** Zero-initialized (`0`, `0.0`, or `NULL`).

> [!property] Static Variable Initializer Rules
> - In standard C (prior to C23), static variables must be initialized strictly with **constant expressions**.
> - In **C23**, block-scope `static` variables can be initialized with non-constant expressions.

---

## `extern` Storage Class & Linkage Rules

> [!definition] Linkage Classification
> - **External Linkage (`extern`):** Accessible across all translation units (`.c` files) comprising the program.
> - **Internal Linkage (`static` at file scope):** Restricted strictly to the single translation unit.

### Pure Declaration vs Definition
- `extern int var;` is a **pure declaration** (allocates no memory).
- `int var;` (at file scope) or `int var = 10;` is a **definition** allocating memory.

> [!trap] Linker Failure with Unresolved `extern`
> Declaring a variable `extern` suppresses compiler errors in the current module, but if no definition exists across any linked module when accessed, the **Linker fails**.


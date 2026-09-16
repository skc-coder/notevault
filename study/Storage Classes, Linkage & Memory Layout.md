## 1. Storage Classes Matrix

C specifies four core storage classes: `auto`, `register`, `static`, and `extern`.

| Storage Class | Keyword | Storage Location | Scope | Lifetime | Default Value | Linkage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Automatic** | `auto` | Runtime Stack | Block scope | Block entry to exit | Garbage (Indeterminate) | None |
| **Register** | `register` | CPU Register / Stack | Block scope | Block entry to exit | Garbage (Indeterminate) | None |
| **Static Local**| `static` | Data Segment | Block scope | Entire execution | `0` | None |
| **Static Global**| `static` | Data Segment | File scope | Entire execution | `0` | Internal |
| **External** | `extern` | Data Segment | File / Block | Entire execution | `0` | External |

> [!trap] The `register` Storage Class Restrictions
> Using the unary address-of operator `&` on a `register` variable triggers a **compile-time error**, regardless of whether the compiler honored the register placement.

---

## 2. The `static` Storage Class

* **Scope:** Block scope (inside a function) or file scope (outside all functions).
* **Lifetime:** Spans the entire lifecycle of the program.
* **Initialization:** Initialized exactly **once** prior to runtime (at compile/load time) in the data segment.
* **Default Value:** Automatically zero-initialized (`0`, `0.0`, or `NULL`).

> [!property] Static Variable Initializer Requirements
> * In standard C (prior to C23), static variables must be initialized strictly with **constant expressions**.
> * In **C23**, block-scope `static` variables can be initialized with non-constant expressions.

---

## 3. `extern` Storage Class and Linkage Pitfalls

> [!definition] Linkage
> * **External Linkage (`extern`):** Accessible across all translation units (object files) comprising the entire program.
> * **Internal Linkage (`static` at file scope):** Restricted strictly to the single translation unit (`.c` file).

### Pure Declaration vs. Definition
* `extern int var;` is a **pure declaration** (allocates no memory).
* `int var;` (at file scope) or `int var = 10;` is a **definition** allocating memory.

> [!trap] Linker Errors with Unresolved `extern`
> Declaring a variable as `extern` suppresses compiler errors inside the current module, but if no definition exists across any linked translation unit when the variable is accessed, the **Linker fails**.

---

## 4. Process Memory Layout

A compiled program binary is organized into runtime memory segments relative to hardware base pointers:

| Memory Segment | Growth Direction | Stored Data & Characteristics |
| :--- | :---: | :--- |
| **Code / Text Segment** | Fixed | Compiled read-only machine instructions. |
| **Data Segment (.data / .bss)** | Fixed | Global and `static` variables initialized at startup. |
| **Heap Segment** | Grows Upward ($\uparrow$) | Dynamic memory allocated at runtime via `malloc` / `calloc`. |
| **Stack Segment** | Grows Downward ($\downarrow$) | Activation records (stack frames), local `auto` variables, and return addresses. |

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->

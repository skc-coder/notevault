## 1. Function Declarations, Prototypes, and Standards Evolution

A function declaration introduces the function name and its signature (parameter types and return type).

> [!definition] Function Signature & Parameter Decay
> * Parameter names in prototypes are purely optional (e.g., `int add(int, int);`).
> * **Array parameter decay:** An array parameter in a function header automatically decays into a pointer:
>   $$\text{void foo(int arr[])} \iff \text{void foo(int *arr)}$$
> * **Function parameter decay:** A function parameter decays into a pointer to a function:
>   $$\text{void bar(void f(void))} \iff \text{void bar(void (*f)(void))}$$

> [!trap] Empty Parameter List: `f()` vs. `f(void)`
> * **Prior to C23:** An empty parameter list in a declaration `int f();` means the function takes an **unspecified number of arguments** (it is *not* a prototype for zero arguments). To enforce zero arguments, write `int f(void);`.
> * **C23 Standard:** `int f()` is now strictly equivalent to `int f(void)`, taking zero arguments.

### Historical Evolution of Return Types and `main`
* **Implicit `int` Rule (Pre-C99):** If no return type was explicitly specified, the compiler assumed `int` by default. C99 and later standards outlawed implicit `int`.
* **Return Semantics of `main`:**
  * In standard-compliant hosted C, `main` must return `int`.
  * **C99+ Standards:** Reaching `}` in `main` implicitly performs `return 0;`.

---

## 2. Function Scoping & Definition Rules

> [!property] Function Definition vs. Declaration Scope
> * **Function Definitions:** Must always reside at file/global scope. Standard C **does not support nested functions** (defining a function inside the body of another function is illegal).
> * **Function Declarations:** Can occur inside any local block scope. The declaration makes the function visible strictly within that block scope.

---

## 3. Variadic `printf` Arguments Pipeline

Arguments passed to variadic functions like `printf` undergo default argument promotions: types narrower than `int` (`char`, `short`) are promoted to `int` (or `unsigned int`).

`printf` does not inspect the original variable's source type; it simply decodes the promoted bit pattern sitting in the CPU register or stack frame according to the provided format specifier (`%d`, `%u`, etc.).

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->

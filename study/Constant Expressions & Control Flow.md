## 1. Syntax Traps: The Dangling `else` Ambiguity

> [!property] Dangling Else Resolution Invariant
> In nested branching structures lacking explicit compound blocks (`{}`), an `else` clause binds syntactically to the **closest preceding un-paired `if`** within the same block scope.

```c
if (condition1)
    if (condition2)
        action_a();
else
    action_b(); // Belongs to 'if (condition2)', NOT 'if (condition1)'!
```

---

## 2. Constant Expressions in C

A constant expression is an expression that can be fully evaluated during translation (compile time) or program loading, rather than dynamically at runtime. C distinguishes three main classes:

### Category 1: Integer Constant Expressions (ICE)
An expression of integer type that must evaluate at compile time without invoking runtime side effects or library routines.
* **Mandatory contexts:** Case label values in `switch` blocks, bit-field widths in structs, enumerator initializers, and compile-time static array dimensions.
* **Grammar restrictions on casts:** C allows casts of arithmetic types to integer types inside an ICE, but the syntax is strictly validated:

```c
(int)3.3   // Valid ICE: Casts floating constant literal to integer at compile time
(int)+3.3  // Invalid ICE under strict C standard grammar: unary operator inside a cast
```

> [!trap] `const` in C vs. `const` in C++
> * In **C**, qualifying an object with `const` (e.g., `const int n = 5;`) creates a **read-only variable**, not an Integer Constant Expression. Consequently, `int arr[n];` at file scope causes a compilation error, and in local scope defines a C99 Variable Length Array (VLA), not a fixed-size array.
> * In **C++**, a `const` variable initialized with a compile-time constant is treated as an ICE.

### Category 2: Static Initializers (Address Constants & Arithmetic Constants)
Objects declared with static storage duration (`static` variables and global variables) must be initialized with compile-time constants:
1. Arithmetic constant expressions (integer or floating-point literals).
2. Address constants: pointers to static objects, functions, or string literals, plus or minus integer offset expressions, or null pointer constants.

```c
static int global_arr[100];
static int *ptr = &global_arr[5]; // Valid: Address constant + offset
```

### Category 3: Floating-Point Constant Expressions & Runtime Traps
Floating-point arithmetic evaluated inside static or global initializers is resolved by the compiler at translation time according to IEEE 754 rules and does not raise runtime hardware exceptions or traps.

```c
static float lol = 0.0f / 0.0f; // Evaluated at compile time: assigns NaN (No runtime trap/signal)
```

However, evaluating the exact same expression in automatic (local) scope executes dynamically at runtime and can trigger hardware floating-point exceptions (`SIGFPE`).

---

## 3. Enumerations, Bit-Fields, and the `switch` Construct

### Enumerations and Struct Bit-Fields
* Enumeration constants are defined by the C grammar to be Integer Constant Expressions:
  ```c
  enum Status { OK = 1, ERROR = 1 << 2, TIMEOUT = ERROR + 10 };
  ```
* Struct bit-fields require an ICE to fix the bit allocation width:
  ```c
  struct Packet { unsigned int flag : 1; unsigned int priority : 3; };
  ```

### The `switch` Statement Semantics
A `switch` statement controls branching based on an integer-compatible selector:

> [!definition] `switch` Statement Anatomy
> * **Control Expression:** Must evaluate to an integer type (or undergo integer promotion).
> * **Case Labels:** Must be unique Integer Constant Expressions (ICE). Floating-point values or runtime variables are syntax errors.
> * **Default Label:** Can appear at any arbitrary position within the switch body.
> * **Interleaving (Duff's Device):** Case labels are syntactically treated as goto-labels. They can be placed inside inner compound blocks, loops, or branch statements within the switch body.

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->

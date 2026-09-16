## 1. Representation, Conversion, and Variadic `printf` Pipeline

Evaluating an assignment and printing integer types in C follows a strict multi-step pipeline:

1. **Integer Literal Parsing:** Integer constants without suffixes are treated by default as signed `int` (or the smallest signed integer type capable of representing the value).
2. **Unary Negation:** For negative values (e.g., `-42`), the positive literal is evaluated first, after which the unary minus operator (`-`) is applied via two's complement.
3. **Truncation or Extension on Assignment:**
   * **Widening (Extension):** Dictated entirely by the **source (RHS) type**, never the destination. A signed source undergoes sign-extension (replicating the MSB), while an unsigned source undergoes zero-extension.
   * **Narrowing (Truncation):** Higher-order bits exceeding the destination width are discarded, regardless of the sign of either operand.
4. **Variadic Integer Promotion in `printf`:**
   * Arguments passed to variadic functions like `printf` undergo default argument promotions: types narrower than `int` (`char`, `short`) are promoted to `int` (or `unsigned int`).
   * `printf` does not inspect the original variable's source type; it simply decodes the promoted bit pattern sitting in the CPU register or stack frame according to the provided format specifier (`%d`, `%u`, etc.).

> [!trap] Literal Typing vs. Explicit Casts
> By default, character constants like `'a'` have type `int` in C (size 4 on 32/64-bit systems), whereas in C++ they have type `char`. Explicit casts such as `(char)'a'` or `(short)45` explicitly narrow the operand type before further evaluation.

### Worked Example: Promotion vs. Assignment Truncation
```c
char a = 30, b = 40;
char d = 30 * 40;

printf("%d\n", d);      // Output: -80
printf("%d\n", a * b);  // Output: 1200
```

* **Calculation for `d`:**
  * $30 \times 40 = 1200$ produces an `int` binary: $00000000\;00000000\;00000100\;10110000_2$.
  * Assigning to `char d` (8-bit signed) truncates upper 24 bits: $10110000_2$.
  * When passed to `printf("%d", d)`, `d` sign-extends to $-80$.
* **Calculation for `a * b`:**
  * Both `a` and `b` promote to signed `int` (32-bit) *before* multiplication.
  * Evaluates directly as $30 \times 40 = 1200$ without 8-bit truncation.

---

## 2. Integer Conversion Hierarchy and Rules

> [!definition] Integer Conversion Rank
> Every integer type has an integer conversion rank defined by the C standard based primarily on bit-width:
> 
> $$\text{\_Bool} < \text{char} \equiv \text{signed char} \equiv \text{unsigned char} < \text{short} \equiv \text{unsigned short} < \text{int} \equiv \text{unsigned int} < \text{long} \equiv \text{unsigned long} < \text{long long} \equiv \text{unsigned long long}$$
>
> *Note:* Signed and unsigned versions of the exact same base integer type share identical conversion rank.

The evaluation of binary arithmetic expressions occurs in two consecutive phases:

```
[Operands A, B] ---> Step 1: Integer Promotion ---> Step 2: Usual Arithmetic Conversions ---> [Common Type]
```

### Step 1: Integer Promotion Phase
Before processing any binary arithmetic or bitwise operation, any operand whose rank is strictly lower than `int` (`_Bool`, `char`, `short`) is automatically promoted:
* To `int`, if `int` can represent all values of the original type.
* To `unsigned int`, otherwise.

### Step 2: Usual Arithmetic Conversion Phase
Once both operands are at least of rank `int`, if their types still differ, the compiler unifies them:

#### Case 1: Same Signedness, Different Rank
Lower rank operand is extended to match higher rank type (e.g. `int + long` $\longrightarrow$ `long`).

#### Case 2: Different Signedness, Different or Equal Rank
* **Subcase 2A: $\text{Rank}(\text{unsigned}) \ge \text{Rank}(\text{signed})$:** Signed operand converted to unsigned type.
* **Subcase 2B: $\text{Rank}(\text{signed}) > \text{Rank}(\text{unsigned})$:**
  * If signed type can represent all values of unsigned type, unsigned converted to higher-rank signed type.
  * Otherwise, both converted to **unsigned variant of higher-rank type**.

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->

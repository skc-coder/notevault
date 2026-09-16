## 1. Integer Constants and Literal Typing

When an integer literal is written without suffixes, the compiler assigns it the first type from the hierarchy that can represent its value:

$$\text{int} \longrightarrow \text{long int} \longrightarrow \text{long long int}$$

The bit representation generated in memory depends strictly on the constant's own characteristics and literal suffixes, **not** the type of the variable to which it is eventually assigned.

To enforce specific width and signedness directly on literal constants, C provides literal suffixes:

| Suffix | Resulting Type |
| :--- | :--- |
| `u` / `U` | `unsigned int` |
| `l` / `L` | `long int` |
| `ll` / `LL` | `long long int` |
| `ull` / `ULL` | `unsigned long long int` |

> [!trap] Unary Minus on Literals
> In C, a negative literal like `-42` is not a standalone lexical token. The compiler parses `42` as an unsigned or positive integer constant first, and then applies the unary negation operator `-`.

---

## 2. Bit-Width Conversions: Extension vs. Truncation

### A. Widening / Extension (Meaning Preserved)
When converting a narrower integer type to a wider integer type, the type of the **source operand (RHS)** completely dictates how extension bits are filled:

* **Zero-Extension (Source is `unsigned`):** High-order bit positions are padded with zeroes (`0`).
* **Sign-Extension (Source is `signed`):** High-order bit positions are replicated using the source's MSB.

```c
short int x = 9;         // 16-bit: 0000 0000 0000 1001 (MSB = 0)
int y = x;               // 32-bit: 00000000 00000000 00000000 00001001 (Zero-extended because MSB was 0)

short int x_neg = -9;    // 16-bit: 1111 1111 1111 0111 (MSB = 1)
unsigned int y_u = x_neg;// 32-bit: 11111111 11111111 11111111 11110111
                         // Sign-extended because source (short int) is SIGNED!
```

> [!property] Extension Invariant
> Extension is determined purely by the **source variable type (RHS)**, never by the destination variable type (LHS).

Consider an unsigned source assigned to a signed destination:
```c
unsigned short x = -9;   // Interpreted as 65527: 1111 1111 1111 0111
int y = x;               // Source is UNSIGNED -> Padded with zeros:
                         // 00000000 00000000 11111111 11110111 = 65527
```

### B. Narrowing / Truncation (Data Discarded)
When converting a wider integer to a narrower integer type:
* The upper $(W_{\text{source}} - W_{\text{dest}})$ bytes/bits are discarded (**truncated**).
* Truncation operates purely via bit slicing; neither the signedness of the RHS nor the LHS affects the bit-chopping itself.
* Discarding bits can abruptly flip the sign bit or alter numeric magnitude.

---

## 3. Case Studies: Extension & Truncation Tracing

### Case Study 1: `signed char c = 130;`
1. **Source constant:** $130_{10} = \text{0x00000082}$ ($32$-bit `int`).
2. **Assignment (Truncation to $1$ byte):** 
   $$\text{Lower 8 bits} = 10000010_2$$
3. **Integer Promotion during `printf`:**
   Because `c` is `signed char` and its MSB is `1`, it sign-extends to a $32$-bit `int` by copying `1` across the upper $24$ bits:
   $$\text{Promoted bit pattern} = \underbrace{11111111\;11111111\;11111111}_{\text{Sign-extended 3 bytes}}\;10000010_2$$
4. **Output formatting:**
   * `%d` reads as signed 32-bit `int`: $\text{Value} = -128 + 2 = -126$
   * `%u` reads the exact same bit pattern as unsigned: $\text{Value} = 2^{32} - 126 = 4294967170$

```c
signed char c = 130;
printf("%d\n", c); // Outputs: -126
printf("%u\n", c); // Outputs: 4294967170
```

### Case Study 2: `unsigned char c = 130;`
1. **Assignment (Truncation to $1$ byte):** $\text{Lower 8 bits} = 10000010_2$
2. **Integer Promotion during `printf`:** Zero-extension: $00000000\;00000000\;00000000\;10000010_2$
3. **Output formatting:** Both `%d` and `%u` output `130`.

```c
unsigned char c = 130;
printf("%d\n", c); // Outputs: 130
printf("%u\n", c); // Outputs: 130
```

### Case Study 3: `signed char x = 258;`
1. Max capacity of an $8$-bit container is $255$.
2. Constant representation: $258_{10} = 00000000\;00000000\;00000001\;00000010_2$
3. **Truncation:** Lower $8$ bits = $00000010_2$.
4. **Integer Promotion:** Sign extension yields value `2`.

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->

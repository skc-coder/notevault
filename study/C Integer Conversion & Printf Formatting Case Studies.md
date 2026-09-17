---
tags:
  - clang
  - c-language
  - type-conversion
  - printf
  - study
---


Understanding how truncation on assignment interacts with variadic integer promotion in `printf` requires tracing step-by-step bit transformations.

---

## Case Study 1: `signed char c = 130;`

```c
signed char c = 130;
printf("%d\n", c); // Outputs: -126
printf("%u\n", c); // Outputs: 4294967170
```

### Execution Pipeline Trace
1. **Source constant:** $130_{10} = \text{0x00000082}$ ($32$-bit `int`).
2. **Assignment Truncation to 1 byte (`signed char`):**
   $$\text{Lower 8 bits} = 10000010_2$$
3. **Integer Promotion during `printf`:**
   Because `c` is `signed char` and its MSB is `1`, it **sign-extends** to a 32-bit `int` by replicating `1` across the upper 24 bits:
   $$\text{Promoted Bit Pattern} = \underbrace{11111111\;11111111\;11111111}_{\text{Sign-extended 3 bytes}}\;10000010_2$$
4. **Format Specifier Evaluation:**
   - `%d` interprets as 32-bit signed `int`: $-128 + 2 = -126$.
   - `%u` interprets exact same pattern as 32-bit `unsigned int`: $2^{32} - 126 = 4294967170$.

---

## Case Study 2: `unsigned char c = 130;`

```c
unsigned char c = 130;
printf("%d\n", c); // Outputs: 130
printf("%u\n", c); // Outputs: 130
```

### Execution Pipeline Trace
1. **Assignment Truncation to 1 byte (`unsigned char`):** $\text{Lower 8 bits} = 10000010_2$.
2. **Integer Promotion during `printf`:**
   Because `c` is `unsigned char`, it **zero-extends**:
   $$00000000\;00000000\;00000000\;10000010_2$$
3. **Format Specifier Evaluation:** Both `%d` and `%u` output `130`.

---

## Related Notes
- [[Integer Promotion Rules in C]]
- [[Bit-Width Extensions & Sign vs Zero Extension]]
- [[Narrowing & Truncation Mechanics]]
- [[Usual Arithmetic Conversions & Hierarchy]]

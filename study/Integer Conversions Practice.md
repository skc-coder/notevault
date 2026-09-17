---
tags:
  - clang
  - c-language
  - type-conversion
  - printf
  - study
---

## Example 1: `signed char c = 130;`

```c
signed char c = 130;
printf("%d\n", c); // Outputs: -126
printf("%u\n", c); // Outputs: 4294967170
```

### Execution Pipeline Trace
1. **Source Constant:** $130_{10} = \text{0x00000082}$ (32-bit `int`).
2. **Assignment Truncation to 1 byte (`signed char`):**
   - $\text{Lower 8 bits} = 10000010_2$ (Value: $-128 + 2 = -126$).
3. **Integer Promotion during `printf`:**
   - Because `c` is a `signed char` and its MSB is $1$, it **sign-extends** into a 32-bit `int` by replicating $1$ across the upper 24 bits:
   $$\text{Promoted Bit Pattern} = \underbrace{11111111\;11111111\;11111111}_{\text{Sign-extended 3 bytes}}\;10000010_2 = \text{0xFFFFFF82}$$
4. **Format Specifier Evaluation:**
   - `%d` interprets as 32-bit signed `int`: $-126$.
   - `%u` interprets as 32-bit unsigned `int`: $2^{32} - 126 = 4294967170$.

---

## Example 2: `unsigned char c = 130;`

```c
unsigned char c = 130;
printf("%d\n", c); // Outputs: 130
printf("%u\n", c); // Outputs: 130
```

### Execution Pipeline Trace
1. **Source Constant:** $130_{10} = \text{0x00000082}$ (32-bit `int`).
2. **Assignment Truncation to 1 byte (`unsigned char`):**
   - $\text{Lower 8 bits} = 10000010_2$ (Unsigned value: $130$).
3. **Integer Promotion during `printf`:**
   - Because `c` is an `unsigned char`, it **zero-extends** into a 32-bit `int`:
   $$\text{Promoted Bit Pattern} = \underbrace{00000000\;00000000\;00000000}_{\text{Zero-extended 3 bytes}}\;10000010_2 = \text{0x00000082}$$
4. **Format Specifier Evaluation:**
   - Both `%d` and `%u` evaluate the positive pattern as $130$.

---

## Example 3: `signed char c = -5;`

```c
signed char c = -5;
printf("%d\n", c); // Outputs: -5
printf("%u\n", c); // Outputs: 4294967291
```

### Execution Pipeline Trace
1. **Source Constant:** $-5_{10} = \text{0xFFFFFFFB}$ (32-bit two's complement).
2. **Assignment Truncation to 1 byte (`signed char`):**
   - $\text{Lower 8 bits} = 11111011_2$ ($251_{10}$, signed interpretation: $251 - 256 = -5$).
3. **Integer Promotion during `printf`:**
   - Because `c` is a `signed char` and its MSB is $1$, it **sign-extends** to 32 bits:
   $$\text{Promoted Bit Pattern} = \underbrace{11111111\;11111111\;11111111}_{\text{Sign-extended 3 bytes}}\;11111011_2 = \text{0xFFFFFFFB}$$
4. **Format Specifier Evaluation:**
   - `%d` interprets as 32-bit signed: $-5$.
   - `%u` interprets as 32-bit unsigned: $2^{32} - 5 = 4294967291$.

---

## Example 4: `unsigned char c = -5;`

```c
unsigned char c = -5;
printf("%d\n", c); // Outputs: 251
printf("%u\n", c); // Outputs: 251
```

### Analysis Trace
1. **Truncation:** $-5 \pmod{256} = 251_{10} = 11111011_2$.
2. **Promotion:** Since `c` is `unsigned char`, it **zero-extends** to $32$ bits:
   $$\text{Promoted Bit Pattern} = 00000000\;00000000\;00000000\;11111011_2 = \text{0x000000FB}$$
3. **Output:** Both `%d` and `%u` display **$251$**.
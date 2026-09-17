---
tags:
  - clang
  - c-language
  - type-conversion
  - printf
  - study
---

## Case 1: 0-Extension, Signed Interpretation

### Example 1.1: `signed char c = 65;`

```c
signed char c = 65;
printf("%d\n", c); // Outputs: 65
printf("%u\n", c); // Outputs: 65
```

#### Execution Pipeline Trace

- **Source Constant:** $65_{10} = \text{0x00000041}$ (32-bit `int`).
- **Assignment Truncation to 1 byte (`signed char`):**
  $\text{Lower 8 bits} = 01000001_2$ ($U = 65 < 128 \implies \text{MSB} = 0$).
- **Integer Promotion during `printf`:**
  Because `c` is a `signed char` and its MSB is $0$, sign-extension replicates $0$ across the upper 24 bits:
  $$\text{Promoted Bit Pattern} = \underbrace{00000000\;00000000\;00000000}_{\text{Sign-extended with zeros}}\;01000001_2 = \text{0x00000041}$$
- **Format Specifier Evaluation & Matrix Case Mapping:**
  - `%d` (**Matrix Case: Row 1, $\text{MSB} = 0$**): Evaluates as 32-bit signed: $\text{val} \pmod{2^8} = 65$.
  - `%u` (**Matrix Case: Row 2, $\text{MSB} = 0$**): Evaluates as 32-bit unsigned: since bit 31 is $0$, prints $65$.

---

### Example 1.2: `signed char c = 300;`

```c
signed char c = 300;
printf("%d\n", c); // Outputs: 44
printf("%u\n", c); // Outputs: 44
```

#### Execution Pipeline Trace

- **Source Constant:** $300_{10} = \text{0x0000012C}$ (32-bit `int`).
- **Assignment Truncation to 1 byte (`signed char`):**
  $300 \pmod{256} = 44$. $\text{Lower 8 bits} = 00101100_2$ ($U = 44 < 128 \implies \text{MSB} = 0$).
- **Integer Promotion during `printf`:**
  Because `c` is a `signed char` and its MSB is $0$, sign-extension fills the upper 24 bits with $0$s:
  $$\text{Promoted Bit Pattern} = \text{0x0000002C}$$
- **Format Specifier Evaluation & Matrix Case Mapping:**
  - `%d` (**Matrix Case: Row 1, $\text{MSB} = 0$**): $\text{val} \pmod{2^8} = 44$.
  - `%u` (**Matrix Case: Row 2, $\text{MSB} = 0$**): Bit 31 is $0$, outputs $44$.

---

### Example 1.3: `signed char c = -200;`

```c
signed char c = -200;
printf("%d\n", c); // Outputs: 56
printf("%u\n", c); // Outputs: 56
```

#### Execution Pipeline Trace

- **Source Constant:** $-200_{10} = \text{0xFFFFFF38}$ (32-bit two's complement).
- **Assignment Truncation to 1 byte (`signed char`):**
  $-200 \pmod{256} = 256 - 200 = 56$. $\text{Lower 8 bits} = 00111000_2$ ($U = 56 < 128 \implies \text{MSB} = 0$).
- **Integer Promotion during `printf`:**
  Because `c` is a `signed char` and its MSB is $0$, sign-extension fills the upper 24 bits with $0$s:
  $$\text{Promoted Bit Pattern} = \text{0x00000038}$$
- **Format Specifier Evaluation & Matrix Case Mapping:**
  - `%d` (**Matrix Case: Row 1, $\text{MSB} = 0$**): $\text{val} \pmod{2^8} = 56$.
  - `%u` (**Matrix Case: Row 2, $\text{MSB} = 0$**): Bit 31 is $0$, outputs $56$.

---

## Case 2: 1-Extension, Signed Interpretation

### Example 2.1: `signed char c = 130;`

```c
signed char c = 130;
printf("%d\n", c); // Outputs: -126
printf("%u\n", c); // Outputs: 4294967170
```

#### Execution Pipeline Trace

- **Source Constant:** $130_{10} = \text{0x00000082}$ (32-bit `int`).
- **Assignment Truncation to 1 byte (`signed char`):**
  $\text{Lower 8 bits} = 10000010_2$ ($U = 130 \ge 128 \implies \text{MSB} = 1$).
- **Integer Promotion during `printf`:**
  Because `c` is a `signed char` and its MSB is $1$, it sign-extends into a 32-bit `int` by replicating $1$ across the upper 24 bits:
  $$\text{Promoted Bit Pattern} = \underbrace{11111111\;11111111\;11111111}_{\text{Sign-extended 3 bytes}}\;10000010_2 = \text{0xFFFFFF82}$$
- **Format Specifier Evaluation & Matrix Case Mapping:**
  - `%d` (**Matrix Case: Row 1, $\text{MSB} = 1$**): Interprets as 32-bit signed: $S = -2^8 + U = -256 + 130 = -126$.
  - `%u` (**Matrix Case: Row 2, $\text{MSB} = 1$ with Sign-Extension**): Interprets as 32-bit unsigned: $2^{32} + S = 2^{32} - 126 = 4294967170$.

---

### Example 2.2: `signed char c = -5;`

```c
signed char c = -5;
printf("%d\n", c); // Outputs: -5
printf("%u\n", c); // Outputs: 4294967291
```

#### Execution Pipeline Trace

- **Source Constant:** $-5_{10} = \text{0xFFFFFFFB}$ (32-bit two's complement).
- **Assignment Truncation to 1 byte (`signed char`):**
  $-5 \pmod{256} = 251$. $\text{Lower 8 bits} = 11111011_2$ ($U = 251 \ge 128 \implies \text{MSB} = 1$).
- **Integer Promotion during `printf`:**
  Because `c` is a `signed char` and its MSB is $1$, it sign-extends with $1$s to 32 bits:
  $$\text{Promoted Bit Pattern} = \text{0xFFFFFFFB}$$
- **Format Specifier Evaluation & Matrix Case Mapping:**
  - `%d` (**Matrix Case: Row 1, $\text{MSB} = 1$**): Interprets as 32-bit signed: $S = -2^8 + U = -256 + 251 = -5$.
  - `%u` (**Matrix Case: Row 2, $\text{MSB} = 1$ with Sign-Extension**): Interprets as 32-bit unsigned: $2^{32} + S = 2^{32} - 5 = 4294967291$.

---

### Example 2.3: `signed char c = 250;`

```c
signed char c = 250;
printf("%d\n", c); // Outputs: -6
printf("%u\n", c); // Outputs: 4294967290
```

#### Execution Pipeline Trace

- **Source Constant:** $250_{10} = \text{0x000000FA}$ (32-bit `int`).
- **Assignment Truncation to 1 byte (`signed char`):**
  $250 \pmod{256} = 250$. $\text{Lower 8 bits} = 11111010_2$ ($U = 250 \ge 128 \implies \text{MSB} = 1$).
- **Integer Promotion during `printf`:**
  Because `c` is a `signed char` and its MSB is $1$, it sign-extends with $1$s:
  $$\text{Promoted Bit Pattern} = \text{0xFFFFFFFA}$$
- **Format Specifier Evaluation & Matrix Case Mapping:**
  - `%d` (**Matrix Case: Row 1, $\text{MSB} = 1$**): Interprets as 32-bit signed: $S = -2^8 + U = -256 + 250 = -6$.
  - `%u` (**Matrix Case: Row 2, $\text{MSB} = 1$ with Sign-Extension**): Interprets as 32-bit unsigned: $2^{32} + S = 2^{32} - 6 = 4294967290$.

---

## Case 3: Zero-Extension, Unsigned Interpretation

### Example 3.1: `unsigned char c = 65;`

```c
unsigned char c = 65;
printf("%d\n", c); // Outputs: 65
printf("%u\n", c); // Outputs: 65
```

#### Execution Pipeline Trace

- **Source Constant:** $65_{10} = \text{0x00000041}$ (32-bit `int`).
- **Assignment Truncation to 1 byte (`unsigned char`):**
  $\text{Lower 8 bits} = 01000001_2$ ($U = 65 < 128$).
- **Integer Promotion during `printf`:**
  Because `c` is an `unsigned char`, it **zero-extends** into a 32-bit `int`:
  $$\text{Promoted Bit Pattern} = \underbrace{00000000\;00000000\;00000000}_{\text{Zero-extended 3 bytes}}\;01000001_2 = \text{0x00000041}$$
- **Format Specifier Evaluation & Matrix Case Mapping:**
  - **Matrix Case: Unsigned Source (Zero-Extension)**. Since bit 31 is $0$, both `%d` and `%u` evaluate the positive pattern directly as $\text{val} \pmod{2^8} = 65$.

---

### Example 3.2: `unsigned char c = 300;`

```c
unsigned char c = 300;
printf("%d\n", c); // Outputs: 44
printf("%u\n", c); // Outputs: 44
```

#### Execution Pipeline Trace

- **Source Constant:** $300_{10} = \text{0x0000012C}$ (32-bit `int`).
- **Assignment Truncation to 1 byte (`unsigned char`):**
  $300 \pmod{256} = 44$. $\text{Lower 8 bits} = 00101100_2$ ($U = 44$).
- **Integer Promotion during `printf`:**
  Because `c` is an `unsigned char`, it zero-extends into a 32-bit `int`:
  $$\text{Promoted Bit Pattern} = \text{0x0000002C}$$
- **Format Specifier Evaluation & Matrix Case Mapping:**
  - **Matrix Case: Unsigned Source (Zero-Extension)**. Bit 31 is $0$, so both `%d` and `%u` output $\text{val} \pmod{2^8} = 44$.

---

### Example 3.3: `unsigned char c = -200;`

```c
unsigned char c = -200;
printf("%d\n", c); // Outputs: 56
printf("%u\n", c); // Outputs: 56
```

#### Execution Pipeline Trace

- **Source Constant:** $-200_{10} = \text{0xFFFFFF38}$ (32-bit two's complement).
- **Assignment Truncation to 1 byte (`unsigned char`):**
  $-200 \pmod{256} = 256 - 200 = 56$. $\text{Lower 8 bits} = 00111000_2$ ($U = 56$).
- **Integer Promotion during `printf`:**
  Because `c` is an `unsigned char`, it zero-extends into a 32-bit `int`:
  $$\text{Promoted Bit Pattern} = \text{0x00000038}$$
- **Format Specifier Evaluation & Matrix Case Mapping:**
  - **Matrix Case: Unsigned Source (Zero-Extension)**. Bit 31 is $0$, so both `%d` and `%u` output $\text{val} \pmod{2^8} = 56$.

---

## Case 4: Zero-Extension, Unsigned Interpretation

### Example 4.1: `unsigned char c = 130;`

```c
unsigned char c = 130;
printf("%d\n", c); // Outputs: 130
printf("%u\n", c); // Outputs: 130
```

#### Execution Pipeline Trace

- **Source Constant:** $130_{10} = \text{0x00000082}$ (32-bit `int`).
- **Assignment Truncation to 1 byte (`unsigned char`):**
  $\text{Lower 8 bits} = 10000010_2$ (Unsigned magnitude: $U = 130 \ge 128$).
- **Integer Promotion during `printf`:**
  Because `c` is an `unsigned char`, it **zero-extends** into a 32-bit `int` regardless of bit 7:
  $$\text{Promoted Bit Pattern} = \underbrace{00000000\;00000000\;00000000}_{\text{Zero-extended 3 bytes}}\;10000010_2 = \text{0x00000082}$$
- **Format Specifier Evaluation & Matrix Case Mapping:**
  - **Matrix Case: Unsigned Source (Zero-Extension)**. Because bit 31 (promoted MSB) is $0$, both `%d` and `%u` evaluate the positive pattern directly as $\text{val} \pmod{2^8} = 130$.

---

### Example 4.2: `unsigned char c = -5;`

```c
unsigned char c = -5;
printf("%d\n", c); // Outputs: 251
printf("%u\n", c); // Outputs: 251
```

#### Execution Pipeline Trace

- **Source Constant:** $-5_{10} = \text{0xFFFFFFFB}$ (32-bit two's complement).
- **Assignment Truncation to 1 byte (`unsigned char`):**
  $-5 \pmod{256} = 251$. $\text{Lower 8 bits} = 11111011_2$ ($U = 251 \ge 128$).
- **Integer Promotion during `printf`:**
  Because `c` is an `unsigned char`, it zero-extends to 32 bits:
  $$\text{Promoted Bit Pattern} = \text{0x000000FB}$$
- **Format Specifier Evaluation & Matrix Case Mapping:**
  - **Matrix Case: Unsigned Source (Zero-Extension)**. Promoted bit 31 is $0$, so both `%d` and `%u` display $\text{val} \pmod{2^8} = 251$.

---

### Example 4.3: `unsigned char c = 200;`

```c
unsigned char c = 200;
printf("%d\n", c); // Outputs: 200
printf("%u\n", c); // Outputs: 200
```

#### Execution Pipeline Trace

- **Source Constant:** $200_{10} = \text{0x000000C8}$ (32-bit `int`).
- **Assignment Truncation to 1 byte (`unsigned char`):**
  $200 \pmod{256} = 200$. $\text{Lower 8 bits} = 11001000_2$ ($U = 200 \ge 128$).
- **Integer Promotion during `printf`:**
  Because `c` is an `unsigned char`, it zero-extends to 32 bits:
  $$\text{Promoted Bit Pattern} = \text{0x000000C8}$$
- **Format Specifier Evaluation & Matrix Case Mapping:**
  - **Matrix Case: Unsigned Source (Zero-Extension)**. Promoted bit 31 is $0$, so both `%d` and `%u` display $\text{val} \pmod{2^8} = 200$.
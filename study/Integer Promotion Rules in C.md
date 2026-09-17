---
title: Integer Promotion Rules in C
tags:
  - clang
  - c-language
  - type-conversion
  - study
---


CPU registers and Arithmetic Logic Units (ALUs) operate most efficiently on natural hardware word boundaries (typically 32-bit or 64-bit).

> [!definition] Integer Promotion
> Before evaluating expressions, performing bitwise operations, or passing arguments through variadic parameters (such as `printf`), C automatically promotes integer types with a conversion rank lower than `int` (`char`, `signed char`, `unsigned char`, `short`, `unsigned short`, `_Bool`):
> 
> - If `int` can represent all possible values of the original type, the value is promoted to **`int`**.
> - Otherwise, it is promoted to **`unsigned int`**.

---

## Promotion vs. Assignment Truncation

```c
char a = 30, b = 40;
char d = 30 * 40;

printf("%d\n", d);      // Output: -80
printf("%d\n", a * b);  // Output: 1200
```

### Analysis
1. **For `d = 30 * 40`:**
   - Both literals are `int`. $30 \times 40 = 1200$ ($00000000\;00000000\;00000100\;10110000_2$).
   - Assignment to 8-bit `char d` truncates upper 24 bits $\longrightarrow 10110000_2$.
   - Passing `d` to `printf` sign-extends $10110000_2$ to 32-bit `int`, printing **$-80$**.
2. **For `a * b`:**
   - Operands `a` and `b` undergo integer promotion to 32-bit `int` **before** multiplication.
   - Evaluates as $30 \times 40 = 1200$ without 8-bit truncation.

---

## Character Literal Type Discrepancy

In C, a character literal such as `'a'` has type **`int`** (4 bytes on 32/64-bit systems) with ASCII value `97`. Assigning it to a `char` variable truncates the upper 3 zero bytes:

```c
char c = 'a'; // 'a' is a 4-byte int (0x00000061); 3 upper bytes are truncated to fit 1 byte
```

*(Note: In C++, character literals like `'a'` are natively typed as `char` of 1 byte).*

---

## Related Notes
- [[Two's Complement Fundamentals & Weight Method]]
- [[Integer Literal Typing & Parsing Rules]]
- [[Usual Arithmetic Conversions & Hierarchy]]
- [[Bit-Width Extensions & Sign vs Zero Extension]]

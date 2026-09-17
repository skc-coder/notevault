---
tags:
  - clang
  - c-language
  - type-conversion
  - study
---


In C, binary arithmetic operations require operands to be converted to a common type before evaluation.

---

## Integer Conversion Rank

Every integer type in C has a predefined conversion rank:

$$\text{\_Bool} < \text{char} \equiv \text{signed char} \equiv \text{unsigned char} < \text{short} \equiv \text{unsigned short} < \text{int} \equiv \text{unsigned int} < \text{long} \equiv \text{unsigned long} < \text{long long} \equiv \text{unsigned long long}$$

> [!note] Rank Rule
> Signed and unsigned variants of the exact same base integer type share identical conversion rank.

---

## Two-Phase Evaluation Pipeline

```
[Operands A, B] ---> Phase 1: Integer Promotion ---> Phase 2: Usual Arithmetic Conversions ---> [Common Type]
```

### Phase 1: Integer Promotion
Any operand with rank lower than `int` (`_Bool`, `char`, `short`) is promoted to `int` (or `unsigned int` if `int` cannot hold all values).

### Phase 2: Usual Arithmetic Conversions
If operand types still differ after promotion, the compiler unifies them:

#### Case 1: Same Signedness, Different Rank
The operand with lower rank is converted to the higher rank type (e.g. `int + long` $\longrightarrow$ `long`).

#### Case 2: Different Signedness, Different or Equal Rank
1. **$\text{Rank}(\text{unsigned}) \ge \text{Rank}(\text{signed})$:** Signed operand converted to unsigned type.
2. **$\text{Rank}(\text{signed}) > \text{Rank}(\text{unsigned})$:**
   - If signed type can represent all values of unsigned type $\longrightarrow$ unsigned converted to higher-rank signed type.
   - Otherwise $\longrightarrow$ both converted to **unsigned variant of higher-rank type**.

---

## Related Notes
- [[Integer Promotion Rules in C]]
- [[Bit-Width Extensions & Sign vs Zero Extension]]
- [[C Integer Conversion & Printf Formatting Case Studies]]

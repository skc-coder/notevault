---
tags:
  - clang
  - c-language
  - operators
  - study
---


---

## Assignment & Compound Assignment

- **Compound Assignment Expansion:**
  $$V \text{ op}= E \implies V = V \text{ op } (E)$$
  The right-hand expression $E$ is evaluated as a fully parenthesized unit with higher precedence before applying `op`.

---

## The Comma Operator (`,`)

- **Sequential Evaluation:** Evaluates operands left to right and discards the left operand's value.
- **Result Value:** Yields the value and type of the **rightmost operand**.
- **Sequence Point:** Introduces an explicit sequence point after evaluating the left operand.

```c
int x = (a = 3, b = 4, a + b); // a=3, b=4, x=7
```

---

## Related Notes
- [[Operator Precedence & Associativity Hierarchy]]
- [[Sequence Points & Short-Circuit Evaluation]]

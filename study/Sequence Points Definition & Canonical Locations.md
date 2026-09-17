---
title: Sequence Points Definition & Canonical Locations
tags:
  - clang
  - c-language
  - sequence-points
  - study
---


A sequence point governs execution ordering guarantees and memory side effects in C.

> [!definition] Sequence Point
> A sequence point defines a point in the program's execution where all side effects of previous evaluations are guaranteed to be complete, and no side effects from subsequent evaluations have yet taken place.

---

## Canonical Sequence Points Matrix

1. The end of a full expression terminated by a semicolon (`;`).
2. Logical AND (`&&`) and logical OR (`||`) operators (after evaluating the first operand).
3. The comma operator (`,`) (after evaluating the left operand).
4. The condition expression in a ternary operation (`? :`) before evaluating either branch.
5. Right before a function call executes (after all arguments have been evaluated).

---

## Related Notes
- [[Short-Circuit Evaluation Guarantees]]
- [[Undefined Behavior Between Sequence Points]]

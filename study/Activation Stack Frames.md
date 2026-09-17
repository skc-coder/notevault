---
title: Activation Stack Frames
tags:
  - clang
  - c-language
  - stack
  - recursion
  - study
---


Each function call allocates a discrete activation frame on the **Stack Segment**.

---

## Activation Frame Contents

1. Local automatic variables (`auto`).
2. Parameter values passed to the function.
3. Return memory address pointing back to caller instruction frame.

---

## Related Notes
- [[Recursion Tracing - Tree Method & Side Effects]]
- [[Process Memory Layout - Segments & Stack]]

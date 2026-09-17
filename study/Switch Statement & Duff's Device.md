---
title: Switch Statement & Duff's Device
tags:
  - clang
  - c-language
  - control-flow
  - study
---


A `switch` statement controls multi-way branching based on an integer-compatible selector expression.

---

## `switch` Anatomy Rules

> [!definition] Anatomy of `switch`
> - **Control Expression:** Must evaluate to an integer type (or undergo integer promotion).
> - **Case Labels:** Must be unique Integer Constant Expressions (ICE). Floating-point values or runtime variables generate compilation errors.
> - **Default Label:** Can appear at any location within the switch body.

---

## Interleaving & Duff's Device

Case labels are syntactically treated as `goto` targets. They can be placed inside inner compound blocks, loops, or branch statements within the switch body:

```c
// Duff's Device example for unrolling copies
void send(register char *to, register char *from, register int count) {
    register int n = (count + 7) / 8;
    switch (count % 8) {
    case 0: do { *to = *from++;
    case 7:      *to = *from++;
    case 6:      *to = *from++;
    case 5:      *to = *from++;
    case 4:      *to = *from++;
    case 3:      *to = *from++;
    case 2:      *to = *from++;
    case 1:      *to = *from++;
            } while (--n > 0);
    }
}
```

---

## Related Notes
- [[Dangling Else Ambiguity]]
- [[Integer Constant Expressions (ICE)]]
- [[Loop Control Flow - Break & Continue]]

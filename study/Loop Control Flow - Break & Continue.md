---
title: Loop Control Flow - Break & Continue
tags:
  - clang
  - c-language
  - control-flow
  - study
---

# Loop Control Flow - Break & Continue

Both `break` and `continue` statements alter linear iteration execution.

> [!property] Target Scope Invariant
> `break` and `continue` apply strictly to the **innermost enclosing loop construct** (`for`, `while`, `do-while`) in which they reside. They do not break or skip outer parent loops.
>
> *(Note: `break` exits an enclosing `switch` block, but `continue` does not; a `continue` inside a `switch` located within a loop skips to the next iteration of the enclosing loop).*

---

## Related Notes
- [[Switch Statement & Duff's Device]]
- [[Dangling Else Ambiguity]]

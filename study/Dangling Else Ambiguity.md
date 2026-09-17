---
title: Dangling Else Ambiguity
tags:
  - clang
  - c-language
  - control-flow
  - study
---

# Dangling Else Ambiguity

In C, nested branching structures without explicit compound block braces (`{}`) exhibit the **dangling else ambiguity**.

> [!property] Dangling Else Resolution Invariant
> In nested branching structures lacking explicit compound blocks (`{}`), an `else` clause syntactically binds to the **closest preceding un-paired `if`** within the same block scope.

---

## Code Example & Parsing

```c
if (condition1)
    if (condition2)
        action_a();
else
    action_b(); // Belongs syntactically to 'if (condition2)', NOT 'if (condition1)'!
```

### Explicit Braces Equivalent

To force `else` to belong to `if (condition1)`, explicit compound braces are required:

```c
if (condition1) {
    if (condition2)
        action_a();
} else {
    action_b();
}
```

---

## Related Notes
- [[Switch Statement & Duff's Device]]
- [[Loop Control Flow - Break & Continue]]

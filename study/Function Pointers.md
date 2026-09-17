---
tags:
  - clang
  - c-language
  - function-pointers
  - study
---


In C, function names decay to function pointers, and dereferencing function pointers resolves back to the function itself.

---

## Canonical Invocation Syntaxes

```c
void greet(void) { /* ... */ }

void (*fp)(void) = greet;
fp();       // Direct invocation
(*fp)();    // Explicit dereference invocation
(**fp)();   // Redundant dereference (fp == *fp == **fp)
```


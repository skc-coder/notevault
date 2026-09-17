---
tags:
  - clang
  - c-language
  - functions
  - study
---


---

## Function Definition vs Declaration Scope

- **Function Definitions:** Must always reside at global/file scope. Standard C **does not support nested functions** (defining a function inside another function body is illegal).
- **Function Declarations:** Can occur inside any local block scope. The declaration makes the function visible strictly within that block scope.


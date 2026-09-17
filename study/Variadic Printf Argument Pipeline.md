---
title: Variadic Printf Argument Pipeline
tags:
  - clang
  - c-language
  - printf
  - variadic-functions
  - study
---

# Variadic Printf Argument Pipeline

Arguments passed to variadic functions like `printf` undergo default argument promotions.

---

## Variadic Promotion & Decoding Pipeline

1. **Default Argument Promotions:** Narrower integer types (`char`, `short`) are automatically promoted to `int` (or `unsigned int`) before being pushed to stack/registers.
2. **Type Disregard by `printf`:** `printf` does not inspect the original variable's source type; it simply decodes the promoted bit pattern in CPU register/stack according to the format specifier (`%d`, `%u`, etc.).

---

## Related Notes
- [[C Integer Conversion & Printf Formatting Case Studies]]
- [[Integer Promotion Rules in C]]
- [[Function Declarations, Prototypes & Standards Evolution]]

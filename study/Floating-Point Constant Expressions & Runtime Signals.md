---
tags:
  - clang
  - c-language
  - floating-point
  - study
---


Floating-point operations evaluated inside static or global initializers are resolved at translation time by the compiler under IEEE 754 rules.

---

## Static Scope vs Local Scope Behavior

### Translation-Time Evaluation (Static / Global Scope)
Evaluated compile-time; does **not** raise runtime hardware exceptions or signals:

```c
static float lol = 0.0f / 0.0f; // Evaluated at compile time: assigns NaN (No runtime signal)
```

### Runtime Evaluation (Local Automatic Scope)
Evaluating the exact same expression inside automatic (local) scope executes dynamically at runtime and can trigger hardware floating-point exceptions (`SIGFPE`):

```c
void test(void) {
    float lol = 0.0f / 0.0f; // Executed dynamically: may trigger SIGFPE hardware trap
}
```


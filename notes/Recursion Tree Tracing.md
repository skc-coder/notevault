---
tags:
  - clang
  - c-language
  - recursion
  - study
---
When tracing recursive execution paths, especially those involving persistent side effects (like `static` variables or global state), adopt systematic tree-tracing rules.

---

## Systematic Tree-Tracing Rules

1. **Side-Effect Chronology:**
   - Never evaluate `static` variables prematurely. Evaluate them in strict, real-time sequential order as each activation frame executes.
   - If a `static` variable is read *after* a child recursive call returns, read its **updated value** (as altered by the recursive descent), not its old state upon function entry.
1. **Structural Execution Ordering:**
   - Statements executed **before** the recursive call branch to the **left** of the recursive node.
   - Statements executed **after** the recursive call branch to the **right** of the recursive node.
3. **Traversal Semantics:**
   - **Pre-order Traversal:** Print/evaluation statements executed before recursive calls (top-down execution).
   - **Post-order Traversal:** Unwinding phases and return value combinations (bottom-up back-tracking).
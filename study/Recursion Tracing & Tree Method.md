## 1. Tracing Recursion: The Tree Method

When tracing recursive execution paths, especially those involving persistent side effects (like `static` variables or global state), adopt systematic tree-tracing rules:

1. **Side-Effect Chronology:**
   * Never evaluate `static` variables prematurely. Evaluate them in strict, real-time sequential order as each activation frame executes.
   * If a `static` variable is read after a child recursive call returns, read its **updated value** (as altered by the recursive descent), not its old state upon function entry.
2. **Structural Execution Ordering:**
   * Statements executed **before** the recursive call branch to the **left** of the recursive node.
   * Statements executed **after** the recursive call branch to the **right** of the recursive node.
3. **Traversal Semantics:**
   * **Pre-order Traversal:** Corresponds to print/evaluation statements executed before recursive calls (top-down, forward execution).
   * **Post-order Traversal:** Corresponds to unwinding phases and return value combinations (bottom-up, back-tracking execution).

---

## 2. Activation Stack Frames

Each recursive function call allocates a new activation frame on the **Stack Segment**, containing:
* Local automatic variables (`auto`)
* Parameter values passed to the function
* The return memory address pointing back to the caller

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->

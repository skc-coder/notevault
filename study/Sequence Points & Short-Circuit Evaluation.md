## 1. Sequence Points Definition

> [!definition] Sequence Point
> A sequence point defines a point in the program's execution where all side effects of previous evaluations are guaranteed to be complete, and no side effects from subsequent evaluations have yet taken place.

### Canonical Sequence Points
1. The end of a full expression terminated by a semicolon (`;`).
2. The logical AND (`&&`) and logical OR (`||`) operators (after evaluating the first operand).
3. The comma operator (`,`) (after evaluating the left operand).
4. The condition expression in a ternary operation (`? :`) before evaluating either branch.
5. Right before a function call executes (after all arguments have been evaluated).

---

## 2. Short-Circuit Evaluation Guarantees

Logical operators evaluate strictly from left to right and introduce an explicit sequence point between operand evaluations:

* In $E_1 \ \&\&\ E_2$: $E_1$ is evaluated first. If $E_1 = 0$, $E_2$ is **never** evaluated.
* In $E_1 \ \|\|\ E_2$: $E_1$ is evaluated first. If $E_1 \ne 0$, $E_2$ is **never** evaluated.

```c
int i = 1;
if (i++ && i == 1) {
    // Execution trace:
    // 1. i++ evaluates to 1 (true).
    // 2. A sequence point is passed; the side effect commits: i becomes 2.
    // 3. Right operand evaluates: i == 1 -> 2 == 1 -> evaluates to 0 (false).
    // The entire condition evaluates to false (0).
}
```

```c
int i = 0, j = 1, k = 2;
int result = i++ || j++ || k++;
// i++ evaluates to 0, side effect i=1.
// j++ evaluates to 1, side effect j=2. Expression becomes true.
// k++ is SHORT-CIRCUITED (skipped entirely).
// Final state: i=1, j=2, k=2, result=1.
```

---

## 3. Undefined Behavior Traps

> [!trap] Undefined Behavior Between Sequence Points
> Modifying a scalar variable more than once between two consecutive sequence points, or reading it to determine both its value and store a new value without an intervening sequence point, results in **Undefined Behavior (UB)**:
> 
> ```c
> arr[i] = i++;      // Undefined Behavior: unsequenced modification and access of i
> f(i++, i++);       // Undefined Behavior: unsequenced modifications of i
> i = ++i + 1;       // Undefined Behavior: multiple unsequenced writes to i
> ```

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->

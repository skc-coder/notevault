## 1. Pointer Basics & Addressability

A pointer variable stores the memory address of an object. Address size is uniform across compilation targets ($4$ bytes on 32-bit systems, $8$ bytes on 64-bit systems).

> [!property] Uniformity of Pointer Sizing
> $$\text{sizeof}(\text{int}*) = \text{sizeof}(\text{char}*) = \text{sizeof}(\text{double}*) = \text{sizeof}(\text{void}*) = 8 \text{ bytes (64-bit)}$$

> [!trap] Non-Addressable Operands
> The unary address-of operator `&` requires an addressable lvalue. It is a compile-time error to apply `&` to literal constants (`&125`), expressions (`&(x + y)`), or `register` variables.

---

## 2. Array Representation & The Array Decay Rule

> [!definition] Array Decay Rule
> In almost all value contexts and expressions, an expression of array type `T[N]` automatically converts (**decays**) into a pointer to its first element:
> $$\text{Array of type } T[N] \xrightarrow{\text{decay}} \text{Pointer of type } T*$$

### The Three Exceptions to Array Decay
1. **Operand of `sizeof`:** `sizeof(arr)` yields total memory footprint: $N \times \text{sizeof}(T)$.
2. **Operand of Unary `&` (Address-Of):**
   * `arr` decays to `T*` (pointer to first element).
   * `&arr` yields a pointer to the **entire array block**, type `T (*)[N]`.
   * Stride difference: `arr + 1` advances by $\text{sizeof}(T)$; `&arr + 1` advances by $N \times \text{sizeof}(T)$.
3. **String Literal Initialization:** `char str[] = "hello";` initializes array memory directly.

---

## 3. Array Indexing & Pointer Arithmetic

> [!property] Commutative Equivalence of Array Subscripting
> The array subscript operator `[]` is defined strictly by pointer arithmetic:
> $$E_1[E_2] \equiv *(\,(E_1) + (E_2)\,)$$
> $$\text{arr}[i] \equiv *( \text{arr} + i ) \equiv *( i + \text{arr} ) \equiv i[\text{arr}]$$

### Pointer Distance & Comparison
> [!definition] The One-Past-The-End Rule
> Pointer arithmetic and comparisons are valid across index $0$ to $N-1$, plus the **one-past-the-end** index $N$. Dereferencing index $N$ or calculating addresses beyond $N$ is **Undefined Behavior (UB)**.

$$\text{end} - \text{start} = N \quad (\text{for pointers to index } N \text{ and } 0)$$

---

## 4. `sizeof` Operator Mechanics

* In standard C (non-VLA), `sizeof` operand is **unevaluated** at runtime.
* `sizeof(i++)` leaves `i` unmodified.
* Floating literals default to `double`: `sizeof(1.3) == 8`.

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->

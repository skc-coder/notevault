## 1. Multidimensional Arrays

Multidimensional arrays are stored in contiguous flat linear memory in **row-major order** (rightmost index changes most rapidly).

### Decay Hierarchy in Multidimensional Arrays
When a multidimensional array decays, only the outermost dimension is stripped away:
* `int a[5]` decays to `int *`.
* `int a[5][6]` decays to `int (*)[6]` (pointer to an array of 6 integers), **never** `int **`.
* Function parameter passing requires all dimensions except the first:
  ```c
  void process(int arr[][6]); // Valid
  ```

$$\text{Address of } arr[i][j] = \text{Base} + (i \cdot N + j) \cdot \text{sizeof}(\text{element})$$

---

## 2. Function Pointers & Canonical Invocation

In C, function names decay to function pointers, and dereferencing them resolves back to the function:

```c
void greet(void) { /* ... */ }

void (*fp)(void) = greet;
fp();       // Direct invocation
(*fp)();    // Explicit dereference invocation
(**fp)();   // Redundant dereference (fp == *fp == **fp)
```

---

## 3. Complex Declarations & The Clockwise/Spiral Rule

To parse complex declarations, start from the identifier and spiral outward clockwise, adhering to operator precedence:
* `[ ]`: Array of...
* `( )`: Function returning...
* `*`: Pointer to...

```c
int (*fp1)(int);
// fp1 is a pointer (*) to a function taking (int) returning int

int (*apa[5])[10];
// apa is an array [5] of pointers (*) to an array [10] of int
```

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->

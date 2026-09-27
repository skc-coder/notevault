> [!question] GATE IT 2006: Multidimensional Pointer Indirection
> Analyze the pointer dereferencing sequence in the following program[cite: 1]:
> 
> ```c
> int a1[] = {6, 7, 8, 18, 34, 67};
> int a2[] = {23, 56, 28, 29};
> int a3[] = {-12, 27, 31};
> int *a[] = {a1, a2, a3};
> 
> void print(int **a) {
>     printf("%d ", a[0][2]);
>     printf("%d ", *a[2]);
>     printf("%d ", *++a[0]);
>     printf("%d ", *(++a)[0]);
>     printf("%d\n", a[-1][+1]);
> }
> 
> int main() {
>     print(a);
>     return 0;
> }
> ```
> 
> **Memory Map:**
> * `a1` (Base 100): `[6, 7, 8, 18, 34, 67]`
> * `a2` (Base 200): `[23, 56, 28, 29]`
> * `a3` (Base 300): `[-12, 27, 31]`
> * `a` (Base 1000): `[100, 200, 300]` (array of `int*`)
> 
> **Instruction Trace:**
> 1. `a[0][2]`:
>    * `a[0]` is `a1` (address 100).
>    * `a1[2]` is the 3rd element: **`8`**[cite: 1].
> 2. `*a[2]`:
>    * `a[2]` is `a3` (address 300).
>    * `*a3` accesses `a3[0]`: **`-12`**[cite: 1].
> 3. `*++a[0]`:
>    * Array subscription `[]` binds tighter than prefix `++`. Expression parses as `*(++(a[0]))`.
>    * `a[0]` (originally holding 100) is pre-incremented: `100 + sizeof(int) = 104` (now points to `a1[1]`).
>    * Dereferencing gives `*104` = **`7`**[cite: 1].
> 4. `*(++a)[0]`:
>    * Evaluates `++a`: pointer `a` is incremented to point to `&a[1]` (address 1008).
>    * `a[0]` now accesses `*(a + 0)` relative to the new base $\implies$ `a2` (address 200).
>    * `*a2` accesses `a2[0]`: **`23`**[cite: 1].
> 5. `a[-1][+1]`:
>    * Since `a` currently points to `&a[1]`, `a[-1]` refers back to `&a[0]`.
>    * Remember from Step 3 that `a[0]` was permanently updated to point to address 104 (`&a1[1]`).
>    * Therefore, `(a[-1])[1]` resolves to `*(104 + 1)` which is `&a1[2]`.
>    * Value at `a1[2]` = **`8`**[cite: 1].
> 
> **Output:**
> ```text
> 8 -12 7 23 8
> ```

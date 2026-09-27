> [!question] Self-Referential Struct Pointer Traversal
> Determine the output of the following pointer manipulation code[cite: 1]:
> 
> ```c
> struct s1 {
>     char *z;
>     int i;
>     struct s1 *p;
> };
> 
> int main() {
>     static struct s1 a[] = {
>         {"Nagpur", 1, a + 1},
>         {"Raipur", 2, a + 2},
>         {"Kanpur", 3, a}
>     };
> 
>     struct s1 *ptr = a;
> 
>     printf("%s ", ++(ptr->z));
>     printf("%s ", (++ptr)->z);
>     printf("%s\n", (ptr->p)->z);
> 
>     return 0;
> }
> ```
> 
> **Step-by-Step Derivation:**
> 1. `++(ptr->z)`:
>    * `ptr` points to `a[0]`. `ptr->z` points to string `"Nagpur"`.
>    * Prefix `++` increments the `char*` pointer by 1 byte, pointing to `"agpur"`.
>    * Prints: **`agpur`**[cite: 1].
> 2. `(++ptr)->z`:
>    * `ptr` is incremented first, now pointing to `a[1]`.
>    * Accesses `a[1].z` which holds `"Raipur"` (or `"Kanpur"` depending on rotation).
>    * Prints: **`Raipur`** (or **`Kanpur`**)[cite: 1].
> 3. `(ptr->p)->z`:
>    * `ptr->p` follows the self-referential link from `a[1]` to `a[2]`.
>    * Accesses `a[2].z` which holds `"Kanpur"`.
>    * Prints: **`Kanpur`**[cite: 1].
> 
> **Output:**
> ```text
> agpur Raipur Kanpur
> ```

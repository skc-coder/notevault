> [!theorem] Structure Copying Semantics
> In C, the assignment operator (`=`) between two variables of the **same structure type** performs a bitwise / member-by-member **shallow copy**[cite: 1]:
> 
> ```c
> struct n {
>     int a;
>     int b;
> };
> 
> struct n x1, x2;
> x1.a = 10;
> x1.b = 20;
> x2 = x1; /* Perfectly legal: copies all member values from x1 to x2 */
> ```

> [!trap] Structure Direct Equality Comparison Error
> In C, direct equality operators (`==` and `!=`) are **not defined** for structure types[cite: 1]:
> 
> ```c
> if (x1 == x2) { ... } /* COMPILE TIME ERROR! */
> ```
> 
> **Why?**
> * Memory alignment padding bytes may contain uninitialized garbage values. A raw memory comparison (`memcmp`) could evaluate to false even if all logical members are identical.
> * Language philosophy: C does not provide automatic deep or shallow structure comparison operators.
> 
> **Correct Approach:** Compare each member individually[cite: 1]:
> ```c
> if (x1.a == x2.a && x1.b == x2.b) {
>     /* Structures are logically equal */
> }
> ```

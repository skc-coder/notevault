> [!question] Struct Array String Traversal
> Trace the output of the following pointer code[cite: 1]:
> 
> ```c
> struct test {
>     int i;
>     char *c;
> } st[] = {
>     {5, "become"},
>     {4, "better"},
>     {6, "jungle"},
>     {8, "ancestor"},
>     {7, "brother"}
> };
> 
> int main() {
>     struct test *p = st;
> 
>     printf("%s ", (p++)->c + 1);
>     printf("%c ", *++p->c);
>     printf("%d ", p[0].i);
>     printf("%s\n", p->c);
> 
>     return 0;
> }
> ```
> 
> **Step-by-Step Derivation:**
> 1. `(p++)->c + 1`:
>    * `p` initially points to `st[0]`.
>    * `(p++)->c` yields `st[0].c` (`"become"`)[cite: 1].
>    * Pointer offset `+ 1` points to `"become" + 1`, which is the string starting at the second character: **`ecome`** (or **`etter`** depending on array binding)[cite: 1].
>    * Note: In the lecture notebook handwriting: `p++->c` evaluated over `st[1]` prints **`etter`**[cite: 1].
>    * Side-effect: `p` increments to point to `st[1]`[cite: 1].
> 2. `*++p->c`:
>    * `->` has higher precedence than unary prefix `++` and dereference `*`[cite: 1].
>    * Expression parses as `*(++(p->c))`[cite: 1].
>    * `p` currently points to `st[1]`. `p->c` originally points to `"better"` (or `"jungle"`)[cite: 1].
>    * Increments the pointer `st[1].c` by 1 character, and dereferences the character at that position: produces **`u`**[cite: 1].
> 3. `p[0].i`:
>    * Array indexing `p[0]` denotes the current element pointed to by `p` (`st[2]`)[cite: 1].
>    * Prints the integer field: **`6`**[cite: 1].
> 4. `p->c`:
>    * Prints the remainder of string `st[2].c`: **`ungle`**[cite: 1].

> [!question] GATE CSE 2018: String Pointer Array Manipulation
> Determine the output printed by the following program[cite: 1]:
> 
> ```c
> int main() {
>     char *s[] = {"ice", "green", "cone", "please"};
>     char **ptr[] = {s + 3, s + 2, s + 1, s};
>     char ***p = ptr;
> 
>     printf("%s ", **++p);
>     printf("%s ", *--*++p + 3);
>     printf("%s ", *p[-2] + 3);
>     printf("%s\n", p[-1][-1] + 1);
> 
>     return 0;
> }
> ```
> 
> **Memory Setup:**
> * `s[0] = "ice"`, `s[1] = "green"`, `s[2] = "cone"`, `s[3] = "please"`[cite: 1].
> * `ptr[0] = &s[3]`, `ptr[1] = &s[2]`, `ptr[2] = &s[1]`, `ptr[3] = &s[0]`[cite: 1].
> * `p = &ptr[0]`[cite: 1].
> 
> **Evaluation Trace:**
> 1. `**++p`:
>    * `++p` advances `p` to `&ptr[1]`.
>    * `*p` is `ptr[1]` which is `s + 2` (`&s[2]`).
>    * `**p` is `s[2]` $\implies$ `"cone"`.
>    * Prints: **`cone`**[cite: 1].
> 2. `*--*++p + 3`:
>    * `++p` advances `p` to `&ptr[2]` (which stores `s + 1`).
>    * `*p` evaluates to `ptr[2]`.
>    * `--(*p)` decrements `ptr[2]` from `s + 1` to `s` (`&s[0]`).
>    * `*(--(*p))` evaluates to `s[0]` (`"ice"`).
>    * `"ice" + 3` offsets the pointer to the terminating null byte `'\0'`.
>    * Prints: **(empty string / nothing)**[cite: 1].
> 3. `*p[-2] + 3`:
>    * `p` currently resides at `&ptr[2]`.
>    * `p[-2]` accesses `ptr[0]` which holds `s + 3` (`&s[3]`).
>    * `*p[-2]` is `s[3]` (`"please"`).
>    * `"please" + 3` offsets 3 characters forward: `p`, `l`, `e`, then `ase`.
>    * Prints: **`ase`**[cite: 1].
> 4. `p[-1][-1] + 1`:
>    * `p` is at `&ptr[2]`. `p[-1]` accesses `ptr[1]` which points to `s + 2`.
>    * `(ptr[1])[-1]` accesses `*( (s + 2) - 1 ) = s[1]` (`"green"`).
>    * `"green" + 1` offsets 1 character forward: `"reen"`.
>    * Prints: **`reen`**[cite: 1].
> 
> **Complete Output:**
> ```text
> cone ase reen
> ```

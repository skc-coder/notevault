> [!definition] Character I/O Primitives
> Standard C library functions for raw character input and output:
> 
> * **`getchar()`:** Reads the next available character from standard input (`stdin`)[cite: 1]:
>   ```c
>   c = getchar(); /* Functionally equivalent to: scanf("%c", &c); */
>   ```
> * **`putchar(c)`:** Writes the single character `c` to standard output (`stdout`)[cite: 1]:
>   ```c
>   putchar(c);    /* Functionally equivalent to: printf("%c", c); */
>   ```

> [!trap] The `EOF` Sentinel Constant
> `getchar()` returns an `int` rather than a `char` so it can accommodate the integer sentinel value `EOF` (End-of-File, commonly defined as `-1`)[cite: 1].
> * In interactive terminal sessions, `EOF` is triggered via keyboard signals:
>   * **Linux / macOS:** `Ctrl + D`
>   * **Windows:** `Ctrl + Z`[cite: 1]

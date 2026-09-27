## Return-by-Value Struct Execution
Trace the output of the following C program[cite: 1]:

```c
struct student {
    char *name;
};

struct student s;

struct student fun() {
    s.name = "newton";
    printf("%s\n", s.name);
    s.name = "alan";
    return s;
}

int main() {
    struct student m = fun();
    printf("%s\n", m.name);
    m.name = "turing";
    printf("%s\n", s.name);
    printf("%s\n", m.name);
    return 0;
}
```

**Detailed Execution Step-by-Step:**
1. `s` is a global variable of type `struct student`[cite: 1].
2. In `main()`, `fun()` is called[cite: 1].
3. Inside `fun()`:
   * `s.name` is assigned the literal `"newton"`[cite: 1].
   * `printf("%s\n", s.name)` prints: **`newton`**[cite: 1].
   * `s.name` is updated to point to `"alan"`[cite: 1].
   * `return s;` returns a copy of the structure where `name` points to `"alan"`[cite: 1].
4. In `main()`, the local variable `m` receives the returned struct value: `m.name` holds the pointer to `"alan"`[cite: 1].
5. `printf("%s\n", m.name)` prints: **`alan`**[cite: 1].
6. `m.name = "turing";` modifies the local struct variable `m`. It does **not** alter global variable `s`[cite: 1]. 
7. `printf("%s\n", s.name)` prints: **`alan`**[cite: 1].
8. `printf("%s\n", m.name)` prints: **`turing`**[cite: 1].

**Final Program Output:**
```text
newton
alan
alan
turing
```

## The main thing
Before executing `m.name = "turing"` in main, both `m.name` and `s.name` point to the same read only string `alan`. But after that they point at different strings.
In general, `x = "string` changes the data pointed by `x`.
`strcpy(m.name, "turing")` is used to write inplace over the writable string pointed by `m.name`.
> [!formula] Member Selection Syntax
> Direct structure variables use the dot operator (`.`):
> ```c
> var_name.member_name
> ```
> Pointers to structures use either dereference plus dot or the direct arrow operator (`->`):
> ```c
> (*ptr).member_name == ptr->member_name
> ```

### Operator Precedence and Associativity Rules

| Rank | Operators | Associativity | Category |
| :---: | :--- | :---: | :--- |
| **1 (Highest)** | `()`, `[]`, `->`, `.`, post `++`, post `--`[cite: 1] | Left to Right | Postfix / Member Selection[cite: 1] |
| **2** | Unary `+`, Unary `-`, `!`, `~`, pre `++`, pre `--`, `*` (deref), `&` (addr), `sizeof`[cite: 1] | Right to Left | Prefix / Unary Operators[cite: 1] |

> [!trap] Dereference vs. Member Selection Precedence
> Because `.` and `->` (precedence 1) rank higher than unary `*` (precedence 2), parenthesis enclosure is mandatory when dereferencing structure pointers via the dot syntax[cite: 1]:
> 
> $$*ptr.member \equiv *(ptr.member) \quad (\text{Attempts dereferencing the member itself!}) \text{[cite: 1]}$$
> $$(\ast ptr).member \equiv ptr \to member \quad (\text{Correctly accesses member through pointer}) \text{[cite: 1]}$$
> 
> Conversely, `*(t.ptr_member)` does not strictly need parentheses because `.` evaluates before `*`, making `*t.ptr_member` evaluate identically to `*(t.ptr_member)`[cite: 1].

### Pointer to Structure Demonstration

```c
struct book_bank {
    char author[30];
    int pages;
};

struct book_bank b1;
struct book_bank *bptr = &b1;

/* Three equivalent ways to access member 'author': */
b1.author;          /* 1. Direct variable dot access */
(*bptr).author;     /* 2. Dereferenced pointer dot access */
bptr->author;       /* 3. Pointer arrow access */
```

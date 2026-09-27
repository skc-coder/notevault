> [!definition] Structure (`struct`)
> A **structure** in C is a user-defined composite data type used for grouping logically related heterogeneous data items under a single variable name[cite: 1].
> * Individual variables declared inside a structure are termed its **members**[cite: 1].
> * Common use cases: Representing entities such as Student records (`name`, `marks`, `age`), Book inventory (`title`, `author`, `pages`, `price`), or mathematical types like Complex numbers (`real`, `imag`)[cite: 1].

### Syntax and Declaration Styles

```c
/* Style 1: Declaration with Structure Tag */
struct book_bank {
    char title[30];
    char author[30];
    int pages;
    float price;
};

/* Variable instantiation */
struct book_bank b1, b2, b3;

/* Style 2: Declaring variables directly with the struct definition */
struct book_bank {
    char title[30];
    char author[30];
    int pages;
    float price;
} b1, b2, b3;
```

> [!theorem] Type Alias via `typedef`
> The `typedef` keyword creates a synonym or alias for existing primitive or user-defined types[cite: 1]:
> ```c
> typedef type new_name;
> ```
> For structures, `typedef` eliminates the requirement of repeatedly typing the `struct` keyword during variable instantiation[cite: 1].

```c
/* Approach A: Two-step typedef */
struct book_bank {
    char title[20];
    float price;
};
typedef struct book_bank Books;
Books b1, b2, b3; /* Equivalent to: struct book_bank b1, b2, b3; */

/* Approach B: Compact inline typedef definition */
typedef struct book_bank {
    char title[20];
    float price;
} Books;

/* Approach C: Anonymous struct typedef */
typedef struct {
    char title[20];
    float price;
} Books; /* Here the struct tag is omitted; 'Books' is the alias */
```

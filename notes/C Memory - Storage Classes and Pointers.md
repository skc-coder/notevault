[!definition] Storage Classes dictate the storage location, scope, initial default value, and lifetime of variables in C:
auto: Allocated on the Stack; function-local scope; indeterminate/garbage initial value; destroyed upon block exit.
register: Stored in CPU registers (if available); address-of operator & cannot be applied; local lifetime.
static: Allocated in the Data Segment (BSS if uninitialized, Data if initialized); retains its value across function invocations; initialized exactly once at program startup.
extern: Global reference; points to an existing variable declared elsewhere; does not allocate new physical memory.

Storage Class
Location
Default Value
Scope
Lifetime
auto
Stack Frame
Garbage
Local Block
Function Execution
register
CPU Register / RAM
Garbage
Local Block
Function Execution
static
Data Segment (.data / .bss)
Zero (0)
Local to Block / File
Program Lifetime
extern
Data Segment
Zero (0)
Global / Multiple Files
Program Lifetime

[!theorem] Pointer Dereferencing Equivalences: For an array A and index i:

$$A[i] \equiv *(A + i) \equiv *(i + A) \equiv i[A]$$

For a 2D array char s[3][5]:

$$*(*(p + i) + j) \equiv p[i][j]$$

Base address decays: s decays to a pointer to an array of 5 characters (char (*)[5]), whereas s[0] is a pointer to the first character (char *).
[!trap]
Dangling Pointer vs. Memory Leak:
Dangling Pointer: A pointer pointing to memory that has been deallocated (e.g., returning the address of a local automatic stack variable)[cite: 11].
Memory Leak: Occurs when dynamically allocated heap memory (malloc/calloc) is no longer referenced by any pointer and was never released using free()[cite: 11].
[!question] PSU CBT Practice Drill: What is the output of the following C program?



C
#include <stdio.h>
int main() {
    char *a[] = {"ABC", "DEF", "GHI", "JKL"};
    char **p = a;
    printf("%c%c %s", *(*(p + 1) + 2), *(*(p + 3)), *(p + 2) + 1);
    return 0;
}


(A) FJ HI
(B) FJ GH
(C) EJ HI
(D) FK HI
Step-by-Step Resolution:
a is an array of pointers to string literals: a[0]="ABC", a[1]="DEF", a[2]="GHI", a[3]="JKL".
p points to a[0].
First format specifier %c:
$$*(*(p + 1) + 2) \equiv *(a[1] + 2) = *(\text{"DEF"} + 2) = \text{'F'}$$


Second format specifier %c:
$$*(*(p + 3)) \equiv *(a[3] + 0) = *(\text{"JKL"}) = \text{'J'}$$


Third format specifier %s:
$$*(p + 2) + 1 \equiv a[2] + 1 = \text{"GHI"} + 1 = \text{"HI"}$$


Concatenating: 'F', 'J', space, "HI" $\rightarrow$ FJ HI.
Correct Answer: (A) FJ HI

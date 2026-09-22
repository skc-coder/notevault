> [!definition]
> * **Static Scoping (Lexical Scoping):** Variable binding is determined strictly at compile-time by the physical structure and block nesting of the source code. If an identifier is not local, the compiler searches the enclosing lexical parent up to the global scope.
> * **Dynamic Scoping:** Variable binding is resolved at runtime based on the dynamic chain of function activations (call stack). A non-local variable resolves to the most recent binding along the calling sequence.

```mermaid
flowchart TD
    subgraph Execution Chain: main calls A, A calls B
        M["main()"] -->|"calls"| FA["A()"]
        FA -->|"calls"| FB["B()"]
    end
    subgraph Scope Resolution for Free Variable in B
        FB -.->|"Static Scoping (Lexical)"| G["Global Scope"]
        FB -.->|"Dynamic Scoping (Call Stack)"| FA
    end


[!theorem]
Resolution Invariant:
Under Static Scope, local declarations in calling functions are invisible to the callee unless the callee is lexically nested inside them[cite: 11, 13].
Under Dynamic Scope, if a function defines a local variable with the same name, any function called downstream accesses that local variable instead of the global instance[cite: 11, 13].
[!trap] Parameter Re-binding Trap: Global variable modifications inside functions executing under dynamic scope update the caller's active frame variable if shadowed, leaving the global variable unaffected. Always trace the exact caller stack hierarchy[cite: 11, 13].
[!question] PSU CBT Practice Drill: Consider the program below executed under (i) Static Scoping and (ii) Dynamic Scoping:



C
int a = 5, b = 10;
void B() {
    printf("%d %d\n", a, b);
}
void A() {
    int b = 30;
    B();
}
int main() {
    int a = 20;
    A();
    return 0;
}


What are the printed values of a and b?
Step-by-Step Resolution:
Static Scoping Analysis:
Function B() does not declare a or b.
Its enclosing scope is the global file scope[cite: 11, 13].
Global a = 5, global b = 10.
Static Output: 5 10.
Dynamic Scoping Analysis:
Call Stack: main() $\rightarrow$ A() $\rightarrow$ B().
Function B() checks its own frame: neither a nor b found.
Checks caller A()'s frame: finds local b = 30. No a defined in A().
Checks caller main()'s frame: finds local a = 20.
Dynamic Output: 20 30.
Conclusion: Static = 5 10, Dynamic = 20 30.

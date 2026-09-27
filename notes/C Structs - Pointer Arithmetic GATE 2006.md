> [!question] GATE 2006: Struct Pointer Increments
> Trace the following program carefully[cite: 1]:
> 
> ```c
> struct student {
>     int n;
> };
> 
> int main() {
>     struct student s[4];
>     s[0].n = 10;
>     s[1].n = 20;
>     s[2].n = 30;
>     s[3].n = 40;
> 
>     struct student *m = s;
> 
>     printf("%d ", (m++)->n);
>     printf("%d ", m->n);
>     printf("%d ", (*m++).n);
>     printf("%d ", m->n);
>     printf("%d ", (++m)->n);
>     printf("%d\n", m->n);
> 
>     return 0;
> }
> ```
> 
> **Step-by-Step Derivation:**
> * `s` array occupies indices `0, 1, 2, 3` with `.n` values `10, 20, 30, 40` respectively[cite: 1].
> * Initially, `m = &s[0]` (address 100)[cite: 1].
> 
> 1. `printf("%d ", (m++)->n);`:
>    * Postfix increment evaluates with current `m` (`&s[0]`)[cite: 1].
>    * Accesses `s[0].n` = **10**[cite: 1].
>    * Side-effect: `m` advances to `&s[1]` (address 104)[cite: 1].
> 2. `printf("%d ", m->n);`:
>    * Evaluates `m->n` with `m = &s[1]` $\implies$ **20**[cite: 1].
> 3. `printf("%d ", (*m++).n);`:
>    * Postfix `++` has higher precedence than `*`. It evaluates the old pointer value `&s[1]`, dereferences it to `s[1]`, and accesses `.n` = **20**[cite: 1].
>    * Side-effect: `m` advances to `&s[2]` (address 108)[cite: 1].
> 4. `printf("%d ", m->n);`:
>    * Evaluates `m->n` with `m = &s[2]` $\implies$ **30**[cite: 1].
> 5. `printf("%d ", (++m)->n);`:
>    * Prefix `++` increments `m` first. `m` advances from `&s[2]` to `&s[3]` (address 112)[cite: 1].
>    * Evaluates `s[3].n` = **40**[cite: 1].
> 6. `printf("%d\n", m->n);`:
>    * Evaluates current `m->n` (`s[3].n`) $\implies$ **40**[cite: 1].
> 
> **Complete Output Sequence:**
> ```text
> 10 20 20 30 40 40
> ```


question: print(++i) does it print i or i+1? 
print(++*m++) where m is a pointer?
print(++m++-->n)?

### 1. Does `printf("%d", ++i)` print `i` or `i + 1`?

It prints **`i + 1`** (the new, incremented value).

  

- **Prefix `++i`:** Increments the variable first, and the expression evaluates to the updated value.
    
      
    
- **Postfix `i++`:** Evaluates to the old value first, then increments the variable as a side effect.
    
      
    

### 2. Tracing `printf("%d", ++*m++)` where `m` is a pointer

To parse this expression, apply C operator precedence and associativity rules:

  

1. **Rank 1 (Postfix):** Postfix `++` binds tightest and associates left-to-right (`m++`).
    
      
    
2. **Rank 2 (Unary/Prefix):** Dereference `*` and prefix `++` have equal precedence and associate **right-to-left** (`<-`).
    
      
    

#### Expression Parsing:

C

```
++*m++  ===>  ++(*(m++))
```

#### Step-by-Step Execution:

1. **`m++`:** Evaluates to the **current address** stored in `m`. As a side effect, `m` is scheduled to increment by $\text{sizeof}(*m)$ to point to the next element.
    
      
    
2. **`*(m++)`:** Dereferences the **original address** of `m`, yielding the lvalue of the object originally pointed to.
    
      
    
3. **`++(...)`:** Applies prefix increment directly to the value stored inside that object, incrementing its value by 1.
    
      
    
4. **Evaluation:** The expression evaluates to the **newly incremented numerical value** inside the original target object.
    
      
    
5. **Pointer state:** `m` now points to the next memory element.
    
      
    

C

```
// Concrete Example:
int arr[] = {10, 20};
int *m = arr;

printf("%d\n", ++*m++); // Prints 11 (arr[0] becomes 11)
printf("%d\n", *m);     // Prints 20 (m advanced to &arr[1])
```

### 3. Tracing `printf("%d", ++m++->n)`

This expression triggers a **compile-time error** (syntax/lvalue error).

  

#### Operator Binding:

1. **Rank 1 (Postfix):** Both arrow `->` and postfix `++` sit at Priority Rank 1 and associate **left-to-right**.
    
      
    - Therefore, `m++->n` groups as:
        
          
        
        $$(m++)->n$$
        
2. **Rank 2 (Prefix):** Prefix `++` now attempts to bind to that entire result:
    
      
    
    $$++((m++)->n)$$
    
3. **Double Increment on `m`:** Notice the token sequence `++ m ++`.
    
      
    - A variable cannot be both prefix-incremented and postfix-incremented simultaneously in this manner without explicit grouping:
        
          
        - Postfix `++` requires an lvalue. The result of prefix `++m` is not a modifiable lvalue in C: `(++m)++` is an **error**.
            
              
            
        - Conversely, prefix `++` requires an lvalue. While `(m++)->n` evaluates to the integer member `n` (which is an lvalue), having `++m++` consecutively causes the compiler's lexical scanner to group the tokens ambiguously or fail lvalue constraints (`lvalue required as increment operand`).
            
              
            

#### If written as valid, unambiguous variations:

- **Variation A: `++(m->n)` or `++m->n`**
    
      
    - `->` has higher precedence than prefix `++`.
        
          
        
    - Parses as `++(m->n)`.
        
          
        
    - Increments and prints the value of member `.n` without moving `m`.
        
          
        
- **Variation B: `(++m)->n`**
    
      
    - Increments pointer `m` first to point to the next struct, then accesses and prints its `.n` value.
        
          
        
- **Variation C: `(m++)->n`**
    
      
    - Reads and prints `.n` from the currently pointed struct, then advances pointer `m` to the next struct.
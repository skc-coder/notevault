
--atom--
file_name: Top-Down Parsers - LL1 Verification Walkthrough

> [!definition]
> An **$LL(1)$ Grammar** is an unambiguous context-free grammar where the parsing table $M[A, a]$ contains at most one production entry for every non-terminal $A$ and terminal / lookahead $a \in (V_T \cup \{\$\})$.

```mermaid
flowchart TD
    Grammar["Grammar: S -> aS' | S' -> S | e"] --> Step1["1. Compute FIRST and FOLLOW"]
    Step1 --> FirstSets["FIRST(S) = {a}\nFIRST(S') = {a, e}"]
    Step1 --> FollowSets["FOLLOW(S) = {$, a}\nFOLLOW(S') = {$, a}"]
    FirstSets & FollowSets --> Step2["2. Build Parsing Table M"]
    Step2 --> ConflictCheck{"Multiple entries in M[S', a]?"}
    ConflictCheck -- Yes --> NotLL1["FIRST-FOLLOW Conflict: NOT LL(1)"]
````

### Step-by-Step Mathematical Verification

Consider the factored grammar:

  

1. $S \to a S'$
    
      
    
2. $S' \to S$
    
      
    
3. $S' \to \epsilon$
    
      
    

#### 1. FIRST Set Computations

- $\text{FIRST}(S) = \text{FIRST}(a S') = \{a\}$
    
      
    
- For $S'$:
    
      
    - From $S' \to S$: $\text{FIRST}(S) = \{a\}$
        
          
        
    - From $S' \to \epsilon$: $\{\epsilon\}$
        
          
        
    - Therefore: $\text{FIRST}(S') = \{a, \epsilon\}$
        
          
        

#### 2. FOLLOW Set Computations

- Since $S$ is the start symbol, add the end marker:
    
      
    
    $$\$ \in \text{FOLLOW}(S)$$
    
- From $S \to a S'$:
    
      
    - $S'$ sits at the end of the production.
        
          
        
    - By Rule 3: $\text{FOLLOW}(S) \subseteq \text{FOLLOW}(S')$, so $\$ \in \text{FOLLOW}(S')$.
        
          
        
- From $S' \to S$:
    
      
    - $S$ sits at the end of the production.
        
          
        
    - By Rule 3: $\text{FOLLOW}(S') \subseteq \text{FOLLOW}(S)$.
        
          
        
    - This creates a mutual dependency: $\text{FOLLOW}(S) = \text{FOLLOW}(S')$.
        
          
        
- From $S' \to S$ where $S \to a S'$:
    
      
    - Notice that in a derivation $S \Rightarrow a S' \Rightarrow a S \Rightarrow a a S'$, terminal $a$ follows $S$.
        
          
        
    - Thus, $\text{FOLLOW}(S) = \{a, \$\}$ and $\text{FOLLOW}(S') = \{a, \$\}$.
        
          
        

#### 3. LL(1) Condition Evaluation for $S'$

For the two alternate productions of $S'$:

  

- $\alpha_1 = S \implies \text{FIRST}(\alpha_1) = \{a\}$
    
      
    
- $\alpha_2 = \epsilon \implies \text{FIRST}(\alpha_2) = \{\epsilon\}$
    
      
    

Since $\alpha_2 \Rightarrow^* \epsilon$, we must verify the disjoint condition:

  

$$\text{FIRST}(\alpha_1) \cap \text{FOLLOW}(S') = \emptyset$$

Substituting the calculated sets:

  

$$\{a\} \cap \{a, \$\} = \{a\} \neq \emptyset$$

> [!theorem]
> 
> **FIRST-FOLLOW Conflict**: Because $\text{FIRST}(S) \cap \text{FOLLOW}(S') \neq \emptyset$, the table cell $M[S', a]$ receives two competing entries:
> 
>   
> 
> 1. $S' \to S$ (from $\text{FIRST}(S)$)
>     
>       
>     
> 2. $S' \to \epsilon$ (from $\text{FOLLOW}(S')$ due to the $\epsilon$-production)
>     
>       
>     
> 
> Hence, this factored grammar remains **strictly non-$LL(1)$**.
> 
>   

> [!trap]
> 
> Factoring eliminates the immediate $\text{FIRST-FIRST}$ conflict at non-terminal $S$, but shifting the recursion into $S' \to S \mid \epsilon$ converts the issue into a **$\text{FIRST-FOLLOW}$ conflict** at $S'$. Left-factoring alone does not guarantee that an ambiguous language becomes deterministic.
> 
>   

> [!question]
> 
> Given the grammar:
> 
>   
> 
> $$S \to a S', \quad S' \to S \mid \epsilon$$
> 
> Which entries appear in cell $M[S', a]$ of the predictive parsing table?
> 
>   
> 
> - (A) Only $S' \to S$
>     
>       
>     
> - (B) Only $S' \to \epsilon$
>     
>       
>     
> - (C) Both $S' \to S$ and $S' \to \epsilon$
>     
>       
>     
> - (D) No entries (blank error entry)
>     
>       
>     
> 
> **Correct Option**: **(C)**
> 
> **Explanation**: Because $a \in \text{FIRST}(S)$, the production $S' \to S$ is entered into $M[S', a]$. Because $a \in \text{FOLLOW}(S')$ and $S'$ contains an $\epsilon$-production ($S' \to \epsilon$), $S' \to \epsilon$ is also entered into $M[S', a]$. This dual entry constitutes a fatal $\text{FIRST-FOLLOW}$ conflict.

```

---

### Key Takeaway on $\text{FOLLOW}(S')$

You correctly saw that $S'$ is at the end of $S \to a S'$, meaning $S'$ inherits everything in $\text{FOLLOW}(S)$ (starting with $\$$). 

However, because the second rule allows $S' \to S$, $S$ and $S'$ end up mutually inheriting from each other. That brings terminal $a$ into $\text{FOLLOW}(S')$ as well, leading to:
$$\text{FOLLOW}(S') = \{a, \$\}$$

Because $a$ is present in both $\text{FIRST}(S)$ and $\text{FOLLOW}(S')$, table cell $M[S', a]$ receives two competing rules ($S' \to S$ and $S' \to \epsilon$).

Would you like to try constructing the full $2 \times 2$ predictive parsing table for this grammar to see the collision visually, or move on to diagnosing another grammar?
```
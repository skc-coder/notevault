---
tags:
hardness: mid
importance: high
revision: "1"
---
Peterson's Algorithm = flag + turn = intention + politness.
For two processes.

---

## 1. The Polite Roommates: How Peterson's Works

```c
// Shared variables
bool flag[2] = {false, false};
int turn = 0;

// Process Pi (i ∈ {0, 1}, peer j = 1 - i)
flag[i] = true;
turn = j;
while (flag[j] && turn == j);

/* Critical Section */

flag[i] = false;

/* Remainder Section */
```

Two roommates, Peter and Jerry, share one bathroom.

1. **Raise your hand:** Peter shouts, *"I want the bathroom!"*
2. **Be polite:** Peter immediately adds, *"After you, Jerry!"*
3. **Wait outside only if:**
   - Jerry also wants to go, **and**
   - Peter was the last one to say *"After you!"*
4. **Use the loo:** If Jerry never asked, or Jerry was the last one to say *"After you!"*, Peter walks right in.
5. **Leave:** Peter finishes and shouts, *"I'm done!"*

 The Rule
> Whoever is polite **last** waits. The other goes in first.
---

## 2. Order matters

> [!trap] Swapping Peterson's Entry Statements
> If process $P_i$ executes `turn = j` **before** `flag[i] = true`:
> 1. $P_0$ sets `turn = 1` and is preempted.
> 2. $P_1$ sets `turn = 0`, sets `flag[1] = true`, checks `flag[0]` (which is still `false`), skips the while loop, and enters the CS.
> 3. $P_0$ resumes, sets `flag[0] = true`, checks `while (flag[1] && turn == 1)`. Since `turn == 0` (overwritten by $P_1$), the while condition evaluates to `false`.
> 4. $P_0$ enters the CS while $P_1$ is still inside. **Mutual Exclusion is violated.**

 The Story 
 1. **Peter shouts:** *"After you, Jerry!"* (but stays in his room without saying he needs to go). 
 2. **Jerry shouts back:** *"No, after you, Peter!"* and announces he is heading to the loo. 
 3. **Jerry checks the hall:** Peter hasn't said he needs to go, so Jerry walks right in. 
 4. **Peter now announces:** *"I need the loo!"* 
 5. **Peter checks:** He remembers Jerry's last words were *"after you, Peter!"*—so Peter walks straight in too. 
 6. **Collision:** Both are in the loo at the same time.

---

## 3. Evaluation of Requirements

- **Mutual Exclusion:** Satisfied ($\boldsymbol{\checkmark}$). Both processes entering simultaneously would require `turn == 0` and `turn == 1` to hold concurrently, which is impossible ($\bot$).
- **Progress:** Satisfied ($\boldsymbol{\checkmark}$). `turn` can only hold one value at a time, ensuring at least one while-condition evaluates to `false`.
- **Bounded Waiting:** Satisfied ($\boldsymbol{\checkmark}$). Upon exiting, $P_0$ sets `flag[0] = false`, allowing $P_1$ to immediately enter. When $P_0$ re-requests entry, it sets `turn = 1`, yielding priority to $P_1$.

## 4. Disadvantages of peterson soln

- slow compared to hardware solutions
- busy wait
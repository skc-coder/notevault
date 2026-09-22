[!definition] Hashing maps large key domains to fixed-size table indices using a hash function $h(k)$.
Collision: Occurs when $h(k_1) = h(k_2)$ for $k_1 \neq k_2$.
Load Factor ($\alpha$): Ratio of stored keys $n$ to table size $m$: $\alpha = \frac{n}{m}$.
Primary Clustering: Formation of long contiguous blocks of occupied slots in linear probing, severely increasing average search time.
Secondary Clustering: Keys hashing to the same initial location trace identical probe sequences in quadratic probing.
[!formula]
Probing Functions ($i = 0, 1, \dots, m-1$):
Linear Probing:
$$h(k, i) = (h(k) + i) \pmod m$$


Quadratic Probing:
$$h(k, i) = (h(k) + c_1 i + c_2 i^2) \pmod m$$


Double Hashing:
$$h(k, i) = (h_1(k) + i \cdot h_2(k)) \pmod m$$

(Constraint: $h_2(k)$ must be relatively prime to $m$, and $h_2(k) \neq 0$).
Search Complexities:
Chaining: Average search time $= O(1 + \alpha)$.
Open Addressing: Unsuccessful search expected probes $= \frac{1}{1 - \alpha}$; Successful search expected probes $= \frac{1}{\alpha} \ln \left(\frac{1}{1 - \alpha}\right)$.

Hashing Collision Method
Primary Clustering
Secondary Clustering
Table Size Constraint
Linear Probing
Severe
Present
$\alpha \le 1$


Quadratic Probing
Eliminated
Present
Prime table size
Double Hashing
Eliminated
Eliminated
$m$ and $h_2(k)$ coprime
Separate Chaining
None
None
Can exceed $\alpha > 1$



[!trap] Load Factor Limit in Open Addressing: In open addressing, the load factor $\alpha$ can never exceed $1.0$. In separate chaining, $\alpha$ can exceed $1.0$ arbitrarily because chains reside in dynamically allocated heap memory outside the table buckets.
[!question]
PSU CBT Practice Drill:
A hash table of size $m = 13$ uses Double Hashing with:

$$h_1(k) = k \pmod{13} \quad \text{and} \quad h_2(k) = 1 + (k \pmod{11})$$

What is the probe sequence for inserting key $k = 41$? (A) 2, 11, 7, 3
(B) 2, 7, 12, 4
(C) 3, 12, 8, 4
(D) 3, 8, 0, 5
Step-by-Step Resolution:
Compute primary hash:
$$h_1(41) = 41 \pmod{13} = 2 \quad (13 \times 3 = 39, \text{ rem } 2)$$


Compute secondary hash step size:
$$h_2(41) = 1 + (41 \pmod{11}) = 1 + (8) = 9 \quad (11 \times 3 = 33, \text{ rem } 8)$$


Generate probe sequence $h(k, i) = (2 + i \times 9) \pmod{13}$:
$i = 0$: $(2 + 0) \pmod{13} = 2$


$i = 1$: $(2 + 9) \pmod{13} = 11$


$i = 2$: $(2 + 18) \pmod{13} = 20 \pmod{13} = 7$


$i = 3$: $(2 + 27) \pmod{13} = 29 \pmod{13} = 3$


Sequence: $2, 11, 7, 3$.
Correct Answer: (A) 2, 11, 7, 3

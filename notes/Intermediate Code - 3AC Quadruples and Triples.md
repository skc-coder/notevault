> [!definition]
> - **Three-Address Code (3AC)**: An intermediate linearization where each statement contains at most one operator on the RHS and references at most three memory addresses.
> - **Static Single Assignment (SSA)**: A strict form of 3AC where **every variable is assigned exactly once**, eliminating name reuse.

> [!formula]
> **Data Structures for 3AC Storage**:
> 1. **Quadruple**: Four explicit record fields:
>    $$\text{Quadruple} = \langle \text{op}, \; \text{arg}_1, \; \text{arg}_2, \; \text{result} \rangle$$
> 2. **Triple**: Eliminates the explicit `result` field. References to previous computations use array indices:
>    $$\text{Triple} = (\text{index}) \; \langle \text{op}, \; \text{arg}_1, \; \text{arg}_2 \rangle$$
> 3. **Indirect Triple**: Stores an ordered array of pointers pointing into a separate unordered table of Triples, decoupling sequence order from position.

| Feature | Quadruples | Triples | Indirect Triples |
| :--- | :--- | :--- | :--- |
| **Field Count** | 4 (`op, arg1, arg2, res`) | 3 (`op, arg1, arg2`) | Pointers to 3-field records |
| **Space Overhead** | Space Inefficient (stores temporary names) | Space Efficient (no temporary names) | Intermediate space |
| **Optimization Flexibility** | Time Efficient (moving instructions requires no pointer updates) | Time Inefficient (moving an instruction requires updating all referencing indices) | Highly Efficient (reordering updates the pointer list only) |

> [!question]
> How many temporary variables are generated in the minimum 3AC representation of $x = (a + b) * (c + d)$?
> - (A) 1
> - (B) 2
> - (C) 3
> - (D) 4
>
> **Correct Option**: **(B)**
> **Step-by-Step Breakdown**:
> 1. $t_1 = a + b$
> 2. $t_2 = c + d$
> 3. $x = t_1 * t_2$
> Minimum number of temporary variables = **2** ($t_1, t_2$).

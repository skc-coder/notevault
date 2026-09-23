[!definition] Multi-dimensional arrays map continuous linear memory indices to multidimensional coordinates using either Row-Major Order (RMO) (row by row) or Column-Major Order (CMO) (column by column).
[[trainalguar ]]

[!formula] 1. 1D Array Address Formula: For array $A[L \dots U]$ with element size $c$:

$$\text{Address}(A[i]) = BA + (i - L) \times c$$

2. 2D Array Address Formula ($A[L_r \dots U_r, L_c \dots U_c]$): Number of rows: $M = U_r - L_r + 1$; Number of columns: $N = U_c - L_c + 1$.
Row-Major Order (RMO):
$$\text{Address}(A[i][j]) = BA + \Big((i - L_r) \times N + (j - L_c)\Big) \times c$$


Column-Major Order (CMO):
$$\text{Address}(A[i][j]) = BA + \Big((j - L_c) \times M + (i - L_r)\Big) \times c$$


3. 3D Array Address Formula ($A[L_1 \dots U_1, L_2 \dots U_2, L_3 \dots U_3]$ in RMO): Dimensions: $D_2 = U_2 - L_2 + 1$, $D_3 = U_3 - L_3 + 1$.

$$\text{Address}(A[i][j][k]) = BA + \Big((i - L_1) \times D_2 \times D_3 + (j - L_2) \times D_3 + (k - L_3)\Big) \times c$$

4. Triangular Matrix Non-Zero Elements ($N \times N$): Total elements stored in Upper Triangular (UTM) or Lower Triangular (LTM) matrix:

$$\text{Total Non-Zero Elements} = \frac{N(N + 1)}{2}$$

[!trap] Upper vs. Lower Bound Off-by-One Trap: When calculating dimension lengths, always remember $+ 1$:

$$\text{Length} = \text{UpperBound} - \text{LowerBound} + 1$$

For negative bounds (e.g., $-55 \dots +55$), $N = 55 - (-55) + 1 = 111$.
[!question] GATE / PSU Practice Drill: Given a 3D array $A[3 \dots 9, 5 \dots 7, 1 \dots 26]$ with base address $1000$ and element size $10\text{ bytes}$. Calculate the memory address of $A[7][6][20]$ in Row-Major Order. (A) 4470
(B) 4570
(C) 4670
(D) 4770
Step-by-Step Resolution:
Determine dimension lengths:
$D_1 = 9 - 3 + 1 = 7$


$D_2 = 7 - 5 + 1 = 3$


$D_3 = 26 - 1 + 1 = 26$


Determine offset indices for target $A[7][6][20]$:
$i_{\text{off}} = 7 - 3 = 4$


$j_{\text{off}} = 6 - 5 = 1$


$k_{\text{off}} = 20 - 1 = 19$


Calculate linear element displacement:
$$\text{Offset} = (4 \times D_2 \times D_3) + (1 \times D_3) + 19 = (4 \times 3 \times 26) + (1 \times 26) + 19$$

$$\text{Offset} = (4 \times 78) + 26 + 19 = 312 + 26 + 19 = 357\text{ elements}$$


Multiply by element size $c = 10\text{ bytes}$:
$$\text{Address} = 1000 + (357 \times 10) = 1000 + 3570 = 4570$$


Correct Answer: (B) 4570

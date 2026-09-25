###### Translation Lookaside Buffer (TLB)
A TLB is an associative, high-speed on-chip hardware cache located inside the MMU used to accelerate virtual-to-physical address translation[cite: 5, 6].
* Stores recently resolved subsets of Page Table Entries:
  $$\text{TLB Entry} = [\text{Tag / Virtual Page Number } (p) \mid \text{Physical Frame Number } (f) \mid \text{Control Bits}]$$[cite: 5]
* Typical capacity: small, typically $64$ to $512$ entries (rarely exceeds $1024$ entries)[cite: 6].

[!theorem] The Locality of Reference Principle
TLBs work effectively due to the program property where $90\%$ of execution time is spent in $10\%$ of code[cite: 6]:
1. **Temporal Locality**: Items referenced recently are highly likely to be referenced again in the near future (e.g., loop variables `i`, accumulator `sum`)[cite: 5].
2. **Spatial Locality**: Instructions or data elements stored at contiguous or nearby addresses are likely to be accessed sequentially (e.g., sequential array iterations `a[j]`)[cite: 5].

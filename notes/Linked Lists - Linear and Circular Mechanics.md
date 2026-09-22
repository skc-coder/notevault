[!definition]
Singly Linked List (SLL): Forward-only chained collection where each node contains data and a single next pointer.
Doubly Linked List (DLL): Bidirectional chained collection where each node contains prev and next pointers.
Circular Singly Linked List (CSLL): Last node's next pointer loops back to head (contains no NULL pointers).
Circular Doubly Linked List (CDLL): Satisfies head->prev == tail and tail->next == head.



Code snippet
flowchart LR
    subgraph CDLL Architecture
        A["Node A (Head)"] <--> B["Node B"]
        B <--> C["Node C (Tail)"]
        C -.->|"next"| A
        A -.->|"prev"| C
    end


[!theorem]
Tail-Maintained CSLL Invariant:
If a CSLL maintains a single pointer to tail:
head is accessed directly in $O(1)$ time via tail->next.
Insert at Beginning: $O(1)$.
Insert at End: $O(1)$.
Delete First Node: $O(1)$.
Delete Last Node: Requires finding the node preceding tail, taking $O(n)$ time.
[!trap]
Unlinking in DLL without Boundary Checks:
The typical node deletion sequence:



C
p->prev->next = p->next;
p->next->prev = p->prev;
free(p);


Causes a segmentation fault if $p$ is the first node (p->prev == NULL) or the last node (p->next == NULL). In CDLL, however, this exact code executes safely for any node because pointers wrap around cyclically without reaching NULL.
[!question] IOCL / PSU Practice Drill: A 64-bit system uses 8-byte pointers and stores 4-byte data payloads with 4-byte compiler structure padding (total payload = 8 bytes per node). What is the ratio of memory efficiency (Data Payload / Total Node Size) for a Doubly Linked List compared to a Singly Linked List? (A) $1:2$
(B) $2:3$

(C) $3:4$

(D) $1:1$

Step-by-Step Resolution:
Singly Linked List (SLL) Node Size:
$$\text{Payload} = 8\text{ bytes}, \quad \text{Pointer (next)} = 8\text{ bytes}$$

$$\text{Total SLL Node Size} = 8 + 8 = 16\text{ bytes}$$

$$\text{Efficiency}_{\text{SLL}} = \frac{8}{16} = 0.5 \quad (50\%)$$


Doubly Linked List (DLL) Node Size:
$$\text{Payload} = 8\text{ bytes}, \quad \text{Pointers (prev + next)} = 8 + 8 = 16\text{ bytes}$$

$$\text{Total DLL Node Size} = 8 + 16 = 24\text{ bytes}$$

$$\text{Efficiency}_{\text{DLL}} = \frac{8}{24} = 0.3333 \quad (33.33\%)$$


Ratio of Memory Efficiency ($\text{DLL} : \text{SLL}$):
$$\text{Ratio} = \frac{8/24}{8/16} = \frac{1/3}{1/2} = \frac{2}{3} \quad (2:3)$$


Correct Answer: (B) 2:3

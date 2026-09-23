> [!definition]
> **Linking and Dispatch** describe how symbols (functions, routines, and external modules) are mapped to executable code blocks:
> * **Static Linking:** External routines and archive libraries (`.a`, `.lib`) are copied directly into the final binary executable at build time.
> * **Dynamic Linking:** The binary contains only import stub tables. The operating system loader or dynamic linker (`ld.so`) maps shared libraries (`.so`, `.dll`) into the process address space during program startup or at runtime via API calls (`dlopen`).

```mermaid
flowchart TD
    subgraph Static Linking
        SRC1["main.o"] --> LINK1["Static Linker"]
        LIB1["libc.a"] --> LINK1
        LINK1 --> BIN1["Self-Contained Executable (Large)"]
    end
    subgraph Dynamic Linking
        SRC2["main.o"] --> LINK2["Linker"]
        LINK2 --> BIN2["Lean Executable with Import Table"]
        BIN2 -.->|"Loaded at runtime by ld.so"| SHARED["libc.so (Shared in RAM)"]
    end
```

### Dispatch Paradigms

```mermaid
flowchart LR
    subgraph Static Dispatch
        CALL1["Direct Function Call"] -->|"Direct jump to static address"| ADDR1["0x00401020: void func()"]
    end
    subgraph Dynamic Dispatch
        CALL2["Virtual Method Call"] -->|"1. Dereference vptr"| VTAB["vtable"]
        VTAB -->|"2. Offset index lookup"| ADDR2["Indirect Function Pointer Call"]
    end
```

### Comprehensive Comparison: Static vs Dynamic Linking

| Parameter | Static Linking / Static Dispatch | Dynamic Linking / Dynamic Dispatch |
| :--- | :--- | :--- |
| **Resolution Target** | Absolute memory address or relative fixed PC offset | Indirection table: Global Offset Table (GOT) / `vtable` |
| **Memory Utilization** | High disk footprint; code duplicated across processes | Low physical memory; shared pages across multiple processes |
| **Execution Performance**| Optimal speed; allows compiler cross-function inlining | Indirection overhead; potential dynamic linker resolution latency |
| **Hot Patching / Updates**| Requires full recompilation and relinking of application | Allows drop-in updates of shared objects without recompiling host binary |

> [!question]
> **Practice Problem:** Why does dynamic dispatch prevent typical compiler function inlining optimizations?
>
> **Analysis:**
> Inlining requires the compiler to replace a function invocation instruction with the exact body of the callee at compile time. Because dynamic dispatch depends on the runtime value of the object's `vptr` (which can change based on conditional branch logic, polymorphism, or user input), the static compiler cannot definitively identify the target method implementation, forcing an indirect call instruction.

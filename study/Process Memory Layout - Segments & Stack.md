---
title: Process Memory Layout - Segments & Stack
tags:
  - clang
  - c-language
  - memory-layout
  - process
  - study
---


A compiled program binary is organized into runtime memory segments relative to hardware base pointers:

---

## Memory Segments Architecture

| Memory Segment | Growth Direction | Stored Data & Characteristics |
| :--- | :---: | :--- |
| **Code / Text Segment** | Fixed | Compiled read-only machine instructions. |
| **Data Segment (.data / .bss)** | Fixed | Global and `static` variables initialized at startup. |
| **Heap Segment** | Grows Upward ($\uparrow$) | Dynamic memory allocated at runtime via `malloc` / `calloc`. |
| **Stack Segment** | Grows Downward ($\downarrow$) | Activation records (stack frames), local `auto` variables, and return addresses. |

---

## Related Notes
- [[Storage Classes Matrix & Register Class]]
- [[Storage Classes - Static & Extern]]
- [[Recursion Tracing & Tree Method]]

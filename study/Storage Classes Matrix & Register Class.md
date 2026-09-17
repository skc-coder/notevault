---
tags:
  - clang
  - c-language
  - storage-classes
  - study
---


C specifies four core storage classes: `auto`, `register`, `static`, and `extern`.

---

## Storage Classes Matrix

| Storage Class | Keyword | Storage Location | Scope | Lifetime | Default Value | Linkage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Automatic** | `auto` | Runtime Stack | Block scope | Block entry to exit | Garbage (Indeterminate) | None |
| **Register** | `register` | CPU Register / Stack | Block scope | Block entry to exit | Garbage (Indeterminate) | None |
| **Static Local**| `static` | Data Segment | Block scope | Entire execution | `0` | None |
| **Static Global**| `static` | Data Segment | File scope | Entire execution | `0` | Internal |
| **External** | `extern` | Data Segment | File / Block | Entire execution | `0` | External |

---

## The `register` Class Restriction

> [!trap] Unary Address-Of Restriction
> Using the unary address-of operator `&` on a `register` variable triggers a **compile-time error**, regardless of whether the compiler honored the register placement.

---

## Related Notes
- [[Storage Classes - Static & Extern]]
- [[Process Memory Layout - Segments & Stack]]

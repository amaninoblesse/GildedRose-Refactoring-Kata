# Gilded Rose Refactoring Kata — Python

## Purpose of the Exercise
This kata is a classic refactoring challenge designed to assess:
- My ability to understand and improve legacy code,
- My mastery of clean code and SOLID principles,
- My capacity to introduce maintainable abstractions,
- My discipline in preserving existing business rules.

The refactoring performed in this repository keeps the original behavior fully intact, as validated by ApprovalTests.

---

The original implementation placed all business logic inside one large `update_quality()` method with deeply nested conditionals.  
This made the code hard to read, difficult to extend, and fragile.

To improve structure and maintainability, I applied the following principles:

### **1. Single Responsibility & Separation of Concerns**
Each item type now has its own class responsible for its specific update behavior.

### **2. Open/Closed Principle (OCP)**
New item types can be added without modifying existing logic in `GildedRose`.

### **3. Polymorphism instead of conditionals**
The `GildedRose` class no longer contains business logic.  
It delegates updates to specialized item classes.

### **4. Factory pattern**
A simple factory selects the appropriate class based on the item’s name.

### **5. Test-driven refactoring**
The ApprovalTests provided in the kata served as a functional oracle.  
All behavior after refactoring is verified to be identical to the original implementation.

---

## Final Architecture
```
python/
├─ gilded_rose.py          # Orchestrator; delegates logic to specialized classes
├─ item_classes.py         # Contains BaseItem + AgedBrie, BackstagePass, Sulfuras, NormalItem
├─ item_factory.py         # Maps Items to their corresponding logic classes
└─ tests/
   ├─ test_gilded_rose.py
   ├─ test_gilded_rose_approvals.py
   └─ approved_files/
```

---

## What Was Improved ?

### **Before**
- One long method handling every case  
- Complex nested `if/elif` blocks  
- Difficult to extend (e.g., adding “Conjured” items)

### **After**
- Clean, modular, and readable architecture  
- Clear separation of item behaviors  
- Extensible design: adding a new item type requires only a new class  
- `GildedRose` is now minimal and easy to reason about:

```python
class GildedRose:
    def __init__(self, items):
        self.items = [create_item(i) for i in items]

    def update_quality(self):
        for item in self.items:
            item.update()
```


## Ensuring Correct Behavior
No rules were changed during the refactoring.
All logic was extracted as-is into dedicated classes.

Behavior was validated using:
- ApprovalTests → ensure full functional equivalence
- Unit tests → validate specific scenarios

```
python -m pytest
```

## To run the simulation (from the kata)
```
python texttest_fixture.py 5
```

## Time spent
Approximately 3 hours:
- reading & analyzing the legacy code,
- designing the refactoring strategy,
- implementing polymorphic item classes,
- validating behavior with ApprovalTests,
- documenting the solution.

## Notes & Possible Extensions
If given more time, further improvements could include:
- Adding first-class support for “Conjured” items
- Introducing type annotations for stricter validation
- Increasing test coverage beyond the approval mechanism
- Converting item names into an enum for better structure

## Conclusion
This refactoring demonstrates a clean, extensible architecture aligned with SOLID principles while fully preserving the original business behavior.
The codebase is now significantly easier to maintain, test, and evolve.
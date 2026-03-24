---
mode: agent
description: "Refactor a specific item type in the Gilded Rose kata using the Strategy Pattern"
---

# Refactor Step: {{ itemType }}

You are refactoring the Gilded Rose inventory system one item type at a time.
The target item type for this step is **{{ itemType }}**.

## Context

- Source file: `python/gilded_rose.py`
- Test file: `python/tests/test_gilded_rose.py`
- The project uses a **Strategy Pattern** where each item type has its own `*Updater` class inheriting from `ItemUpdater`.
- The `Item` class must NEVER be modified (it belongs to the goblin).

## Your Task

Perform a focused refactoring of the **{{ itemType }}** updater class. Follow these steps in order:

### Step 1 — Review Current Implementation

Read the current updater class for {{ itemType }} in `python/gilded_rose.py`.
Identify any code smells:
- Duplicated logic with the base class
- Missing edge-case handling
- Unclear variable names or magic numbers
- Inconsistent patterns compared to other updaters

### Step 2 — Review Existing Tests

Read `python/tests/test_gilded_rose.py` and find the test class for {{ itemType }}.
Identify any gaps in test coverage:
- Are boundary conditions tested? (quality = 0, quality = 50, sell_in = 0)
- Are both before and after sell date scenarios covered?
- Is the quality cap (min 0, max 50) enforced?

### Step 3 — Add Missing Tests (TDD)

If you found gaps, add new test methods to the appropriate test class.
Follow the existing naming convention: `test_<what_it_tests>`.
Run `pytest python/tests/test_gilded_rose.py -v` to confirm all tests pass.

### Step 4 — Refactor the Updater

Apply any improvements to the updater class:
- Extract magic numbers into descriptive local variables if helpful
- Simplify conditional logic
- Ensure consistent use of `_decrease_quality` / `_increase_quality` helpers
- Keep the public interface unchanged

### Step 5 — Verify

Run `pytest python/tests/test_gilded_rose.py -v` to confirm all tests still pass.
Report the results.

## Rules

- Do NOT modify the `Item` class
- Do NOT change the `GildedRose.update_quality()` public API
- Keep changes focused on {{ itemType }} only
- Follow the existing coding style and patterns

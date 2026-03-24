# Copilot Instructions — Gilded Rose Kata (Python)

## Project Overview

This is the **Gilded Rose Kata**, a refactoring exercise for an inventory management system.
The codebase lives in the `python/` directory and uses a **Strategy Pattern** to handle
different item types. Each item type has its own updater class that encapsulates its
quality-update logic.

## Architecture

- **`Item` class** — Do NOT modify. Owned by the "goblin in the corner."
- **`ItemUpdater`** (base) — Default strategy for normal items.
- **`AgedBrieUpdater`**, **`SulfurasUpdater`**, **`BackstagePassUpdater`**, **`ConjuredUpdater`** — Specialized strategies inheriting from `ItemUpdater`.
- **`_get_updater(item)`** — Factory function mapping item names to strategies.
- **`GildedRose`** — Public API; delegates to the factory + strategy.

## Business Rules

| Item | sell_in | Quality behaviour |
|---|---|---|
| Normal | decreases | -1 per day; -2 after sell date; min 0 |
| Aged Brie | decreases | +1 per day; +2 after sell date; max 50 |
| Sulfuras | never changes | always 80; never sold |
| Backstage passes | decreases | +1 (>10 days), +2 (6-10 days), +3 (1-5 days), 0 after concert |
| Conjured | decreases | -2 per day; -4 after sell date; min 0 |

## Coding Conventions

- **Language**: Python 3
- **Testing**: `unittest` framework; run with `pytest python/tests/`
- **Test organisation**: One test class per item type (e.g., `NormalItemTest`, `AgedBrieTest`)
- **Test naming**: `test_<what_it_tests>` (e.g., `test_quality_decreases_by_1_before_sell_date`)
- **Docstrings**: Each updater class and test class has a one-line docstring
- **Quality bounds**: Use `max(0, ...)` and `min(50, ...)` helpers from `ItemUpdater`
- **No modification** of the `Item` class (constraint of the kata)

## When Generating Code

1. Follow the Strategy Pattern — add new item types by creating a new `*Updater` subclass and registering it in `_get_updater`.
2. Write tests first (TDD) — create a test class with boundary cases before implementing.
3. Keep quality bounds enforced via `_decrease_quality` / `_increase_quality` helpers.
4. Always run `pytest python/tests/` after making changes to verify nothing breaks.
5. Keep the public `GildedRose.update_quality()` interface unchanged.

## File Structure

```
python/
├── gilded_rose.py            # Main source (Item, strategies, GildedRose)
├── texttest_fixture.py       # Text-based test fixture for approval tests
├── requirements.txt          # pytest, approvaltests, coverage
└── tests/
    ├── test_gilded_rose.py           # Unit tests (23 tests, 6 classes)
    └── test_gilded_rose_approvals.py # Approval / golden-master tests
```

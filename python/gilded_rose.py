# -*- coding: utf-8 -*-


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# ---------------------------------------------------------------------------
# Strategy Pattern: each item type has its own update strategy
# ---------------------------------------------------------------------------

class ItemUpdater:
    """Default strategy for normal items."""

    def update(self, item):
        self._decrease_quality(item, 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._decrease_quality(item, 1)

    def _decrease_quality(self, item, amount):
        item.quality = max(0, item.quality - amount)

    def _increase_quality(self, item, amount):
        item.quality = min(50, item.quality + amount)


class AgedBrieUpdater(ItemUpdater):
    """Aged Brie increases in quality over time."""

    def update(self, item):
        self._increase_quality(item, 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._increase_quality(item, 1)


class SulfurasUpdater(ItemUpdater):
    """Sulfuras never changes in quality or sell_in."""

    def update(self, item):
        pass


class BackstagePassUpdater(ItemUpdater):
    """Backstage passes have tiered quality increases, then drop to 0."""

    def update(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            self._increase_quality(item, 3)
        elif item.sell_in <= 10:
            self._increase_quality(item, 2)
        else:
            self._increase_quality(item, 1)
        item.sell_in -= 1


class ConjuredUpdater(ItemUpdater):
    """Conjured items degrade in quality twice as fast as normal items."""

    def update(self, item):
        self._decrease_quality(item, 2)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._decrease_quality(item, 2)


# ---------------------------------------------------------------------------
# Factory: maps item names to their update strategy
# ---------------------------------------------------------------------------

def _get_updater(item):
    """Factory function that returns the correct strategy for an item."""
    if item.name == "Aged Brie":
        return AgedBrieUpdater()
    if item.name == "Sulfuras, Hand of Ragnaros":
        return SulfurasUpdater()
    if item.name == "Backstage passes to a TAFKAL80ETC concert":
        return BackstagePassUpdater()
    if item.name.startswith("Conjured"):
        return ConjuredUpdater()
    return ItemUpdater()


# ---------------------------------------------------------------------------
# Main class (public API unchanged)
# ---------------------------------------------------------------------------

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = _get_updater(item)
            updater.update(item)

# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class NormalItemTest(unittest.TestCase):
    """Tests for normal items that have no special rules."""

    def test_quality_decreases_by_1_before_sell_date(self):
        items = [Item("Normal Item", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_quality_decreases_by_2_after_sell_date(self):
        items = [Item("Normal Item", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

    def test_quality_never_negative(self):
        items = [Item("Normal Item", 5, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_never_negative_after_sell_date(self):
        items = [Item("Normal Item", -1, 1)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)


class AgedBrieTest(unittest.TestCase):
    """Tests for Aged Brie which increases in quality over time."""

    def test_quality_increases_before_sell_date(self):
        items = [Item("Aged Brie", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_quality_increases_by_2_after_sell_date(self):
        items = [Item("Aged Brie", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(22, items[0].quality)

    def test_quality_never_exceeds_50(self):
        items = [Item("Aged Brie", 10, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_never_exceeds_50_after_sell_date(self):
        items = [Item("Aged Brie", 0, 49)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)


class SulfurasTest(unittest.TestCase):
    """Tests for Sulfuras which never changes."""

    def test_quality_stays_at_80(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(80, items[0].quality)

    def test_sell_in_never_decreases(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(10, items[0].sell_in)

    def test_quality_stays_at_80_after_sell_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)


class BackstagePassTest(unittest.TestCase):
    """Tests for Backstage passes with tiered quality increases."""

    def test_quality_increases_by_1_when_more_than_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_quality_increases_by_2_when_10_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(22, items[0].quality)

    def test_quality_increases_by_2_when_6_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(22, items[0].quality)

    def test_quality_increases_by_3_when_5_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(23, items[0].quality)

    def test_quality_increases_by_3_when_1_day(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(23, items[0].quality)

    def test_quality_drops_to_0_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_never_exceeds_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)


class ConjuredItemTest(unittest.TestCase):
    """Tests for Conjured items which degrade twice as fast."""

    def test_quality_decreases_by_2_before_sell_date(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

    def test_quality_decreases_by_4_after_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(16, items[0].quality)

    def test_quality_never_negative(self):
        items = [Item("Conjured Mana Cake", 5, 1)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_never_negative_after_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 3)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)


class MultipleItemsTest(unittest.TestCase):
    """Tests for updating multiple items at once."""

    def test_multiple_items_updated_correctly(self):
        items = [
            Item("Normal Item", 5, 10),
            Item("Aged Brie", 3, 20),
            Item("Sulfuras, Hand of Ragnaros", 0, 80),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 30),
            Item("Conjured Mana Cake", 5, 10),
        ]
        GildedRose(items).update_quality()

        self.assertEqual(9, items[0].quality)   # Normal: -1
        self.assertEqual(21, items[1].quality)  # Aged Brie: +1
        self.assertEqual(80, items[2].quality)  # Sulfuras: unchanged
        self.assertEqual(32, items[3].quality)  # Backstage: +2 (10 days)
        self.assertEqual(8, items[4].quality)   # Conjured: -2


if __name__ == '__main__':
    unittest.main()

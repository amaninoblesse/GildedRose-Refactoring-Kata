# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # --------------------------
            # Aged Brie
            # --------------------------
            if item.name == "Aged Brie":
                item.increase_quality()
                item.decrease_sell_in()
                if item.sell_in < 0:    
                    item.increase_quality()
    
            # --------------------------
            # Backstage Passes
            # --------------------------           
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.increase_quality()
                if item.sell_in < 11:
                    item.increase_quality()
                if item.sell_in < 6:
                    item.increase_quality()
                item.decrease_sell_in()
                if item.sell_in < 0:
                    item.quality = 0

            # --------------------------
            # Sulfuras
            # --------------------------            
            elif item.name == "Sulfuras, Hand of Ragnaros":
                # Nothing to do for Sulfuras
                pass

            # --------------------------
            # Normal items
            # --------------------------
            else:
                item.decrease_quality()
                item.decrease_sell_in()
                if item.sell_in < 0:
                    item.decrease_quality()

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.decrease_quality()
            else:
                if item.quality < 50:
                    item.increase_quality()
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.increase_quality()
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.increase_quality()
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.decrease_quality()
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.increase_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def decrease_quality(self):
        if self.quality > 0:
            self.quality -= 1

    def increase_quality(self):
        if self.quality < 50:
            self.quality += 1

    def decrease_sell_in(self):
        self.sell_in -= 1

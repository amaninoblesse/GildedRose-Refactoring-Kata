# -*- coding: utf-8 -*-
from item_factory import create_item

class GildedRose(object):

    def __init__(self, items):
        # Convert each item to its corresponding class
        self.items = [create_item(i) for i in items]

    def update_quality(self):
        for item in self.items:
            item.update()

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

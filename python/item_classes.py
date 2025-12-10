from abc import ABC, abstractmethod

class BaseItem(ABC):
    
    def __init__(self, item):
        self.item = item

    @abstractmethod
    def update(self):
        pass

    # Utility methods
    def increase_quality(self, amount=1):
        self.item.quality = min(50, self.item.quality + amount)

    def decrease_quality(self, amount=1):
        self.item.quality = max(0, self.item.quality - amount)

    def decrease_sell_in(self):
        self.item.sell_in -= 1

class AgedBrieItem(BaseItem):
    def update(self):
        self.increase_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.increase_quality()


class BackstagePassItem(BaseItem):
    def update(self):
        self.increase_quality()
        if self.item.sell_in < 11:
            self.increase_quality()
        if self.item.sell_in < 6:
            self.increase_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.item.quality = 0

class SulfurasItem(BaseItem):
    def update(self):
        pass  # Item does not change

class NormalItem(BaseItem):
    def update(self):
        self.decrease_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.decrease_quality()
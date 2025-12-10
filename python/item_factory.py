from item_classes import (
    AgedBrieItem,
    BackstagePassItem,
    SulfurasItem,
    NormalItem,
)

def create_item(item):
    if item.name == "Aged Brie":
        return AgedBrieItem(item)
    
    elif item.name == "Backstage passes to a TAFKAL80ETC concert":
        return BackstagePassItem(item)
    
    elif item.name == "Sulfuras, Hand of Ragnaros":
        return SulfurasItem(item)
    
    else:
        return NormalItem(item)
class Ollivander:

    def __init__(self):
        self.items = []

    def updateQuality(self):
        for item in self.items:
            item.updateQuality()

    def addItem(self, item):
        self.items.append(item)

    def toString(self):
        representation = ""
        for item in self.items:
            representation += item.toString()
        return representation
    
    def inventory(self):
        return self.items
    
    def nextDay(self):
        for item in self.items:
            item.updateQuality()
            print(item.toString())   

class Item:
     def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality

     @property
     def quality(self):
        return self._quality

     @quality.setter
     def quality(self, quality):
        self._quality = max(0, min(50, quality))

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


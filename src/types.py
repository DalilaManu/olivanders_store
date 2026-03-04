class Ollivander:

    def __init__(self):
        self.items = []

    def updateQuality(self):
        for item in self.items:
            item.updateQuality()

    def addItem(self, item):
        self.items.append(item)
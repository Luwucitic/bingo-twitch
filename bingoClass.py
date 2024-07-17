import random

class Bingo():


    def __init__(self, size = 5):
        self.size = size
        self.all_items = set()
    
    def addItem(self, item):
        self.all_items.add(item)
    
    #items is an array of item
    def addItems(self, items):
        [self.all_items.add(item) for item in items]
    
    def removeItem(self, item):
        self.all_items.remove(item)
    
    def clearItems(self, item):
        self.all_items.clear()
    
    def generateBoard(self, n = 1):
        items = list(self.all_items)
        random.shuffle(items)
        board = []
        temp = []
        i = 0
        for item in items[:self.size*self.size - 1]:
            temp.append(item)
            if (i == self.size - 1):
                board.append(temp)
                temp = []
                i=0
            i += 1
        return board
    





        


    



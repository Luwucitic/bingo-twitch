from pyscript import document

import pandas as pd
import random
import os

column = ""
GKEY = "1G-zaXRrLhcOsaVAt31C2IQNQUYxbm12E0ZVXtasZj2c"
SHEET = 'Bingo Spreadsheet'

url=f'https://docs.google.com/spreadsheet/ccc?key={GKEY}&output=xlsx'
data = pd.read_excel(url,sheet_name=SHEET)
print(data)
URL = url 

data = pd.read_csv(URL)
#data = pd.read_csv("test-sheet.csv")

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
        for item in items[:self.size*self.size]:
            i += 1
            temp.append(item)
            if (i == self.size):
                board.append(temp)
                temp = []
                i=0
            
        return board
    
    #converts CSV file  with column of items into a set
    def convertCSV(self, column):
        return set(data.loc[column])

def fillDrop():
    document.querySelector("dropdown-content")
    for name in data.keys():
        btn = document.createElement("button")
        btn.setAttribute("pyclick", "switchCol")
        btn.setAttribute("id", name)   

bingo = Bingo()
fillDrop()
items = bingo.convertCSV(column)



def switchCol(event):
    global column
    col = event.target.id
    column = col
    global items 
    items = bingo.convertCSV(column)

def clearCard():
    grid = document.querySelector(".flex-grid")
    grid.innerHTML = ""

def genCard(event):
    clearCard()
    bingo.addItems(items)
    board = bingo.generateBoard()
    #need to display the board for the user
    grid = document.querySelector(".flex-grid")
    for side in board:
        row = document.createElement("div")
        row.setAttribute("class","flex-row")
        for box in side:
            cell = document.createElement("div")
            cell.setAttribute("class", "flex-cell")
            cell.innerText = box
            row.append(cell)
        grid.append(row)

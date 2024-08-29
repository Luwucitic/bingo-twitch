from pyscript import document

from pyodide.http import open_url
import pandas as pd
import random


column = ""
GKEY = '1G-zaXRrLhcOsaVAt31C2IQNQUYxbm12E0ZVXtasZj2c'
SHEET = 'Bingo Spreadsheet'

url=f'https://docs.google.com/spreadsheet/ccc?key={GKEY}&output=csv'
print(url)
data = pd.read_csv(open_url(url))

URL = url 

#data = pd.read_csv(URL)
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
    def convertCSV(self, data, column):
        return set(data[column].dropna())

def fillDrop():
    global column
    drp = document.querySelector(".drp-con")
    for name in data.columns:
        print(name)
        btn = document.createElement("button")
        btn.setAttribute("class", "drp-item")
        btn.setAttribute("py-click", "switchCol")
        btn.setAttribute("id", name) 
        btn.innerHTML = name
        drp.append(btn)  
        column = name

bingo = Bingo()
fillDrop()
bingo.all_items = bingo.convertCSV(data, column)


def switchCol(event):
    global bingo
    global column
    print(event.target.id)
    col = event.target.id
    column = col
    bingo.all_items = bingo.convertCSV(data, column)

def clearCard():
    grid = document.querySelector(".flex-grid")
    grid.innerHTML = ""

def genCard(event):
    bingo.addItems(bingo.all_items)
    board = bingo.generateBoard()
    #need to display the board for the user
    grid = document.querySelector(".flex-grid")
    clearCard()
    for side in board:
        row = document.createElement("div")
        row.setAttribute("class","flex-row")
        for box in side:
            cell = document.createElement("div")
            cell.setAttribute("class", "flex-cell")
            cell.innerText = box
            row.append(cell)
        grid.append(row)

import bingoClass

items = list(range(36))

bingo = bingoClass.Bingo()
bingo.addItems(items)
print(bingo.generateBoard())

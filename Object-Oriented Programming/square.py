class Square:
    def __init__(self,side):
        self.side = side

    def changeSide(self,newSide):
        self.side = newSide

    def showSide(self):
        print("O valor do quadrado é: ",self.side)

    def calcArea(self):
        area = self.side * self.side
        print("A área do quadrado é de: ",area)

square = Square(6)
square.showSide()
square.changeSide(4)
square.showSide()
square.calcArea()
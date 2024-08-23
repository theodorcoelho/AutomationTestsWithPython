class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def changeSides(self,newWidth,newHeight):
        self.width = newWidth
        self.height = newHeight
        print("Nova largura: ",self.width)
        print("Nova altura: ",self.height)

    def showSides(self):
        print("A largura é: ",self.width)
        print("A altura é: ",self.height)


    def calArea(self):
        return self.width * self.height        

    def calcPerimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        print("O valor do perímetro é : ",perimeter)

rectangle = Rectangle(2,3)
rectangle.showSides()
rectangle.calcPerimeter()
rectangle.changeSides(3,4)
rectangle.calcPerimeter()
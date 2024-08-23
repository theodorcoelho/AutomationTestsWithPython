class Ball:
    def __init__(self,color,circumference,material):
        self.color = color
        self.circumference = circumference
        self.material = material

    def changeColor(self,newColor):
        self.color = newColor

    def showColor(self):
        print("Color: ",self.color)
        print("Circumference: ",self.circumference)
        print("Material: ",self.material)

ball = Ball("Red",15,"Metal")        
ball.showColor()
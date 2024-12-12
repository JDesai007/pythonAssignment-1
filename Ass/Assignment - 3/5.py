class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0 

class Square(Shape):
    def __init__(self, length):
        super().__init__()  
        self.length = length
    
    def area(self):
        return self.length * self.length  


square = Square(5)

shape = Shape()
print("Area of Shape:", shape.area()) 

print("Area of Square:", square.area()) 


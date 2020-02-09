class Rectangle:   
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return self.length*self.breadth
    
print(Rectangle(3,4).area())
print(Rectangle(4,5).area())
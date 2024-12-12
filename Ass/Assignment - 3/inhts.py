class obj:
    def __init__(self,x):
        self.x=x
    

class a(obj):
    def method(self):
        print("A class method")
        super().method()
        
class b(obj):
    def method(self):
        print("B class method")
        super().method()
        
       
class c(obj):
    def method(self):
        print("c class method")
        super().method()
        
           
class x(a,b):
    def method(self):
        print("X class method")
        super().method()
        
       
class y(b,c):
    def method(self):
        print("Y class method")
        super().method()
        
       
class p(x,y,c):
    def method(self):
        print("P class method")
        super().method()
        
k=p("my")
k.method()
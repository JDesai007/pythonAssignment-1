class student:
    def __init__(self,name):
        self.name=name
        
    def hello(self):
        print("Hello",self.name)
        
s1=student("Jaydip")
s1.hello() # calling the mathod


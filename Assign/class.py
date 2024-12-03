# class demo: #define the class 
#     name="Jaydip"
    
# d=demo()  #calling the object/Instance of class
# print(d.name) # call the class variable



## how to create constructor in python 

# class car:
#     def __init__(self):
#         print("Constructor")

# c=car()



# ## constructor with user parameter 

# class car:
     
#     def __init__(self,color,brand,model):
#         print("Constructor call")
#         self.color=color
#         self.brand=brand
#         self.model=model
    
# c=car("white","Audi","a7")
# c1=car("blue","kia","sonet")
# print(c.color)
# print(c.brand)
# print(c.model)

# print(c1.color,c1.brand,c1.model)


## avoid same name and enter only unique name in  given class college name is same for all student but student name and roll_no is diffrent

# class std:
#     college="GVP"
#     name="ABC" #class attribute
    
#     def __init__(self,roll_no,name):
#         self.roll=roll_no
#         self.name=name #Object attribute

# s=std(10,"XYZ")
# print(s.roll)
# print(s.name)  ## In this example object attribute is call
# print(s.college)


## User define method or function in class

class student:
    def __init__(self,name):
        self.name=name
        
    def hello(self):
        print("Hello",self.name)
        
s1=student("Jaydip")
s1.hello() # calling the mathod







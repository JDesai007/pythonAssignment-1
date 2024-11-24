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

# class student:
#     def __init__(self,name):
#         self.name=name
        
#     def hello(self):
#         print("Hello",self.name)
        
# s1=student("Jaydip")
# s1.hello() # calling the mathod



## Example **** Write a programm to create  student class that takes name and marks of 3 subjects as argument inn constructor. then create a method to print the averrage.

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    
#     def avg(self):
#         sum=0
#         for no in self.marks:
#             sum+=no
#         print("Hii",self.name,"Your marks average is",sum/3)
                  
# s=student("Ashish",[98,99,97])
# s.avg()
            



# ## Static method // It is do not use without self parameter
# class static:
#     @staticmethod  ## decorator
#     def hello():
#         print("This is static method in python")
        
# s=static()
# s.hello()



## create Account class with 2 attributte - balance & account no. create methods for debit, credit & printing the balance.

class account:
    
    def __init__(self,bal,acc_no):
        self.bal=bal
        self.acc=acc_no
        
    def debit(self,amount):
        self.bal -= amount
        print("Rs.",amount,"Was debited..")
        print("Total Balance:",self.print_bal())
        
    def credit(self,amount):
        self.bal += amount
        print("Rs.",amount,"Was credited..")
        print("Total Balance:",self.print_bal())
        
    def print_bal(self):
        return self.bal
        
        
a1=account(10000,34564576)
print("Account no:",a1.acc)
print("Balance:",a1.bal)
a1.debit(2000)
a1.credit(1000)






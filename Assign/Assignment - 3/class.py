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

# class account:
    
#     def __init__(self,bal,acc_no):
#         self.bal=bal
#         self.acc=acc_no
        
#     def debit(self,amount):
#         self.bal -= amount
#         print("Rs.",amount,"Was debited..")
#         print("Total Balance:",self.print_bal())
        
#     def credit(self,amount):
#         self.bal += amount
#         print("Rs.",amount,"Was credited..")
#         print("Total Balance:",self.print_bal())
        
#     def print_bal(self):
#         return self.bal
        
        
# a1=account(10000,34564576)
# print("Account no:",a1.acc)
# print("Balance:",a1.bal)
# a1.debit(2000)
# a1.credit(1000)


## delete object from memory
# del s1.name
# del s1


# ## Using __ sign you can create private variable in pyton
# class account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
        
#     def reset_pss(self):
#         print(self.__acc_pass)

# a=account(567854,"#acc123")
# print(a.reset_pss())
# print(a.acc_no)
# print(a.__acc_pss)









###Q-1 Ass-3

# from datetime import datetime

# class Person:
#     # Constructor to initialize name, country, and date_of_birth
#     def __init__(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         # Date of birth should be a datetime object
#         self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    
#     # Method to calculate age based on date of birth
#     def calculate_age(self):
#         # Get the current date
#         current_date = datetime.now()
#         # Calculate the difference in years
#         age = current_date.year - self.date_of_birth.year
#         # Adjust age if the birthday has not occurred yet this year
#         if current_date.month < self.date_of_birth.month or (current_date.month == self.date_of_birth.month and current_date.day < self.date_of_birth.day):
#             age -= 1
#         return age

#     # Method to display the person's details
#     def display_person_info(self):
#         print(f"Name: {self.name}")
#         print(f"Country: {self.country}")
#         print(f"Date of Birth: {self.date_of_birth.strftime('%Y-%m-%d')}")
#         print(f"Age: {self.calculate_age()} years")

# # Create an instance of the Person class
# person = Person(name="John Doe", country="USA", date_of_birth="1990-05-15")

# # Display the person's information and calculated age
# person.display_person_info()






###Q-2 Ass-3

# Parent class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     # Method to display details of the person
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")

# # Child class inheriting from Person
# class Employee(Person):
#     def __init__(self, name, age, employee_id, department):
#         # Call the constructor of the parent class (Person)
#         super().__init__(name, age)
#         self.employee_id = employee_id
#         self.department = department
    
#     # Method to display employee details
#     def display(self):
#         # Call the display method of the parent class
#         super().display()  
#         print(f"Employee ID: {self.employee_id}")
#         print(f"Department: {self.department}")
    
#     # Method to modify the behavior of the details method
#     def details(self):
#         print(f"Employee Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Department: {self.department}")
        
# # Creating an instance of the Employee class
# employee = Employee("John Doe", 30, "E12345", "HR")

# # Displaying details using the display method
# print("Employee Display:")
# employee.display()

# # Displaying details using the details method (modified from the parent class)
# print("\nEmployee Details:")
# employee.details()



###Q-3 Ass-3
# # Parent class Vehicle
# class Vehicle:
#     def speed(self):
#         raise NotImplementedError("Subclass must implement abstract method")

# # Subclass Car
# class Car(Vehicle):
#     def speed(self):
#         return "The car is speeding at 120 km/h."

# # Subclass Bike
# class Bike(Vehicle):
#     def speed(self):
#         return "The bike is speeding at 80 km/h."

# # Subclass Train
# class Train(Vehicle):
#     def speed(self):
#         return "The train is speeding at 150 km/h."

# # Function to demonstrate polymorphism
# def show_speed(vehicle):
#     print(vehicle.speed())

# # Creating instances of each subclass
# car = Car()
# bike = Bike()
# train = Train()

# # Demonstrating polymorphism
# print("Polymorphism Demonstration:")
# show_speed(car)   # The car's speed message
# show_speed(bike)  # The bike's speed message
# show_speed(train) # The train's speed message



###Q-4 Ass-3
# class BankAccount:
#     # Constructor to initialize account number and balance
#     def __init__(self, account_number, initial_balance=0):
#         self.__account_number = account_number  # Private attribute
#         self.__balance = initial_balance        # Private attribute
    
#     # Method to deposit money
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited ${amount}. Current balance: ${self.__balance}")
#         else:
#             print("Deposit amount must be positive.")
    
#     # Method to withdraw money
#     def withdraw(self, amount):
#         if amount > 0:
#             if self.__balance >= amount:
#                 self.__balance -= amount
#                 print(f"Withdrew ${amount}. Current balance: ${self.__balance}")
#             else:
#                 print("Insufficient balance.")
#         else:
#             print("Withdrawal amount must be positive.")
    
#     # Method to get the current balance
#     def get_balance(self):
#         return self.__balance


# # Create an instance of BankAccount
# account = BankAccount(account_number="123456789", initial_balance=500)

# # Perform deposit and withdrawal operations
# account.deposit(200)  # Deposit $200
# account.withdraw(100)  # Withdraw $100
# account.withdraw(700)  # Attempt to withdraw more than balance

# # Check the updated balance
# print(f"Final balance: ${account.get_balance()}")





###Q-5 Ass-3


# # Parent class Shape
# class Shape:
#     def __init__(self):
#         pass
    
#     # Method to calculate the area (default is 0)
#     def area(self):
#         return 0  # Default area for a generic shape

# # Subclass Square, inherits from Shape
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__()  # Call the constructor of the parent class
#         self.length = length
    
#     # Overriding the area method to calculate the area of the square
#     def area(self):
#         return self.length * self.length  # Area of square = length^2

# # Create an instance of the Square class
# square = Square(5)

# # Print the area of the Shape (which is 0 by default)
# shape = Shape()
# print("Area of Shape:", shape.area())  # Expected output: 0

# # Print the area of the Square
# print("Area of Square:", square.area())  # Expected output: 25










## Inharitance

## Single level inheritance

# class car:
#     @staticmethod
#     def start():
#         print("Start car")
        
#     @staticmethod
#     def stop():
#         print("Stop car")
        
# class toyotacar(car):
#     def __init__(self,name):
#         self.name=name
        
# car1=toyotacar("Fortunar")
# car2=toyotacar("prius")

# print(car1.name)
# print(car1.start())
# print(car1.stop())
# print(car2.name)


## Multi level inheritance

    
# class car:
#     @staticmethod
#     def start():
#         print("Start car")
        
#     @staticmethod
#     def stop():
#         print("Stop car")
        
# class toyotacar(car):
#     def __init__(self,brand):
#         self.brand=brand
  
  
# class fortunar(toyotacar):
#     def __init__(self,type):
#         self.type=type
    
    
# c=fortunar("disel") 
# print(c.type) 
# c.start()  
# car1=toyotacar("Fortunar")
# car2=toyotacar("prius")




### Multiple inherithance

# class a:
#     varA="Welcome to Class A"
    
# class b:
#     varB="Class B"
    
# class c(a,b):
#     varC="Class c"
    
# c1=c()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)



# ## super() in inheritance

# class car:
    
#     def __init__(self,type):
#         self.type=type
#     @staticmethod
#     def start():
#         print("Start car")
        
#     @staticmethod
#     def stop():
#         print("Stop car")
        
# class toyotacar(car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
#         super().start()
        
        
# car1=toyotacar("prius","electric")
# print(car1.type)


## Class decorator method in python
# class person:
#     name="anonymous"
    
#     # def changename(self,name):
#     #     self.__class__.name="Rahul"
        
#     @classmethod
#     def changename(cls,name):
#         cls.name=name
    
# p1=person()
# p1.changename("Rahul kumar")
# print(p1.name)
# print(person.name)




# class student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentage=str((self.phy+self.chem+self.math)/3)+" %"

# s1=student(98,97,96)
# print(s1.percentage)





# class student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentage=str((self.phy+self.chem+self.math)/3)+" %"

#     def calc_per(self):
#          self.percentage=str((self.phy+self.chem+self.math)/3)+" %"
  
        
# s1=student(98,97,96)
# print(s1.percentage)

# s1.phy=86
# print(s1.phy)
# s1.calc_per()
# print(s1.percentage)




## propery decorator in python

class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math)/3)+" %"

    # def calc_per(self):
    #      self.percentage=str((self.phy+self.chem+self.math)/3)+" %"
  
    @property
    def calc_per(self):
         return str((self.phy+self.chem+self.math)/3)+" %"

        
s1=student(98,97,96)
print(s1.percentage)

s1.phy=89
print(s1.phy)

print(s1.percentage)



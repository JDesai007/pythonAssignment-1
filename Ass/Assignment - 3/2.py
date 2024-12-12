
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
   
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id, department):
   
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department
    

    def display(self):

        super().display()  
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
    
  
    def details(self):
        print(f"Employee Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Department: {self.department}")
        

employee = Employee("John Doe", 30, "E12345", "HR")


print("Employee Display:")
employee.display()

print("\nEmployee Details:")
employee.details()
from datetime import datetime

class person:
    
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=datetime.strptime(dob, '%d-%m-%Y')
        
    def calc(self):
        today=datetime.today()
        age = today.year - self.dob.year
        return age
    

p = person("Ashish","India","02-01-2004")
print("Name:",p.name)
print("Country:",p.country)
print("DOB:",p.dob)
print("Age:",p.calc(),"Years")
class Dog:
    def walk(self):
        return "*walking*"
    
    def speak(self):
        return "woof!"
    
class Tomy(Dog):
    def talk(self):
        return super().speak()

mydog=Tomy()
m=mydog.talk()
print(m)
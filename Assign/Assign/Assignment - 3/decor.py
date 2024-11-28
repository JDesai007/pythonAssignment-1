
def venila():
    print("This is venila")
    
x=venila()

def choc():
    print("This is choclate")
    
x=choc()

def decor_choc(func):
    def inner_func(x):
        x="Choclate"
        return func(x)
    return inner_func
        
        
a=decor_choc()
b=a("choclate")
print(b)
    

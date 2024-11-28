def add(a,b):
    res =a+b
    return res

x=add(10,-30)
print(x)

def decor(func):
    def inner_func(a,b):
        if a < 0:
            a=a*-1
        if b < 0:
            b=b*-1
        return func(a,b)
    return inner_func

add1=decor(add)

ans=add1(20,-10)
print(ans)
    
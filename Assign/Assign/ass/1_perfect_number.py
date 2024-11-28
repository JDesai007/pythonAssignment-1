num=int(input("Enter the number: "))  
sum=0  
for i in range(1,num):  
    if (num%i==0):  
        sum+=i
        print(i)
    
if(sum==num):  
    print(f"{num} is perfect number")  
else:  
    print(f"{num} is not a perfect number")  
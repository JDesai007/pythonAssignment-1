## 1. create new file and enter following data.
# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in Java.")

    
## 2.Write a function that replaces all occurences of "Java" with "Python" in above file.

# def replace_word():
#     with open("practice.txt","r") as f:  
#         data=f.read()
        
#     new=data.replace("Java","Python")
#     print(data)
#     print(new)

#     with open("practice.txt","w") as f:
#         f.write(new)
# replace_word()


        
## 3.search if the word "learning" exist in the file or not.
# def check_word():
#     with open("practice.txt","r") as f:
#         data=f.read()
#         word="learning"
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not Found")
            
# check_word()


## 4.write a function to find in which line of tthe file does the word "learning" occur first. print-1 if word not found.
# def check_line():
#     word="learning"
#     data=True
#     line=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line)
#                 return
#             line+=1
#     return -1

# print(check_line())      


## 5.From a file counting number seperated by comma, print the count of even numbers.

# with open("count.txt","r") as f:
#     data=f.read()
#     print(data)
#     no=""
#     for i in range(len(data)):
#         if(data[i]==","):
#             print(no)
#             no=""
#         else:
#             no+=data[i]

count=0
with open("count.txt","r") as f:
    data=f.read()
    no=data.split(",")
    for val in no:
        if(int(val)%2==0):
            count+=1
            print(val)
            
print("Total no of Even is:",count)
    
    
  

    
        
    
    
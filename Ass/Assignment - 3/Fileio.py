
## How to install external module in python
    # pip install tensorflow
    # pip3 install tensorflow

## Mode of file in python
# r - open for reading(default)
# w - open for writing, override the data in file
# x - create a new file and open it for writing
# a - open for writing, appending to end of the ffile if it exists
# b - binary mode
# t - text mode(default)
# + - open a disk file for updating(reading or writing), r+, w+, a+ etc..



## open("File_name","Mode") used for opening the file
## open("sample.txt","r/w")

# f=open("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()


## print only few character from the file use the read(7) with no. of characters 
# f=open("demo.txt","r")
# d=f.read(7)
# print(d)
# f.close()

## Print only no. of line in the readline() 
# f=open("demo.txt","r")
# d=f.readline()
# f1=f.readline() 
# print(d)
# print(f1)
# f.close()


## Write new data in the file using "w" mode in existting file otherwise python is create that file 
# f=open("sample.txt","w")
# f.write("Hello, how are you this function is used for the write in file..")
# f.close()

## Wrrite new data at the end of file in existing file using "a" mode
# f=open("sample.txt","a")
# f.write("\nAnd this is write line using append..")
# f.close()

## when you override the text at the stating of the file  you can use the "r+" mode
# f=open("demo.txt","r+")
# f.write("ABCDE")
# print(f.read()) 
# f.close()


# ## Using "w+" mode first of all file is empty and than you can write data in file
# f=open("demo.txt","w+") 
# print(f.read()) 
# f.write("ABCDE")
# f.close()

## using the "a+" mode you can read and append data in file, using "a" only append the data not read the data 
# f=open("demo.txt","a+")  
# print(f.read()) 
# f.write("ABCDE")
# f.close()




## with Syntax

# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)             
#     ## Using the with syntax, it is close file automatically 
    
# with open("demo.txt","w") as f:
#     data=f.write("New data")
#     print(data) ## it print number of character in string 


## Deleteing a file in I/O operation 
# import os
# os.remove("sample.txt")



class Parent:
    hair_color = "brown"

class Child(Parent):
    hair_color = "purple"
    
c=Child()
print(c.hair_color)
p=Parent()
print(p.hair_color)

with open("std.txt","r") as fc: 
    line=len(fc.readlines())
    print("Total lines is :",line)

file=open("std.txt","r")
count=0
for line in file:
    word=line.split()
    count=count+len(word)

print("Number of word:"+str(count))
file.close()





# #Menu driven program to do various list operations
# myList = [22,4,16,38,13] #myList already has 5 elements
# choice = 0
# while True:
#  print("The list 'myList' has the following elements", myList)
#  print("\nL I S T O P E R A T I O N S")
#  print(" 1. Append an element")
#  print(" 2. Insert an element at the desired position")
#  print(" 3. Append a list to the given list")
#  print(" 4. Modify an existing element")
#  print(" 5. Delete an existing element by its position")
#  print(" 6. Delete an existing element by its value")
#  print(" 7. Sort the list in ascending order")
#  print(" 8. Sort the list in descending order")
#  print(" 9. Display the list")
#  print(" 10. Exit")
#  choice = int(input("ENTER YOUR CHOICE (1-10): "))
#  #append element
#  if choice == 1: 
#   element = int(input("Enter the element to be appended: "))
#   myList.append(element)
#   print("The element has been appended\n")
#  #insert an element at desired position
#  elif choice == 2: 
#   element = int(input("Enter the element to be inserted: "))
#   pos = int(input("Enter the position:"))
#   myList.insert(pos,element)
#   print("The element has been inserted\n")
#  #append a list to the given list
#  elif choice == 3:
#   newList = eval(input( "Enter the elements separated by commas"))
#   myList.extend(list(newList))
#   print("The list has been appended\n")
#  #modify an existing element
#  elif choice == 4: 
#   i = int(input("Enter the position of the element to be modified: "))
#   if i < len(myList):
#     newElement = int(input("Enter the new element: "))
#     oldElement = myList[i]
#     myList[i] = newElement
#     print("The element",oldElement,"has been modified\n")
#   else:
#     print("Position of the element is more than the length of list")
#  #delete an existing element by position
#  elif choice == 5: 
#   i = int(input("Enter the position of the element to be deleted: "))
#   if i < len(myList):
#     element = myList.pop(i)
#     print("The element",element,"has been deleted\n")
#   else:
#     print("\nPosition of the element is more than the length of list")
#  #delete an existing element by value
#  elif choice == 6: 
#   element = int(input("\nEnter the element to be deleted: "))
#   if element in myList:
#     myList.remove(element)
#     print("\nThe element",element,"has been deleted\n")
#   else:
#     print("\nElement",element,"is not present in the list")
#  #list in sorted order
#  elif choice == 7: 
#   myList.sort()
#   print("\nThe list has been sorted")
#  #list in reverse sorted order
#  elif choice == 8: 
#   myList.sort(reverse = True)
#   print("\nThe list has been sorted in reverse order")
#  #display the list
#  elif choice == 9: 
#   print("\nThe list is:", myList)
#  #exit from the menu
#  elif choice == 10: 
#   break
#  else:
#   print("Choice is not valid")
#   print("\n\nPress any key to continue..............")
#   ch = input()








#   # defining functions  
# def p_circle(radius):  
#     para = 2 * 3.14 * radius  
#     print("Parameter of Circle:", para)  
  
# def p_rectangle(height, width):  
#     para = 2 * (height + width)  
#     print("Parameter of Rectangle:", para)  
  
# def p_square(side):  
#     para = 4 * side  
#     print("Parameter of Square:", para)  
  
# def a_circle(radius):  
#     area = 3.14 * radius * radius  
#     print("Area of Circle:", area)  
  
# def a_rectangle(height, width):  
#     area = height * width  
#     print("Area of Rectangle:", area)  
  
# def a_square(side):  
#     area = side * side  
#     print("Area of Square:", area)  
  
# # printing the starting line  
# print("WELCOME TO A SIMPLE MENSURATION PROGRAM")  
  
# # creating options  
# while True:  
#     print("\nMAIN MENU")  
#     print("1. Calculate Parameter")  
#     print("2. Calculate Area")  
#     print("3. Exit")  
#     choice1 = int(input("Enter the Choice:"))  
  
#     if choice1 == 1:  
#         print("\nCALCULATE PARAMETER")  
#         print("1. Circle")  
#         print("2. Rectangle")  
#         print("3. Square")  
#         print("4. Exit")  
#         choice2 = int(input("Enter the Choice:"))  
  
#         if choice2 == 1:  
#             radius = int(input("Enter Radius of Circle:"))  
#             p_circle(radius)  
              
#         elif choice2 == 2:  
#             height = int(input("Enter Height of Rectangle:"))  
#             width = int(input("Enter Width of Rectangle:"))  
#             p_rectangle(height, width)  
              
#         elif choice2 == 3:  
#             side = int(input("Enter Side of Square:"))  
#             p_square(side)  
  
#         elif choice2 == 4:  
#             break  
              
#         else:  
#             print("Oops! Incorrect Choice.")  
      
#     elif choice1 == 2:  
#         print("\nCALCULATE AREA")  
#         print("1. Circle")  
#         print("2. Rectangle")  
#         print("3. Square")  
#         print("4. Exit")  
#         choice3 = int(input("Enter the Choice:"))  
  
#         if choice3 == 1:  
#             radius = int(input("Enter Radius of Circle:"))  
#             a_circle(radius)  
              
#         elif choice3 == 2:  
#             height = int(input("Enter Height of Rectangle:"))  
#             width = int(input("Enter Width of Rectangle:"))  
#             a_rectangle(height, width)  
              
#         elif choice3 == 3:  
#             side = int(input("Enter Side of Square:"))  
#             a_square(side)  
  
#         elif choice3 == 4:  
#             break  
              
#         else:  
#             print("Oops! Incorrect Choice.")  
      
#     elif choice1 == 3:  
#         break  
      
#     else:  
#         print("Oops! Incorrect Choice.")



from functools import reduce

a = [1, 24, 76, 23, 12]

# Find the largest number using reduce
largest = reduce(lambda x, y: x if x > y else y, a)
smallest = reduce(lambda x, y: x if x < y else y, a)
print(largest)
print(smallest)
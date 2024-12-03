
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
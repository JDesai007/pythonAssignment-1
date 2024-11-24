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
f=open("demo.txt","r")
d=f.read(7)
print(d)
f.close()

## Print only no. of line in the read() 



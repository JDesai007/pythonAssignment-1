f1=open("files.txt","r")
f2=open("filesdest.txt","w")

for line in f1:
    f2.write(line)
    print("File copy successfully...")
f1.close()
f2.close()

def replace_word():
    with open("practice.txt","r") as f:  
        data=f.read()
        
    new=data.replace("gujrat","Gujarat")
    print(data)
    print(new)

    with open("practice.txt","w") as f:
        f.write(new)
replace_word()
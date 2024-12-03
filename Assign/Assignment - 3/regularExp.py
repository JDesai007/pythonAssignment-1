
## Syambols for Regular expression in python

# []  "[a-z]" - set of character
# [] "[abc]" - start with character
# \   "\d" - can also be user to escape special character
# .  "ma..o" - except newline character
# ^ "^hello" - Start with
# [^abc] -  return match character EXCEPT(skip this character) a,b,and c
# $ ".com$" - Ends with
# * "X*"... - zero or more occurences
# + "a+",... - One or more occurences 
# {} "q{2}" - Exactly the specified number of occurences
# | "yes|no" Either or
# ? "x?" zero or one occurences


## special sequence

# \d - return a match where the starting contain digit (number from 0-9)
# \D - return a match where the starting DOES NOT contain digit 
# \s - white space character
# \S - DOSE NOT contain white space character
# \w - character a-z, A-Z, 0-9, _(Underscore)
# \W - DOES NOT contain any character


import re 

crick_score=""" Schine score 760 and Dravid score 40 and \nVirat score 77 in the border - gavasker trophy is played in australiya """
# findall() it return the list containing all matches patterns
# f=re.findall(r'[A-Z][a-z]*',crick_score)
f=re.findall(r'[A-Z][a-z]*',crick_score)
print(f)
score=re.findall(r'\d{2}',crick_score)
print(score)

# Using dictionary you can make name and score board
crick_dict={}
i=0
for x in f:
    crick_dict[x]=score[i]
    i+=1
print(crick_dict)


## Find the match sring using serch() , it return match object if match is found than return gives

str= " Hii i am desai i am from Gujarat Vidhyapith - Ahmedabad"
if re.search(r"am",str):
    print("String is found")
    match=re.findall(r"am",str)
    print(match)
    for i in match:
        print(i)



## Find string Index using finditer()

for i in re.finditer("am",str):
    index=i.span() # span() return the starting and ending index of word whicch match to the regular exprression
    print(index)

# Find data from string in start with specific charater 

str2="Rat Cat Pat Mat Sat Dat Gat Qat"
data=re.findall(r"[CPG]at",str2)
print(data)
for i in data:
    print(i)

#Skip the match chacter and print only annother match character
data1=re.findall(r"[^CPG]at",str2)
print(data1)

# skip data bbetween the range of character
data2=re.findall(r"[^P-R]at",str2)
print(data2)

# compile() used for various operations like searching, matching, and substituting within strings.
reg=re.compile(r"[R]at")
#print(reg)
str2=reg.sub("Lion",str2) # it is used to search pattern in string and replace it with another string
print(str2)


## print the diffrent line into one line 
str4="""How are you
Iam fine
Thank you."""

print(str4)
reg=re.compile(r"\n") 
str4=reg.sub(" ",str4) 
print(str4)

## Find the number of digit in pattern using len()
patter="A123456r7778f"
print("Number of digit :",len(re.findall(r'\d',patter)))

## find the number is arrive in no. of time in string
print("Number of Time :",len(re.findall(r'\d{7}',patter)))

## find the number of Alfabet in strind
print("Number of Time :",len(re.findall(r'\D',patter)))

## find the number between range of number and find it number of time arrives
multinum="12 123 1234 12345 123456 1234567"
x=len(re.findall(r'\d{3,7}',multinum))
print("No of digit:",x)


phone="my phone number is 02244-222568"
if re.search(r"\d{5}-\d{6}",phone):
    print("Valid")
    match=re.findall(r"\d{5}-\d{6}",phone)
    print(match)
 
 
name="Jaydip Desai"
if re.search(r"\w{2,20}\s\w{2,20}",name):
    print("Valid..")
    match=re.findall(r"\w{2,20}\s\w{2,20}",name)
    print(match)
       
phone1="my phone number is +91 4567898765"
if re.search(r"\+\d{2}\s\d{10}",phone1):
    match=re.findall(r"\+\d{2}\s\d{10}",phone1)
    print(match)


## Find email id out of long text
email="abc67@gmail.com and abc@aajfhasffg.com and my12@gmail.com and abx76@gmaul.....c"
e=re.findall(r"\w+@\w+.\w*",email)
print(e)


text="ToPsy TuRvy"
w1,w2=text.split()
print(w1.swapcase(),w2.title().swapcase())

## find URL
url="https://goggle.com"
u=re.findall(r"\w+://\w+.\w*",url)
print(u)


    







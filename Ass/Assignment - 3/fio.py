
import re
crick_score=""" Schine score 760 and Dravid score 40 and \nVirat score 77 in the border - gavasker trophy is played in australiya """
f=re.findall(r'[A-Z][a-z]*',crick_score)
print(f)

s=re.findall(r'\d{2}',crick_score)
print(s)

dict={}
i=0
for x in f:
    dict[x]=s[i]
    i+=1
    
print(dict)
    
    
str= " Hii i am desai i am from Gujarat Vidhyapith - Ahmedabad"
if re.search(r"am",str):
    print("String is found")
    match=re.findall(r"am",str)
    print(match)
    for i in match:
        print(i)

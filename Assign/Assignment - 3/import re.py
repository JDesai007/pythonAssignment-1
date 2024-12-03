import re

text = "hello my email ID is desai@cse.itmse.ac.in in ZANKHI@itmc.ac.in the zankhi@gmail.com a zankhi@usa.net and @rupeshsomething was the one i said"
regex=r'\w+@\w+'
emails=re.findall(regex,text.lower())
print(emails)
import re
text="HHHiii09"

match="^[A-Za-z0-9]+$"
if re.fullmatch(match,text):
    print("Text is match")
else:
    print("Text not match")











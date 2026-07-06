import re

pattern = r'^M(?=.*[0-5])(?=.*\s).*D$'

string = "M test 3 D"
match = re.search(pattern, string)
if match:
    print(match.group())
else:
    print("pattern not found")

string2 = "MD"
match2 = re.search(pattern, string2)
if match2:
    print(match2.group())
else:
    print("pattern not found")
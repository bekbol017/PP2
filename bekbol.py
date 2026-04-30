#Read two lines: a string S and a pattern P (a literal string without regex symbols). Using re.findall() or re.finditer(), count how many times P appears in S as a non-overlapping match.


import re
aru = input()
aiz = re.findall(r"\d",aru)


print(" ".join(aiz))
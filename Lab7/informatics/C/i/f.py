x = input()
res = ''
isFound = False
for i in reversed(x):
    if (i != '0'):
       res += i
       isFound = True
    elif i == '0' and isFound:
        res += i
print(res) 
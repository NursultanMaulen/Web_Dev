import math
a = int(input())
su = 0
for i in range(1, int(math.sqrt(a)) + 1):
    if a % i == 0:
        if int(a / i) == i:
            su += 1
        else:
            su += 2
print(su)
n = input()
k = 0
su = 0
for i in reversed(n):
    if i == '1':
        su += 2 ** k
    k += 1
print(su)
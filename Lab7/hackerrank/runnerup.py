n = int(input())
arr = [int(i) for i in input().split()]
cur = -100
maxi = -100
for i in arr:
    if i > maxi:
        maxi = i
for i in arr:
    if i < maxi and i > cur:
        cur = i
print(cur)
k = [int(i) for i in input().split()]
n = k[0]
maxSum = 0
ind = 0
for i in range(n):
    cur = 0
    r = [int(e) for e in input().split()]
    for k in r:
        cur += k
    if maxSum < cur:
        maxSum = cur
        ind = i
print(maxSum, ind, sep = '\n')
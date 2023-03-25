k = [int(i) for i in input().split()]
n = k[0]
maxi = 0
maxj = 0
curMax = 0
for i in range(n):
    r = [int(e) for e in input().split()]
    # print(r)
    for k in range(len(r)):
        if r[k] > curMax:
            maxi = i
            maxj = k
            curMax = r[k] 
            # print(maxi, maxj, curMax)        
print(curMax)
print(maxi, maxj)
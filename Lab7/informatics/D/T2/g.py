n, m = map(int, input().split())

a = []
maximum1 = 0
s = 0
k = []

for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)

for i in range(n):
    for j in range(m):
        if a[i][j] > maximum1:
            maximum1 = a[i][j]

for i in range(n):
    for j in range(m):
        if a[i][j] == maximum1:
            s += 1
            k.append(i)
            break

print(s)
for i in sorted(k):
    print(i)
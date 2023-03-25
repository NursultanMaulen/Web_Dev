n, m = map(int, input().split())

a = []
maximum1 = 0
stroka1 = 0
stroka2 = 0
c = []
s = 0
igrok = 0

for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)

for i in range(n):
    for j in range(m):
        if a[i][j] > maximum1:
            maximum1 = a[i][j]
            stroka1 = i

for i in range(n):
    for j in range(m):
        if a[i][j] == maximum1:
            c.append(i)

for i in range(len(c)):
    if sum(a[c[i]]) > s:
        igrok = c[i]
        s = sum(a[c[i]])

print(igrok)
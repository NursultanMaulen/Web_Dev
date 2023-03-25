n = int(input())
t = n - 1
for i in range(n):
    for j in range(n):
        if j == t:
            print(1, end = ' ')
        elif j > t:
            print(2, end = ' ')
        else:
            print(0, end = ' ')
    t -= 1
    print()
    
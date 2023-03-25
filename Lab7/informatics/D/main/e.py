n = int(input())
my_list = [int(i) for i in input().split()]
cnt = 0
isIt = False
for i in range(1, n):
    if (my_list[i - 1] >= 0 and my_list[i] >= 0) or (my_list[i - 1] < 0 and my_list[i] < 0):
        isIt = True
        break
if isIt:
    print("YES")
else:
    print("NO")

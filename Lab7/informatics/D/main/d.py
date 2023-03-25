n = int(input())
my_list = [int(i) for i in input().split()]
cnt = 0
for i in range(1, n):
    if my_list[i - 1] < my_list[i]:
        cnt += 1
print(cnt)

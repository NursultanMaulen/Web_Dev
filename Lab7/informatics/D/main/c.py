n = int(input())
my_list = [int(i) for i in input().split()]
cnt = 0
for i in my_list:
    if i > 0:
        cnt += 1
print(cnt)

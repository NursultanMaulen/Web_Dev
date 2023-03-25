n = int(input())
my_list = [int(i) for i in input().split()]
for i in range(0, n, 2):
    print(my_list[i], end = ' ')
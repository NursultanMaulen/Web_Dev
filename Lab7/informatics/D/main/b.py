n = int(input())
my_list = [int(i) for i in input().split()]
for i in my_list:
    if i % 2 == 0:
        print(i, end = ' ')

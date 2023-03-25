n = int(input())
my_list = []
isTrue = True
for i in range(n):
    temp = [int(k) for k in input().split()]
    my_list.append(temp)    
for i in range(n):
    for j in range(n):
        if my_list[i][j] != my_list[j][i]:
            isTrue = False
            break
if isTrue:
    print('yes')
else:
    print('no')
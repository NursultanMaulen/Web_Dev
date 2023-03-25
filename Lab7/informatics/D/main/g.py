n = int(input())
list_ = [int(i) for i in input().split()]
su = 0
for i in range(0, int(len(list_)/2)):
    list_[i], list_[n - i - 1] = list_[n - i - 1], list_[i]
for i in list_:
    print(i, end = ' ')
    
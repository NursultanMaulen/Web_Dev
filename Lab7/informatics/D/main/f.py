n = int(input())
list_ = [int(i) for i in input().split()]
su = 0
for i in range(1, len(list_) - 1):
    if (list_[i - 1] < list_[i]) and (list_[i + 1] < list_[i]):
        su += 1
print(su)
    
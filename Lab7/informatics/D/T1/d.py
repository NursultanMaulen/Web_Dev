list_ = [int(i) for i in input().split()]
for i in range(1, len(list_)):
    if list_[i - 1] < list_[i]:
        print(list_[i], end = ' ')
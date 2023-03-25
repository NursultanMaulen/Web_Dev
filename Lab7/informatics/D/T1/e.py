list_ = [int(i) for i in input().split()]
for i in range(1, len(list_)):
    if (list_[i - 1] >= 0 and list_[i] >= 0) or (list_[i - 1] < 0 and list_[i] < 0):
        print(list_[i - 1], list_[i])
        break
    
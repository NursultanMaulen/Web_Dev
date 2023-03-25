list_ = [int(i) for i in input().split()]
ma = list_[0]
ma_in = 0
for i in range(0, len(list_)):
    if ma < list_[i]:
        ma = list_[i]
        ma_in = i
print(ma, ma_in)
    
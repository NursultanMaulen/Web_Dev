v = int(input())
t = int(input())
if v < 0:
    print((109 - abs(v * t)) % 109)
elif v > 0:
    print((v * t) % 109)
else:
    print(0)
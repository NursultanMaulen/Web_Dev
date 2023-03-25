def xor(a, b):
    return bool(a) != bool(b)
a, b = map(int, input().split())
print(int(xor(a, b)))
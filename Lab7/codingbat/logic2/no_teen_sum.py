def no_teen_sum(a, b, c):
  sum = a + b + c
  if 13 <= a <= 14 or 17<= a <= 19:
    sum -= a
  if 13 <= b <= 14 or 17<= b <= 19:
    sum -= b
  if 13 <= c <= 14 or 17<= c <= 19:
    sum -= c
  return sum
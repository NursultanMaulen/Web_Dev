def in1to10(n, outside_mode):
  return True if (outside_mode and (n <= 1 or n >= 10)) or (not outside_mode and (1 <= n <= 10)) else False

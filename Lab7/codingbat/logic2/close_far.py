def close_far(a, b, c):
  return True if (abs(a - b) <= 1 and abs(b - c) >= 2 and abs(a - c) >= 2) or (abs(a - c) <= 1 and abs(c - b) >= 2  and abs(a - b) >= 2) else False 

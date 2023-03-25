def make_chocolate(small, big, goal):
  if goal - big*5 <0:
    if goal%5 <= small:
      return goal%5
    else:
      return -1
  else:
    if goal - big*5 <= small:
      return goal - big*5
    else:
      return -1

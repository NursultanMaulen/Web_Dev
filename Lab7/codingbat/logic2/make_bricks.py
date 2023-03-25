def make_bricks(small, big, goal):
  if goal - 5*big < 0:
    if goal % 5 <= small:
      return True
    else:
      return False
  else:
    goal -= 5*big
    if goal <= small:
      return True
    else:
      return False
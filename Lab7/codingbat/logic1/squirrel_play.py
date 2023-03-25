def squirrel_play(temp, is_summer):
  if is_summer and 60 <= temp <= 100:
    return True
  elif not is_summer and 60 <= temp <= 90:
    return True
  else:
    return False

def cat_dog(str):
  cnt_cat = 0
  cnt_dog = 0
  for i in range(len(str) - 2):
    if(str[i:i+3] == 'cat'):
      cnt_cat += 1
    elif(str[i:i+3] == 'dog'):
      cnt_dog += 1
  if cnt_cat == cnt_dog:
    return True
  return False
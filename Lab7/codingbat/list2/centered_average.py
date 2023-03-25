def centered_average(nums):
  mini = 100
  maxi = -100
  su = 0
  for i in nums:
    mini = min(mini, i)
    maxi = max(maxi, i)
  for i in nums:
    if i == mini:
      mini = 10000
      continue
    if i == maxi:
      maxi = 100000
      continue
    su += i
  return su / (len(nums)-2)
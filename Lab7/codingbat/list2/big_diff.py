def big_diff(nums):
  mini = 100
  maxi = 0
  for i in nums:
    maxi = max(maxi, i)
    mini = min(mini, i)
  return maxi - mini

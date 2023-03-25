def sum67(nums):
  res = 0
  isFake = False
  for i in range(len(nums)):
    if nums[i] == 7:
      if isFake:
        isFake = False
        continue
    if nums[i] == 6:
      isFake = True
      continue
    if isFake:
      continue
    res += nums[i]
  return res

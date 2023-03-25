def sum13(nums):
  res = 0
  for i in range(len(nums)):
    if nums[i] == 13:
      if i != len(nums) - 1:
        if nums[i + 1] == 13:
          continue
        res -= nums[i + 1]
      else:
        break
      continue
    res += nums[i]
  return res
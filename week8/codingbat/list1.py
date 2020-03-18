def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  else:
    return False

def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[-1]:
    return True
  else:
    return False

def make_pi():
  return [3, 1, 4]

def common_end(a, b):
  if a[-1] == b[-1] or a[0] == b[0]:
    return True
  else:
    return False

def sum3(a):
  return a[0] + a[1] + a[2]

def rotate_left3(a):
  return [a[1], a[2], a[0]]

def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

def max_end3(a):
  max = -1
  if a[0] > a[2]:
    max = a[0]
  if a[2] >= a[0]:
    max = a[2]
    
  return [max, max, max]

def sum2(nums):
  if len(nums) >=2:
    return nums[0] + nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0

def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
  return [nums[0], nums[-1]] 

def has23(nums):
  if nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3:
    return True
  else:
    return False
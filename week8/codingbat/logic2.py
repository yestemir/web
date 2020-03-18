def make_bricks(small, big, goal):
  if (goal%5)<=small and (goal-(big*5))<=small:
    return True
  else:
    return False

def lone_sum(a, b, c):
  if a==b and b == c and c== a:
    return 0
  if a==b:
    return c
  if a == c:
    return b
  if c == b:
    return a
  else:
    return a+b+c

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  if b == 13:
    return a
  if c ==13:
    return a+b
  else:
    return a+b+c




def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
    
def fix_teen(n):
    if 13 <= n and n <= 19 and n != 15 and n!= 16:
        return 0
            
    return n



def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)
    
def round10(num):
    if num % 10 < 5:
        return num - (num % 10)
        
    return num + (10 - num % 10)




def close_far(a, b, c):
    a_b_diff = abs(a - b)
    a_c_diff = abs(a - c)
    b_c_diff = abs(b - c)
    b = False
    c = False
    
    if a_b_diff <= 1 and a_c_diff >= 2 and b_c_diff >= 2:
      b = True
    if a_c_diff <= 1 and a_b_diff >= 2 and b_c_diff >= 2:
      c = True
    
    return b != c

def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5
        
    if remainder <= small:
        return remainder
        
    return -1
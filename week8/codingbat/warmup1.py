def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

def monkey_trouble(a_smile, b_smile):
  if (a_smile == True and b_smile == True) or (a_smile == False and b_smile == False):
    return True
  else:
    return False

def sum_double(a, b):
  if a == b:
    return 2 *(a+b)
  else:
    return a+b

def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return 2 * (n -21)

def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  else:
    return False

def makes10(a, b):
  if a + b == 10 or a == 10 or b == 10:
    return True
  else:
    return False

def near_hundred(n):
  if abs(100 - n) <= 10 or abs(200 - n) <= 10:
    return True
  else:
    return False

def pos_neg(a, b, negative):
  if (a < 0 and b > 0 and negative == False) or (a > 0 and b < 0 and negative == False):
    return True
  elif a <0 and b<0 and negative == True:
    return True
  else:
    return False

def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  else:
    return "not " + str

def missing_char(str, n):
  f = str[:n]
  b = str[n+1:]
  return f + b

def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]
  
  return str[len(str)-1] + mid + str[0]

def front3(str):
  f = str[:3]
  return f+f+f


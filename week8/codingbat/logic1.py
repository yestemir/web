def cigar_party(c, is_weekend):
  if c >= 40 and c<= 60 and is_weekend == False:
    return True
  elif is_weekend == True and c >= 40:
    return True
  else:
    return False
    
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >=8 or date >= 8:
    return 2
  else:
    return 1

def squirrel_play(t, is_summer):
  if t >= 60 and t <= 90 and is_summer == False:
    return True
  elif is_summer == True and t >=60 and t <=100:
    return True
  else:
    return False

def caught_speeding(s, is_b):
  if is_b == True:
    s -= 5
  if s <= 60:
    return 0
  elif s >= 61 and s <=80:
    return 1
  else:
    return 2

def sorta_sum(a, b):
  if a+b >=10 and a+b <= 19:
    return 20
  else:
    return a+b

def alarm_clock(day, vacation):
  if day >=1 and day <=5 and vacation == True:
    return "10:00"
  elif day >=1 and day <=5:
    return "7:00"
  elif (day ==6 or day == 0)and vacation == True:
    return "off"
  elif day ==6 or day == 0:
    return "10:00"

def love6(a, b):
  if a == 6 or b == 6 or abs(a-b)==6 or a+b == 6:
    return True
  else:
    return False

def in1to10(n, outside_mode):
  if n >=1 and n <=10 and outside_mode == False:
    return True
  elif outside_mode == True and (n <= 1 or n >= 10):
    return True
  else:
    return False

def near_ten(num):
  if num%10 <=2 or num%10 >= 8:
    return True
  else:
    return False


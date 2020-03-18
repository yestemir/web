import math
x = int(input())
if x == 0:
	d = 0
elif x == 1:
    d = 1
else:
    d = 2
    for i in range(2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
    		d += 2

print(d)
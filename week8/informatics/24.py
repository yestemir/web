import math
n = int(input())

x = int(math.sqrt(n)) + 1
val = 1

while val <= x:
	if val == x:
    val*=2

print(val)
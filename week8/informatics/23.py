n = int(input())
value = 1
b = False
while value <= n:
    if value == n:
        b=True
    value*=2

if b == True:
    print("YES")
else:
    print("NO")
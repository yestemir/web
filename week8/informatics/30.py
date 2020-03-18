n = int(input())

s = input()
a = s.split()

for i in range(n):
	a[i] = int(a[i])

b = False

for i in range(n-1):
	if (a[i] > 0 and a[i+1] > 0) or (a[i] < 0 and a[i+1] < 0):
		b = True
		print('YES')
		break

if(b == False):
	print('NO')
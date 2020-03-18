n = int(input())
a = []

a = input().split()

for i in range(n):
	a[i] = int(a[i])

for i in range(int(n/2)):
	temp = a[i]
	a[i] = a[n-i-1]
	a[n-i-1] = temp

for i in range(n):
	print(a[i], end =' ')
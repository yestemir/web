n = int(input())
a = []

j = input()
a = j.split()

for i in range(n):
    a[i] = int(a[i])

for i in range(0, n):
	if(a[i] % 2 == 0):
		print(a[i], end = ' ')
	
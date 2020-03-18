n = int(input())
a = []

j = input()
a = j.split()

for i in range(n):
    a[i] = int(a[i])

for i in range(0, n, 2):
	print(a[i], end = ' ')
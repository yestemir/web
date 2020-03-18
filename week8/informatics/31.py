n = int(input())
a = []

a = (input()).split()

for i in range(n):
	a[i] = int(a[i])

cnt = 0

for i in range(1, n-1):
	if a[i] > a[i-1] and a[i] > a[i+1]:
		cnt +=1

print(cnt)
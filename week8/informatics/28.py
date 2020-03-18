n = int(input())
a= []

s = input()
a = s.split()

for i in range(n):
	a[i] = int(a[i])

cnt = 0

for i in range(n):
	if(a[i] > 0):
		cnt += 1

print(cnt)
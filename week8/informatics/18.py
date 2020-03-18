cnt = 0
c = int(input())
a = []

for i in range(c):
	x = int(input())
	a.append(x)


for x in a:
	cnt += x


print(cnt)
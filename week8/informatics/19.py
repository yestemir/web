cnt = 0
c = int(input())
a = []

for i in range(c):
	x = int(input())
	a.append(x)


for x in a:
	if x == 0:
		cnt += 1


print(cnt)
a = int(input())

for i in range(a+1):
	if i > 1 and a%i == 0:
		print(i)
		break
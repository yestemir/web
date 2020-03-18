def power(a, n):
	val = 1
	i = 0
	while i < n:
		val *= a
		i+=1
	print(val)

m = []
s = input()
m = s.split()

a = float(m[0])
n = int(m[1])

power(a, n)
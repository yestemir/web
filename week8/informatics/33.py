
def min(a,b,c,d):
	min = float('inf')
	if min > a:
		min = a
	if min > b:
		min = b
	if min > c:
		min = c
	if min > d:
		min = d
	print(min)


m = []
s = input()
m = s.split()

a = int(m[0])
b = int(m[1])
c = int(m[2])
d = int(m[3])


min(a,b,c,d)

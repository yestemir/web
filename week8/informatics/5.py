v0 = input()
t0 = input()

v = int(v0)
t = int(t0)

if v > 0:
	print((v*t)%109)
if v < 0:
	print((109+(v*t%109))%109)
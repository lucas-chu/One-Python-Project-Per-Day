#euler
for n in range(1,100,10):
	print((1+(1/n))**n)
#2
for n in range(0,10):
	x = 0
	for i in range(0,n):
		x = x + 1/2**i
	print(x)

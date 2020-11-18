
calculate = 13
a=0
b=1
counted = 0
while counted < calculate:
	print(a, end=', ')
	c = a + b
	a = b
	b = c
	counted += 1

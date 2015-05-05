x = input("input first number")
y = input("input second number")
while(True):
	z = x%y
	if z == 0:
		key = y
		break
	x = y
	y = z 
print key
	


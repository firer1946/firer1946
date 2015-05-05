a = input("please input a number between 0 and 1 \n" )
print a,"=",
b = 100 * a

for x in [25,10,5]:
	flat = 0
	if b >= x:
		while b>= x:
			b -= x
			flat += 1
		if b == 0:
			print " %s * %s "%(flat,x),
		else:
			print " %s * %s +"%(flat,x),
if b>0:
	print "%s*1" % int(round(b)),
			


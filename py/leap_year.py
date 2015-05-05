a = input("input a year:")
print "%s is " % a
if a % 100 == 0 :
	if a% 4 == 0:
		print "a leap year"
	else:
		print "not a leap year"
elif a%4 == 0:
	print "a leap year"
else:
	print "not a leap year"
	

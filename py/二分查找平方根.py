x = 123456789 
epsilon = 0.01
numGuess = 0
low = 0.0
high = x
ans = (high + low)/2.0
while (abs(ans**2-x) >= epsilon):
	print "low=%s high= %s ans=%s" %(low,high,ans)
	numGuess += 1
	if ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (high+low)/2.0
print "numGuess"+str(numGuess)
print str(ans)+'is closed to square root of'+str(x)

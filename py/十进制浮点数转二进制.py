num = input()
p = 0
while(((2**p)*num) % 1 != 0):
	print "Remainder = ", str((2**p)*num - int((2**p)*num)),"\n"
	p+=1

num = int(num*(2**p))
result = ""
while num > 0:
	result = str(num%2) + result
	num = num/2
for i in range(p - len(result)):
	result = "0" + result
print result[0:-p]+"."+result[-p:]


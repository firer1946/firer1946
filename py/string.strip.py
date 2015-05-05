a = raw_input()
def splitspace(x):
	flat1 = 0
	flat2 = 0
	for i in a:
		if i == ' ':
			flat1+=1
		else:
			break
	for i in a[-1:-1]:
		if i == ' ':
			flat2 += 1
		else:
			break
	print a[flat1:len(a) - flat2]
splitspace(a)

	

import string
alphas = string.letters + '_'
nums = string.digits

print 'welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long'
my_input = raw_input('Identifier to test?')
if len(my_input) > 1:
	if my_input[0] not in alphas:
		print''' Invalid : the first symbol must be alphabetic  '''
	else:
		for eachchar in my_input:
			if eachchar not in alphas+nums:
				print ''' The remaining symbols must be alphanmuberic '''
			break
else:
	print 'ok,as an Identifier'

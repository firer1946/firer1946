quene = []
def enQ():
	quene.append(raw_input('Enter new string:').strip())
def delQ():
	if len(quene) == 0:
		print "Invalid:you can't remove a empty quene"
	else:
		"removed [",quene.pop(0),"]"
def viewQ():
	print quene
CMDs = {'e':enQ,'d':delQ,'v':viewQ}

def showmenu():
	pr = """please select a choice:
	(e)nQ
	(d)elQ
	(v)iewQ
	(q)uit  
	Enter a choice:"""
	while True:
		while True:
			try:
				choice = raw_input(pr).strip()[0].lower()
			except(EOFError,KeyboardInterrupt,IndexError):
				choice = 'q'
			if choice not in 'edvq':
				print 'Invalid opinion,please try again!'
			else: 
				break
		if choice == 'q':
			break
		else:
			CMDs[choice]()
if __name__ == '__main__':
	showmenu()
	

#coding:utf-8
import random
tips = ''' please input
1.����
2.ʯͷ
3.��  
4.�˳� 
'''
dict = {1:'����',2:'ʯͷ',3:'��'}
while(True):
	playerc = input(tips)
	if playerc == 4:
		break
	pcchoice = random.choice([1,2,3])
	print "�ҳ�%s" % dict[pcchoice],
	if playerc in [1] and pcchoice in [3]:
		print "��Ӯ�ˣ�"
	elif playerc == 3 and pcchoice == 1:
		print "�����ˣ�������"
	else:
		result = cmp(playerc,pcchoice)
		if result == 0:
			print "ƽ�֣�������"
		if result == 1:
			print "��Ӯ�ˣ�"
		if result == -1:
			print "�����ˣ�������"



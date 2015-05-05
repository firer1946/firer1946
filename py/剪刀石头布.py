#coding:utf-8
import random
tips = ''' please input
1.剪刀
2.石头
3.布  
4.退出 
'''
dict = {1:'剪刀',2:'石头',3:'布'}
while(True):
	playerc = input(tips)
	if playerc == 4:
		break
	pcchoice = random.choice([1,2,3])
	print "我出%s" % dict[pcchoice],
	if playerc in [1] and pcchoice in [3]:
		print "你赢了！"
	elif playerc == 3 and pcchoice == 1:
		print "你输了，哈哈！"
	else:
		result = cmp(playerc,pcchoice)
		if result == 0:
			print "平手，再来！"
		if result == 1:
			print "你赢了！"
		if result == -1:
			print "你输了，哈哈！"



#coding:utf-8
import time
a = "2014/08/05"
t = time.mktime(time.strptime(a,"%Y/%m/%d")) #字符串转时间戳
print time.ctime(t)
print "字符时间：%s" % time.strftime("%Y/%m/%d",time.localtime())   #时间戳转字符串
print "时间戳：%s"% time.time()
print "struct_time :%s" % time.localtime()

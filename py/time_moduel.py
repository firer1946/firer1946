#coding:utf-8
import time
a = "2014/08/05"
t = time.mktime(time.strptime(a,"%Y/%m/%d")) #�ַ���תʱ���
print time.ctime(t)
print "�ַ�ʱ�䣺%s" % time.strftime("%Y/%m/%d",time.localtime())   #ʱ���ת�ַ���
print "ʱ�����%s"% time.time()
print "struct_time :%s" % time.localtime()

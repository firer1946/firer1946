fname = raw_input("please input file name")
print "attempt to open file "
try:
    fobj = open(fname,'r')
except IOError,e:
    print "** file open error",e
else:
    for eachline in fobj:
        print eachline,
    print "*****down!***********"
    fobj.close()

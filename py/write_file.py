#!/usr/bin/env python
import os
debug = True
ls = os.linesep

while True:
	
    fname = raw_input("please input filename %s" % ls)
    if os.path.exists(fname):
        print "Error:'%s' already exists" % fname
    else:
        break
all = []
print "\n Enter lines ('.' by it self to quit) \n"
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)
fobj = open(fname+'.txt','w')
fobj.writelines(['%s \n' % x for x in all])
fobj.close()
print "done!"
    

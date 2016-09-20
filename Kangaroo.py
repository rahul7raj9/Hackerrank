#!/bin/python

import sys

val=''
x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
res=''
for i in range(1,10000):
    if x1+(v1*i)==x2+(v2*i):
        res='YES'
        break
    else:
        res='NO'
        
print res
        

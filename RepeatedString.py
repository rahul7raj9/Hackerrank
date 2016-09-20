#!/bin/python

import sys
import math

s = raw_input().strip()
n = long(raw_input().strip())
count=0
for i in range(len(s)):
    if s[i]=='a':
        count=count+1
entry=int(n/len(s))
diff = n-entry*len(s)
if diff==0:
    count=count*entry
else:
    j=0
    for i in range(diff):
        if s[i]=='a':
            j+=1
    count=(count*entry)+j
print count

    
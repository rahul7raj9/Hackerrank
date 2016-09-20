#!/bin/python

import sys


n = int(raw_input().strip())
B = raw_input().strip()
bin_list=[]
bin_list=list(B)
count=0
while '010' in B:
    count+=1
    pos=B.find('010')
    bin_list[pos+2]='1'
    B = ''.join(bin_list)
    
print count
    

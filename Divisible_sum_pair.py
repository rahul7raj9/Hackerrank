#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
count = 0
for i in range(n):
    for j in range(n):
        if i!=j:
            if (a[i]+a[j])%k==0:
                count+=1
print count/2

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
s=raw_input()
n=input()
val=''
for i in range(len(s)):
    if i%n==n-1:
        val+=s[i]
        print ''.join(OrderedDict.fromkeys(val))
        val=''
    else:
        val+=s[i]

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations 
string, n = map(str, raw_input().split(" "))
x=[]
for i in range(1,int(n)+1):
    x=(list(combinations(sorted(string), i)))
    for i in range(len(x)):
        print str("".join(x[i]))

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
string, n = map(str, raw_input().split(" "))
x=[]
x=list(combinations_with_replacement(sorted(string),int(n)))

for i in range(len(x)):
    print str("".join(x[i]))

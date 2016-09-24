from itertools import permutations 
string, n = map(str, raw_input().split(" "))

x=sorted(list(permutations(string, int(n))))

for i in range(len(x)):
    print str("".join(x[i]))

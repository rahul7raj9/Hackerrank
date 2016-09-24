# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n=input()
val = map(str, raw_input().split(" "))
k=input()
a_pos=[]
for i in range(n):
    if val[i]=='a':
        a_pos.append((i+1))
        
x=[]
val_lst=[]
for i in range(1,n+1):
    val_lst.append(i)
    

x=(list(combinations(val_lst, k)))

total_comb=len(x)

count=0

for i in range(total_comb):
    z=set(x[i]).intersection(set(a_pos))
    if list(z):
        count=count+1

print float(count)/total_comb


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n=input()
size=map(int, raw_input().split(" "))
num_cust=input()
earned=0
for i in range(num_cust):
    s, cost=map(int, raw_input().split(" "))
    if s in size:
        size.remove(s)
        earned+=cost
print earned

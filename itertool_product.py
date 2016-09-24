#Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A=map(int, raw_input().split(" "))
B=map(int, raw_input().split(" "))

C=list(product(A,B))
for i in range(len(C)):
    print C[i],

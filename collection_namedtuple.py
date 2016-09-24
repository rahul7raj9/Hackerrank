# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n=input()
average=0
Student=namedtuple('Student',raw_input())
for i in range(n):
    x=Student(*raw_input().strip().split())
    average+=int(x.MARKS)
print float(average)/n


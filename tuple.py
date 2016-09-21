# Enter your code here. Read input from STDIN. Print output to STDOUT
x=input()
n = map(int,raw_input().strip().split(' '))
t=tuple(n)
print hash(t)

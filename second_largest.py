# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
value=map(int, raw_input().strip().split(" "))
value=set(value)
value=sorted(list(value))
print value[-2]

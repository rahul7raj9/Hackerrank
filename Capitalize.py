# Enter your code here. Read input from STDIN. Print output to STDOUT
s=raw_input().split(" ")
s_new=[s[i].capitalize() for i in range(len(s))]
print ' '.join(s_new)

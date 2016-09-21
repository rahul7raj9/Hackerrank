# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
lst=[]
for i in range(n):
    inst=raw_input().split(" ")
    if len(inst)==1:
        if inst[0]=='print':
            print lst
        else:
            cmd='lst.{0}()'.format(inst[0])  
            exec(cmd)
    elif len(inst)==2:
        cmd='lst.{0}({1})'.format(inst[0],inst[1])
        exec(cmd)
    else:
        lst.insert(int(inst[1]),int(inst[2]))
        

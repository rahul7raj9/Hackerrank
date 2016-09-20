x=raw_input()

for i in range(int(x)):
    count=0
    val=raw_input().rstrip()
    for i in range(len(val)-1):
        if val[i]==val[i+1]:
            count+=1
        else:
             pass
    print count

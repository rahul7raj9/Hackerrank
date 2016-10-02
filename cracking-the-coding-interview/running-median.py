from bisect import insort

n = int(raw_input().strip())

a=[]
for i in range(n):
    insort(a,input())
    if (i+1)%2==0:
        print float((a[(i+1)/2-1]+a[(i+1)/2]))/2
    else:
        print float(a[i/2])

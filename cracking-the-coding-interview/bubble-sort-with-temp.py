n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
no_swaps=0
for j in range(n):
    for i in range(n-1):
        if a[i]>a[i+1]:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
            no_swaps+=1
print "Array is sorted in" ,no_swaps, "swaps."
print "First Element:",a[0]
print "Last Element:",a[-1]

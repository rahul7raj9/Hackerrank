# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
bin_n_len=len(bin(n)[2:])
for i in range(1,n+1):
    print ("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b} ".format(i, width=bin_n_len)).upper()
    
   

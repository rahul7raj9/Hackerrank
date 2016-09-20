# Enter your code here. Read input from STDIN. Print output to STDOUT
n, k = raw_input().split(' ')
n,k=[int(n),int(k)]
numbers = map(int, raw_input().split(' '))
#array initialized to 0
counts = [0] * k  
for number in numbers:
    counts[number % k] += 1

count = min(counts[0], 1)
for i in range(1, k/2+1):
    if i != k - i:
        count += max(counts[i], counts[k-i])
if k % 2 == 0: 
    count += 1

print count
def array_left_rotation(a, n, k):
    b=(a[k:])
    b+=(a[:k])
    return b
    

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))

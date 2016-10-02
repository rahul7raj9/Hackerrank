def number_needed(a, b):
    for i in a:
        if i in b:
            a = a.replace(i, "",1)
            b = b.replace(i, "",1)
        else:
            pass
    return len(a)+len(b)
    
        

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

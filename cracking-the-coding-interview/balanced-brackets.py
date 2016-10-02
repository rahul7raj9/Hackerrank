def is_matched(expression):
    stack=[]
    pairs={'}':'{',']':'[',')':'('}
    n=len(expression)
    i=0
    for c in expression:
        if c in pairs.keys() and len(stack)==0:
            return 0
        elif c in pairs.values():
            stack.append(c)
            i+=1
        else:
            key=pairs.get(c)
            if key==stack[-1]:
                stack.pop()
                i+=1
                if len(stack)==0 and i==n:
                    return 1
                continue
            return 0
      
              

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"

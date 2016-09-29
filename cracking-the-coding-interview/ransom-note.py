def ransom_note(magazine, rasom):
    for i in ransom:
        if i in magazine:
            magazine.remove(i)
            pass
        else:
            return 0
    return 1

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    

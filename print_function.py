# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
#map(lambda x: print x+1,xrange(int(raw_input()))
def prnt(x):
    x=x+1
    sys.stdout.write(str(x))

map (prnt, range(input()))

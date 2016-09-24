# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
items=OrderedDict()
n=input()
for i in range(n):
    item_name=raw_input().split()
    net_price=item_name[-1]
    item_name=' '.join(item_name[:-1])
    if item_name in items.keys():
        net_price_new=items[item_name]
    else:
        net_price_new=0
    items[item_name]=int(net_price)+net_price_new
for key in items:    
    print key, items[key]

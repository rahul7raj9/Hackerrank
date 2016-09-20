# Enter your code here. Read input from STDIN. Print output to STDOUT
x=raw_input()
len_x=len(x)
alpha_list=[]
for i in range(len_x):
    if (x[i].lower()).isalpha():
        if x[i].lower() not in alpha_list:
            alpha_list.append(x[i].lower())
if len(alpha_list) == 26:
    print "pangram"
else:
    print "not pangram" 

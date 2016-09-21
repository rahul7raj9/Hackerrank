# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
marks=[]
name=[]
for i in range(n*2):
    if i%2 !=0 :
        marks.append(input())
    else:
        name.append(raw_input())

student=zip(name, marks)
marks=set(marks)
marks=sorted(list(marks))
sec_lowest = marks[1]
name_sec_lowest=[]
for i in range(n):
    if student[i][1]==sec_lowest:   
        name_sec_lowest.append(student[i][0])
name_sec_lowest=sorted(name_sec_lowest)
print '\n'.join(name_sec_lowest) 
    
    
    

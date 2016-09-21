# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division
n=input()
student=[]
for i in range(n):
    student.append(raw_input().split( " "))
name=raw_input()

total=[float(student[i][1])+float(student[i][2])+float(student[i][3]) for i in range(n) if student[i][0]==name]
print "{:.2f}".format(float(total[0])/3.0)



    
    

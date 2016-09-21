# Enter your code here. Read input from STDIN. Print output to STDOUT
x=[]
dim=[input() for x in range(3)]
N=input()
dim_x = [x for x in range(dim[0]+1)]
dim_y = [x for x in range(dim[1]+1)]
dim_z = [x for x in range(dim[2]+1)]
result=[]

result = [[i,j,k] for i in range(len(dim_x)) for j in range(len(dim_y)) for k in range(len(dim_z))  if dim_x[i]+dim_y[j]+dim_z[k] != N]
print result
              

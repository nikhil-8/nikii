x=[[1,4],
   [2,5]]
y=[[2,3],
   [5,6]]
result=[[0,0],
        [0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
for r in result:
    print(r)
    

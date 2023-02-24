X = [[3,9,2],[5,7,8],[0,9,7]]
Y = [[4,7,8],[1,3,4],[6,7,1]]
Result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)): 
    for j in range(len(X[0])):
        Result[i][j] = X[i][j] + Y[i][j]
print("Matrix Addition = :")
for AddedMAtrix in Result:
    print(AddedMAtrix)
print("\n")

X = [[1,2,3],[6,5,4],[7,8,9]]
Y = [[9,8,7],[4,5,6],[3,2,1]]
Result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)): 
    for j in range(len(Y[0])): 
        for k in range(len(Y)): 
            Result[i][j] += X[i][k] * Y[k][j] 
print("Matrix Multiplication =:")
for MultipliedMatrix in Result: 
    print(MultipliedMatrix,)


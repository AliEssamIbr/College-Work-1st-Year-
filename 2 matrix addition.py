A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[3,4,7],[13,9,4],[1,2,12]]
def Matrix_Addition(X,Y):
    Z = []
    for i in range(len(X)):
        V = []
        for j in range(len(X[i])):
            V.append(X[i][j] + Y[i][j])
        Z.append(V)
    return Z
print(Matrix_Addition(A,B))
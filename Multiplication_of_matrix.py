def multiply(A,B):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    '''for rows'''
    for i in range(len(A)):
        '''for columns'''
        for j in range(len(B[0])):
            '''for rows of matrix'''
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    for p in result:
        print(p)
    return 0

A = [[1,2,3],[6,7,4],[8,10,11]]
B = [[1,5,3],[2,6,5],[7,4,9]]

print("Result:")
multiply(A,B)



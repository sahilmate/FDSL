'''Write python program for to compute the following computation on matrix
A. Addition of two matrices
B. Subtraction of two matrices
C. Multiplication of two
D. Transpose of matrix'''
#Matrix Manupulation
print("****Matrix Manupulation****")
r1=int(input("Enter the no of rows:"))
c1=int(input("Enter the no of columns:"))
def m1():
    global m11
    m11=[]
    print("Enter the values in rowwise:")
    for i in range(r1):
        a=[]
        for j in range(c1):
            a.append(int(input()))
        m11.append(a)
    for i in range(r1):
        for j in range(c1):
            print(m11[i][j],end=" ")
        print()
m1()
print("Enter the values for 2nd matrix:")
r2=int(input("Enter the no of rows:"))
c2=int(input("Enter the no of columns:"))
def m2():
    global m22
    m22=[]
    print("Enter the values in rowwise:")
    for i in range(r2):
        b=[]
        for j in range(c2):
            b.append(int(input()))
        m22.append(b)
    for i in range(r2):
        for j in range(c2):
            print(m22[i][j],end=" ")
        print()
m2()
if (r1==r2) and (c1==c2):

    print("Addition of given matrix is:")
    output=[[0 for i in range (c2)] for j in range(r1)]
    for i in range(r1):
        for j in range(c2):
            output[i][j]=m11[i][j]+m22[i][j]
    for i in range(r1):
        for j in range(c2):
            print(output[i][j]," ", end=" ")
        print()
    print()
    print("Subtraction of given matrix is:")
    output=[[0 for i in range(c2)]for j in range(r1)]
    for i in range(r1):
        for j in range(c2):
            output[i][j]=m11[i][j]-m22[i][j]
    for i in range(r1):
        for j in range(c2):
            print(output[i][j]," ",end=" ")
        print()
    print()
else:
    print("Matrix cant be added or subtracted")
if (c1==r2):
    print("Multiplication of matrix")
    result=[[0 for i in range(c2)]for j in range(r1)]
    for i in range(len(m11)):
        for j in range(len(m22[0])):
            for k in range(len(m22)):
                result[i][j]+=m11[i][k]*m22[k][j]
    for r in result:
        print(r)
else:
    print("Matrix can't be multiplied")

print("Transpose of Matrix ONE-")

ans=[[0 for j in range(r1)]for i in range(c1)]
for i in range(c1):
    for j in range(r1):
        ans[i][j] = m11[j][i]
        print(ans[i][j]," ",end=" ")
    print() 
print()

'''
def input_matrix(rows,cols):
    matrix=[]
    for i in range (rows):
        row=[]
        for j in range (cols) :
            element = float(input(f"Enter the element at position ({i+1} , {j+1}):  "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element , end = " ")
        print()

print("Matrix A: ") 
rowsA = int(input("Enter the number of rows: "))
colsA = int(input("Enter the number of columns: "))
matrixA = input_matrix(rowsA,colsA)

print(" \n Matrix B: ")
rowsB=int(input(" Enter the number of rows: "))
colsB=int(input(" Enter the number of columns: "))
matrixB = input_matrix(rowsB, colsB)

print("Matrix A: ")
print_matrix(matrixA)

print("Matrix B: ")
print_matrix(matrixB)

print("\n The Addition of the matrices is:  ")
addition = [[matrixA[i][j]+ matrixB[i][j] for j in range(colsA)] for i in range(rowsA)]
print_matrix(addition)

print(" \n The Subtraction of the matrices is: ")
subtraction=[ [matrixA[i][j]-matrixB[i][j]for j in range(colsA)] for i in range(rowsA)]
print_matrix(subtraction)

print(" \n The Multiplication of the matrices is: ")
multiplication =[[sum([matrixA[i][k]*matrixB[k][j] for k in range(colsA)]) for j in range (colsB)] for i in range (rowsA)]
print_matrix(multiplication)



print("\n Copying matrix A to Matrix C to get transpose: ")
matrixC = [[0] * colsA for _ in range(rowsA)]

for i in range(rowsA):
    for j in range(colsA):
        matrixC[i][j] = matrixA[i][j]

print("\nMatrix C: ")
for row in matrixC:
    print(row)

result = matrixC    

                    
print(" \n The transpose of the matrix A is: ")
for i in range(len(matrixA)):
    for j in range (len(matrixA[0])):
        result[j][i] = matrixA[i][j]
for r in result:
    print(r) 
'''









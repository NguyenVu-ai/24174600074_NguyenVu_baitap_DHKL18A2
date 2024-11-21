#bài tập ma trận với số 
# nhân ma trận với 1 số 
matrix_a = [[1,1,2],
            [4,7,6],
            [7,9,9]]
n = 3
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] * n

# chia ma trận với 1 số 
        matrix_a[hang][cot] = matrix_a[hang][cot]/n
#cộng ma trận với một số 
        matrix_a[hang][cot] = matrix_a[hang][cot] + n
#trù ma trận với 1 số 
        matrix_a[hang][cot] = matrix_a[hang][cot] - n
        print(matrix_a)
# nhân hai ma trận 
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
B = [[2,3,4],
     [4,5,6]]
if len(A[0]) != len(B) :
    print("Loi , vui long nhap lai ma tran")
else : 
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
for i in range(len(A)): 
    for j in range(len(B[0])): 
        for k in range(len(B)): 
            C[i][j] += A[i][k] * B[k][j]
print("Phép nhân ma trận:")
for hang in C: 
    print(hang)
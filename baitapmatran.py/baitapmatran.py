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



    # Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
if n > 0 :
    # Tính tử số: Tích từ k = 2 đến n + 4
    numerator_product = 1
    for k in range(2, n + 5):
        numerator_product *= k

    # Tính mẫu số: 1 + tổng các giá trị 1 / (tích từ i = 1 đến k - 1)
    denominator_product = 1  # Bắt đầu với 1
    for k in range(2, n + 5):
        inner_product = 1
        for i in range(1, k):
            inner_product *= i
        denominator_product += 1 / inner_product

    # Tính giá trị của S
    S = numerator_product / denominator_product

    # In kết quả
    print(f"Giá trị của S là: {S}")
else:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")​11:31/-strong/-heart:>:o:-((:-h Xem trước khi gửiThả Files vào đây để xem lại trước khi gửi
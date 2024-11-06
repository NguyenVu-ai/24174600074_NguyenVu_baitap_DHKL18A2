n = int(input("Nhập số hàng cho Tam giác Pascal: "))
# Vẽ Tam giác Pascal
for i in range(n):
    print(" " * (n - i), end="")
    tong = 1
    for j in range(i + 1):
        print(tong, end=" ")
        tong = tong * (i - j) // (j + 1)

    print()  
    
#vẽ tam giác floyd
n = int(input("Nhập số hàng cho Tam giác Floyd: "))
tong = 1  
for i in range(1, n + 1):
    for j in range(i):
        print(tong, end=" ")
        tong =tong+ 1  
    print()  
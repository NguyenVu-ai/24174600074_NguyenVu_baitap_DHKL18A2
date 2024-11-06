a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
nho_nhat = min(abs(a), abs(b))  
ucln = 1
for i in range(nho_nhat, 0, -1):
    if a % i == 0 and b % i == 0:
        ucln = i
        break
print(f"Ước chung lớn nhất của {a} và {b} là: {ucln}")
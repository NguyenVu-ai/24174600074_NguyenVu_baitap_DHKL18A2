a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
ucln = 1
nho_nhat = min(abs(a), abs(b))  

for i in range(nho_nhat, 0, -1):
    if a % i == 0 and b % i == 0:
        ucln = i
        break

bcnn = abs(a * b) // ucln

print(f"Bội chung nhỏ nhất của {a} và {b} là {bcnn}")
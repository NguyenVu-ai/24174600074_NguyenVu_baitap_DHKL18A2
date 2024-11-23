n = int(input("nhập giá trị n :"))
if n > 2 : 
  tong = 0
  for k in range(4,n+3) :
    def tinh_tich_mau_so(k):
    tich = 1
    for i in range(1, k+1):
        tich *= (i + 2)
    return tich

def tinh_tong_S(n):
    tong = 0
    for k in range(4, n+3):
        tu_so = k
        mau_so = 2 * tinh_tich_mau_so(k)
        tong += tu_so / mau_so
    return tong

# Nhập vào số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))

# Tính tổng S
S = tinh_tong_S(n)

# Xuất ra màn hình tổng S
print("Tổng S là:", S)
# Nhập vào số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))

# Khởi tạo tổng S
S = 0

# Tính tổng S theo công thức
for k in range(4, n + 3):
    tu_so = k
    mau_so = 2
    for i in range(1, k + 1):
        mau_so *= (i + 2)
    S += tu_so / mau_so

# Xuất ra màn hình tổng S
print("Tổng S là:", S)
# Nhập vào số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))

# Khởi tạo tổng S
S = 0

# Tính tổng S theo công thức
for k in range(4, n + 3):
    tu_so = k
    mau_so = 2
    for i in range(1, k + 1):
        mau_so *= (i + 2)
    S += tu_so / mau_so

# Xuất ra màn hình tổng S
print("Tổng S là:", S)
# Nhập vào số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))

# Khởi tạo tổng S
S = 0

# Tính tổng S theo công thức
for k in range(4, n + 3):
    tu_so = k
    mau_so = 2
    for i in range(1, k + 1):
        mau_so *= (i + 2)
    S += tu_so / mau_so

# Xuất ra màn hình tổng S
print("Tổng S là:", S)

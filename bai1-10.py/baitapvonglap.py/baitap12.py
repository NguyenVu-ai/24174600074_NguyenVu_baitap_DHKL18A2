tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))
if mau_so == 0:
    print("Mẫu số phải khác 0.")
else:
    
    nho_nhat = min(abs(tu_so), abs(mau_so))  
    ucln = 1
    for i in range(nho_nhat, 0, -1):
        if tu_so % i == 0 and mau_so % i == 0:
            ucln = i
            break

    tu_so = tu_so // ucln
    mau_so = mau_so // ucln

    print(f"Phân số tối giản là: {tu_so}/{mau_so}")
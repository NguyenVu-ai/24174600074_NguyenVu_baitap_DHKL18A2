a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
if a >= b and a >= c:
    số_lớn_nhất = a
elif b >= a and b >= c:
    số_lớn_nhất = b
else:
    số_lớn_nhất = c

print(f"Số lớn nhất là: {số_lớn_nhất}")
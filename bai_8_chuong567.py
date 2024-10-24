import math
x = float(input("nhap gia tri phuong trinh x: ")) 
if x > 0 and x != 1 :
    print("giá trị thỏa mãn")
else:
    print("giá trị không thỏa mãn ") 
logx4 = math.log(x,4)
log2x = math.log(2,x)
f_x = logx4 + log2x
print(f"Gia tri can tim x:{f_x:.2f}")  
#bai3
while True:
    n = input("Nhập vào số nguyên dương n: ")
    if not n.isdigit() or int(n) <= 0:
        print("Yêu cầu nhập lại số nguyên dương!!")
    else:
        n = int(n)
        break

A = [i for i in range(n) if i % 2 != 0]
B = [i for i in range(n) if i % 2 == 0]
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] < A[j]:
            A[i], A[j] = A[j], A[i]

for i in range(len(B)):
    for j in range(i + 1, len(B)):
        if B[i] < B[j]:
            B[i], B[j] = B[j], B[i]

print(f"Danh sách A gồm các số lẻ nhỏ hơn {n}: {A}")
print(f"Danh sách B gồm các số chẵn nhỏ hơn {n}: {B}")


#2 
ds_so = []
while True:
    n = input("Nhap vao so phan tu n trong danh sach: ")
    if n.isdigit() == False:
       print("Yeu cau nhap lai so nguyen duong!!")
        
    else:
         n = int(n)
         break

for i in range(n):
    while True:
        so = input(f"Nhap gia tri so thu {i + 1}: ")
        if so.count('-') == 1 and so.replace('-','').isdigit():
            so = float(so)
            break
        else:
            print("Yeu cau nhap vao so!!")
            
    ds_so.append(so)

tong = sum(ds_so)
print(f"Tong cac so vua nhap: {tong}")
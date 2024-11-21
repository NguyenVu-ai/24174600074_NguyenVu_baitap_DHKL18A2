n = int(input("Nhập vào một số: "))
if n > 1:
    u = 2
    print("Các thừa số nguyên tố là:", end=" ")

    while n > 1:
        if n % u == 0:
            print(u, end=" ")
            n = n // u  
        else:
            u=u+ 1  
else:
    print("Vui lòng nhập một số lớn hơn 1.")

n = int(input("Nhập một số nguyên: "))
if n < 0:
    print(f"{n} không phải là số chính phương.")
else:
    is_perfect_square = True
    for i in range(0, n + 1):
        if i * i == n:  
            is_perfect_square = True
            break  

    if is_perfect_square:
        print(f"{n} là số chính phương.")
    else:
        print(f"{n} không phải là số chính phương.")
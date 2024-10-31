#bai 1
year = int(input("nhập năm: "))

if year %4 ==0  and year %100 !=0 or year %400 ==0:
    print(" là năm nhuận")
else:
    print("không phải năm nhuận")
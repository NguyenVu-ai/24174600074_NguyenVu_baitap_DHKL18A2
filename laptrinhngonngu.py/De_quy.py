# đệ quy - recursion - tái lặp 
#ví dụ : dãy fibonacci
#số tiếp theo = số hiện tại + số trước đó 
#f(n)=f(n-1)+f(n-2)=> đệ quy trên toán học 
#def f():
 #   f()
 # hoạt động không khác gì vòng lặp

#f()
#import sys
#xem giới hạn 
#sys.getrecursionlimit()
#tăng giới hạn 
#sys.setrecursionlimit()   

# Yêu cầu khi viết đệ quy 
# tham số của hàm lệ quy cần thay đổi sau mỗi lần lặp
# cần có điểm dưng cho lặp đệ quy 

# bài tập về dãy fibonacci
# in ra n số finonacci
n = int(input("Nhập vào số n :"))
def fibonacci(n):
    if n == 2 :  
       return 1 
    elif n == 1 :
        return 0 
    elif n == 0 :
         return 0
    else :
        return  fibonacci(n-1) + fibonacci(n-2)
for i in range(n) : 
    print(fibonacci(i), end=" ")   

# hàm đếm countdowm
 



# áp dụng đệ quy vào giải thuật
# giải thuật sắp xếp trộn (merge sort)
# giải thuật sắp xếp nhanh ( quick sort)
#giải thuật backtracking
#giải thuật nhánh cây lựa chọn (decisipn tree)

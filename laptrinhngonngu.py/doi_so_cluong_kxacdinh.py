# đóng gói bộ tham số 
def f(*args):
    print(args)
    print(type(args), len(args))
    for x in args :
        print(x)

f(1, 2, 3)
#đóng gói từ điển tham số 
def f(**kwanrgs) : 
    print(kwanrgs)
    print(type(kwanrgs))
    for key , val in kwanrgs.items() :
        print(key , '->' , val)

f()

#ví dụ 
def tinh_trung_binh(*args):
    # kiểm tra giá trị trong args
    tong = 0 
    for i in args : 
        tong = tong + i
    trung_binh = tong/len(args)
    return trung_binh

tinh_trung_binh(1,2,3)     

list_ttsv = []
def nhap_thong_tin(**kwargs) :
    #kiểm tra giá trị trong kwargs

nhap_thong_tin(ten="Vu", tuoi="18" , diem_tb="9.9)
               

#Docstring
def tinh_tong_hai_so(a: int,b: float):
    """
    Hàm tính tổng
    Trả về tổng
    """
    return a + b 

tinh_tong_hai_so(4,5)


#Function annotations


 
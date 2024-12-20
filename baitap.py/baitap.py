danh_sach_hang_hoa = []


def them_mat_hang():
    try:
        ma_hang = input("Nhập mã hàng: ")
        ten_hang = input("Nhập tên hàng: ")
        don_vi_tinh = input("Nhập đơn vị tính: ")
        don_gia = float(input("Nhập đơn giá: "))
        so_luong = int(input("Nhập số lượng: "))
        thanh_tien = don_gia * so_luong
        vat = thanh_tien * 0.1

        mat_hang = {
            "ma_hang": ma_hang,
            "ten_hang": ten_hang,
            "don_vi_tinh": don_vi_tinh,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "thanh_tien": thanh_tien,
            "vat": vat,
        }
        danh_sach_hang_hoa.append(mat_hang)
        print("Thêm mặt hàng thành công.")
    except ValueError as i:
        print(f"Lỗi nhập liệu: {i}")


def hien_thi_danh_sach():
    if not danh_sach_hang_hoa:
        print("Danh sách mặt hàng trống.")
        return

    print("\nDanh sách mặt hàng:")
    for mat_hang in danh_sach_hang_hoa:
        print(f"Mã hàng: {mat_hang['ma_hang']}, Tên hàng: {mat_hang['ten_hang']}, "
            f"Đơn vị tính: {mat_hang['don_vi_tinh']}, Đơn giá: {mat_hang['don_gia']}, "
            f"Số lượng: {mat_hang['so_luong']}, Thành tiền: {mat_hang['thanh_tien']}, "
            f"VAT: {mat_hang['vat']}")

def xoa_mat_hang():
    try:
        ma_hang = input("Nhập mã hàng cần xóa: ")
        mat_hang = tim_kiem_theo_ma(ma_hang)
        if mat_hang:
            danh_sach_hang_hoa.remove(mat_hang)
            print(f"Đã xóa mặt hàng: {mat_hang['ten_hang']}")
        else:
            raise Exception("Không tìm thấy mặt hàng với mã đã nhập.")
    except Exception as e:
        print(e)
def sap_xep_theo_ten():
    danh_sach_hang_hoa.sort(key=lambda x: x["ten_hang"])
    print("Danh sách đã được sắp xếp theo tên.")



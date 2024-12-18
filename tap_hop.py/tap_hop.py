tap_hop_a = {"a","b","c"}
tap_hop_b = {"a" , "b", 3 ,2 ,"c"}
tap_hop_c ={1,2,3,4}
# hợp các phần tử 
tong = tap_hop_a.union(tap_hop_b)
tong = tap_hop_a.union(tap_hop_c).union(tap_hop_b)
 #giao các phần tử 
giao = tap_hop_a.intersection(tap_hop_b)
giao = tap_hop_b.intersection(tap_hop_c).intersection(tap_hop_a)
giao = tap_hop_a & tap_hop_b & tap_hop_c
# phép lấy phần tử trong một tập hợp mà không có trong các tập họp còn lại 
tap_hop_khac = tap_hop_a.difference(tap_hop_b)
tap_hop_khac = tap_hop_a.difference(tap_hop_b).difference(tap_hop_c)
tap_hop_khac = tap_hop_a - tap_hop_b - tap_hop_c
# phép lấy hợp của các phần cả trong tập họp này mà k có trong tập hợp kia 
tap_khac_giao = tap_hop_a.symmetric_difference(tap_hop_b)
tap_khac_giao = tap_hop_a.symmetric_difference(tap_hop_b).symmetric_difference(tap_hop_c)
tap_khac_giao = tap_hop_a ^ tap_hop_b ^ tap_hop_c
# chỉnh sửa tập họp 
tap_hop_a = {1, 2, 3}
#thêm phần tử vào a 
tap_hop_a.update([4,5,6])# tương tự việc họp hai tập hợp 
tap_hop_a.add(9)
#a=1
#b=2
#a+=b
#a=a+b
tap_hop_a = tap_hop_a | tap_hop_b
tap_hop_a |= tap_hop_b
 

 
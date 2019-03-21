n = int(input("nhap vao so dien : "))
S = 0
if n < 51:
    S = 15000 * n
if 50 < n < 201:
    S = 16500 * n
if n > 200:
    S = 20000 * n
print("Tong so tien dien phai tra la :", S)

'''
nhap vao so dien : 60
Tong so tien dien phai tra la : 990000
'''

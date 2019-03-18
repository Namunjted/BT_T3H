n = int(input("nhap vao so phan tu cua list : "))
a = [2 for _ in range(n)]
print(a)

'''
nhap vao so phan tu cua list : 8
[2, 2, 2, 2, 2, 2, 2, 2]
'''
#------------------------------------


b = [number for number in range(0, 100) if number % 3 == 0 or number % 5 == 0]
print(b)

'''
[0, 3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50, 51, 54, 55, 57, 60, 63, 65, 66, 69, 70, 72, 75, 78, 80, 81, 84, 85, 87, 90, 93, 95, 96, 99]
'''


#------------------------------------


c = [str(i) * 6 for i in range(21) if i % 2 != 0]
print(c)

'''
['111111', '333333', '555555', '777777', '999999', '111111111111',
'131313131313', '151515151515', '171717171717', '191919191919']
'''


# #------------------------------------#


from random import randrange
N = int(input("nhap so phan tu cua list : "))
d = [randrange(N) for _ in range(N)]
print(d)

'''
nhap so phan tu cua list : 7
[1, 0, 3, 1, 2, 3, 3]
'''

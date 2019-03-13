n = int(input("nhap vao so phan tu cua list : "))
a = [2 for _ in range(n)]
print(a)

'''
nhap vao so phan tu cua list : 8
[2, 2, 2, 2, 2, 2, 2, 2]
'''
#------------------------------------


b = [number for number in range(0, 100) if number % 3 == 0 and number % 5 == 0]
print(b)

'''
[0, 15, 30, 45, 60, 75, 90]
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

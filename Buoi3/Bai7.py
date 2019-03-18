numbers = [1, 6, 7, 8, 1, 3, 4, 6, 3, 6, 7]
sum_ = 0
tich_ = 1
for number in numbers:
    sum_ += number
    tich_ = number * tich_
print(sum_,tich_)

'''
52 3048192
'''

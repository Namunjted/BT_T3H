from random import randint
numbers = [randint(0, 10) for _ in range(100)]
result = []
lenght_tuples = int(input("nhap vao do dai tupper muon khoi tao : "))
count = 0
print("numbers = ", numbers)

while count < 100:
    result.append(tuple(numbers[count:count + lenght_tuples]))
    count += lenght_tuples
print("result = ", result)

'''
nhap vao do dai tupper muon khoi tao : 6
numbers =  [1, 6, 4, 1, 10, 3, 1, 4, 8, 1, 3, 0, 8, 9, 10, 4, 2, 8, 1, 4, 0, 2,
6, 8, 7, 2, 6, 9, 2, 7, 10, 8, 10, 4, 4, 10, 4, 10, 1, 8, 6, 6, 10, 1, 2, 0,
6, 9, 9, 0, 7, 5, 9, 3, 4, 10, 8, 0, 2, 0, 8, 8, 10, 4, 0, 0, 10, 4, 7, 4, 6,
 8,6, 7, 10, 10, 5, 1, 7, 0, 10, 4, 4, 2, 10, 0, 4, 7, 2, 1, 5, 1, 8, 0, 9, 8,
  9,8,3, 8]
result =  [(1, 6, 4, 1, 10, 3), (1, 4, 8, 1, 3, 0), (8, 9, 10, 4, 2, 8), (1, 4,
0, 2, 6, 8), (7, 2, 6, 9, 2, 7), (10, 8, 10, 4, 4, 10), (4, 10, 1, 8, 6, 6),
(10, 1, 2, 0, 6, 9), (9, 0, 7, 5, 9, 3), (4, 10, 8, 0, 2, 0), (8, 8, 10, 4, 0,
0),(10, 4, 7, 4, 6, 8), (6, 7, 10, 10, 5, 1), (7, 0, 10, 4, 4, 2), (10, 0, 4, 7
,2, 1),(5, 1, 8, 0, 9, 8), (9, 8, 3, 8)]

'''

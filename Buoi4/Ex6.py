a = 1
b = 2
fibonacy = [1]
while b < 1000:
    a, b = b, a + b
    fibonacy.append(a)
print(fibonacy)

'''
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

'''

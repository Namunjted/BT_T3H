file = open("Ex1.txt")
f = tuple(file)
file.close()
print(f[-1:-10:-1])

'''
('FizzBuzz\n', '2999999\n', '2999998\n', 'Buzz\n', '2999996\n', 'Fizz\n',
'Buzz\n', '2999993\n', '2999992\n')
'''

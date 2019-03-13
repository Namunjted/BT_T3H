numbers = [1.5, 6.7, 7, 8.9, 1, 3, 4, 6, 3, 6, 7, 0.1]

max_ = numbers[0]
min_ = numbers[0]

for number in numbers:
    if number > max_:
        max_ = number
for number in numbers:
    if number < min_:
        min_ = number
print("Max: ", max_, "\nMin: ", min_)


'''
Max:  8.9 
Min:  0.1
'''

from string import ascii_lowercase

names = ['python', 'patience', 'documents', 'students',
         'homework', 'practice', 'success', 'english',
         'university', 'congratulation']

result = []
for name in names:
    sum_ = 0
    for char in name:
        value = ascii_lowercase.index(char) + 1
        sum_ = sum_ + value
    result.append([name, sum_])

print(result)

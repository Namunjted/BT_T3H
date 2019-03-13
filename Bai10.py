import string

words = ['python', 'patience', 'documents', 'students', 'homework',
         'practice', 'success', 'english', 'university', 'congratulation']
alphabets = string.ascii_lowercase

sum_ = 0
result = []

for word in words:
    for text in word:
        if text in alphabets:
            sum_ += alphabets.index(text) + 1
    result.append(sum_)
    sum_ = 0

print(result)


'''
[98, 73, 114, 122, 108, 75, 89, 74, 162, 170]
'''

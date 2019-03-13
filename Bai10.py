import string

samples = ['python', 'patience', 'documents', 'students', 'homework',
           'practice', 'success', 'english', 'university', 'congratulation']
template = string.ascii_lowercase

Sum = 0
resuilt = []

for sample in samples:
    for x in sample:
        if x in template:
            Sum += template.index(x) + 1
    resuilt.append(Sum)
    Sum = 0

print(resuilt)


'''
[98, 73, 114, 122, 108, 75, 89, 74, 162, 170]
'''
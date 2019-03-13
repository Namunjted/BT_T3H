sample = [[1, 2, 3], [4, 5], [6, [7, 8], 9], [10]]
result	= []
while sample:
    a = sample.pop()
    if isinstance(a, list):
        sample = sample + a
    else:
    	result.append(a)
result.reverse()
print(result)
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

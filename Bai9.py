sample = [[1, 2, 3], [4, 5], [6, [7, 8], 9], [10]]
template = []
for x in sample:
    for y in x:
        if type(y) == list:
            for z in y:
            	template.append(z)
        else:
        	template.append(y)

print(template)

'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
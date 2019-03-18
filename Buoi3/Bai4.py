result = []
for a in range(1,50):
    for b in range(1,50):
        for c in range(1,50):
            if  c * a + b == 10 * c:
                result.append([a, b, c])
print(len(result))


'''
136
'''

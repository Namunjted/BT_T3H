L1 = [1, 2, 3, 4, 5, 6]
L2 = [3, 4, 5, 6, 7, 8, 9, 10]

# co trong ca L1 va L2
print(set(L1) & set(L2))
print(set(L1).intersection(set(L2)))

# chi co trong L1
print(set(L1).difference(set(L2)))
print(set(L1) - set(L2))

# chi co trong L2
print(set(L2).difference(set(L1)))
print(set(L2) - set(L1))

# khong co trong L1 hoac l2

print(set(L1).symmetric_difference(L2))
print(set(L2) ^ set(L1))

'''
{3, 4, 5, 6}
{3, 4, 5, 6}
{1, 2}
{1, 2}
{8, 9, 10, 7}
{8, 9, 10, 7}
{1, 2, 7, 8, 9, 10}
{1, 2, 7, 8, 9, 10}
'''
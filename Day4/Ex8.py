
samples = ["python", None, "cpython", True, 1, 1 + 1j,
           False, [100, 200, 300], 99.99, (31, "January")]
for sample in samples:
    if isinstance(sample, (int, complex, float)) and sample is not True and sample is not False:
        print(sample)

'''
1
(1+1j)
99.99
'''

# a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66
sum_ = 0
numbers = range(1, 10)
for a in numbers:
    for b in numbers:
        for c in numbers:
            for d in numbers:
                for e in numbers:
                    for f in numbers:
                        for g in numbers:
                            for h in numbers:
                                for i in numbers:
                                    if a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 == 66:
                                        sum_ += 1
print(sum_)

'''
442232
'''

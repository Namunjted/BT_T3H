a = [1.5, 6.7, 7, 8.9, 1, 3, 4, 6, 3, 6, 7, 0.1]

Max = a[0]
Min = a[0]

for number_max in a:
    if number_max > Max:
        Max = number_max
for number_min in a:
    if number_min < Min:
        Min = number_min
print("Max: " ,Max , "\nMin: ", Min)


'''
Max:  8.9 
Min:  0.1
'''
f = open("Ex1.txt", "w")

lines = range(1,3000001)

for line in lines:
    if line % 15 == 0:
        f.write('FizzBuzz\n')
    elif line % 5 == 0:
        f.write('Fizz\n')
    elif line % 3 == 0:
        f.write('Buzz\n')
    else:
        f.write(str(line) + '\n')
f.close()


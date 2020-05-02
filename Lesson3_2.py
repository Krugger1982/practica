import random
summ = 0
for i in range(2):
    x = str(random.randint(1, 10)) + '.txt'
    print(x)
    with open(x, 'tr') as a:
        s = a.readline()
        while s!= '':
            summ += int(s.rstrip())
            s = a.readline()
        a.close()
print(summ)

import random
summ = 0
for i in range(2):
    x = str(random.randint(1, 10)) + '.txt'
    print(x)
    with open(x, 'tr') as a:
        try:
            s = a.readline()
            while s!= '':
                summ += int(s.rstrip())
                s = a.readline()
        except TypeError:
            print ('В файле ', x, ' ошибка данных')
        finally:
            a.close()
print(summ)

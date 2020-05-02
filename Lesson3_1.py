import random
for i in range(10):
    x = str(i+1) + '.txt'
    with open(x, 'tw', encoding='utf-8') as a:
        for j in range(3):
            a.write(str(random.randint(1, 100000))+'\n')
        a.close()

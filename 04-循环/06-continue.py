i = 1
while i <= 5:
    if i == 3:
        print('发现虫子不吃了')
        i += 1
        continue
    print('吃第%d个苹果' % i)
    i += 1

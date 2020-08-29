# 重复打印9⾏表达式
i = 1
while i <= 9:
    # 打印一行里面的表达式 a * b = a*b
    j = 1
    while j <= i:
        print('%d*%d=%d' % (j, i, i+j), end='\t')
        j += 1
    print()
    i += 1
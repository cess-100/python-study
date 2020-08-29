# 重复打印5行星星
i = 0
while i < 5:
    # 一行星星的打印
    j = 0
    while j < 5:
        # 一行内的星星不能换行，取消print默认结束符\n
        print('*', end='')
        j += 1
    # 每行结束要换行，这里借助一个空的print，利利用print默认结束符换⾏行
    print()
    i += 1

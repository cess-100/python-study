# range(start, end, step)
# 生成从start到end的数字，步长为 step，供for循环使用
# 不包含end，start省略默认0，step省略默认1

# 1 2 3 4 5 6 7 8 9
for i in range(1, 10, 1):
    print(i, end=' ')
print()

# 1 3 5 7 9
for i in range(1, 10, 2):
    print(i, end=' ')
print()

# 0 1 2 3 4 5 6 7 8 9
for i in range(10):
    print(i, end=' ')

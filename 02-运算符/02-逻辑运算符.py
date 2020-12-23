a = 0
b = 1
c = 2

print((a < b) and (c > b))  # True
print((a > b) and (c > b))  # False

print(a < b or c > b)  # True
print(a > b or c > b)  # True

print(not False)
print(not c > b)


# and运算符，只要有⼀个值为0，则结果为0，否则结果为最后⼀个非0数字
print(a and b)  # 0
print(b and a)  # 0
print(a and c)  # 0
print(c and a)  # 0
print(b and c)  # 2
print(c and b)  # 1

# or运算符，只有所有值为0结果才为0，否则结果为第⼀个非0数字
print(a or b)  # 1
print(a or c)  # 2
print(b or c)  # 1

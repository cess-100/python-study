# 一个函数里面又调用了另外一个函数

def testB():
    print('---- testB start----')
    print('这⾥里里是testB函数执⾏行行的代码...(省略略)...')
    print('---- testB end----')

def testA():
    print('---- testA start----')
    testB()
    print('---- testA end----')

testA()


# 打印图形
# 打印一条横线
def print_line():
    print('-' * 20)

# print_line()

# 打印多条横线
def print_lines(num):
    for i in range(num):
        print_line()

print_lines(5)


# 函数计算
# 求三个数之和
def sum(a, b, c):
    return a + b + c

# result = sum(1, 2, 3)
# print(result)

# 求三个数平均值
def average(a, b, c):
    sumResult = sum(a, b, c)
    return sumResult / 3

result = average(1, 2 , 3)
print(result)
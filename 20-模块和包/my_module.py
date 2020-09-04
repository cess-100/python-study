def testA(a, b):
    print(a + b)


# 测试信息
# __name__ 是系统变量，模块标识符
# 如果是自身模块是__main__ ，否则是当前模块的名字
# __main__ 表示只使用在自身模块内部
if __name__ == '__main__':
    testA(1, 1)

print(__name__)

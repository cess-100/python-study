"""
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
"""


try:
    f = open('test.txt', 'r')
except:
    f = open('test.txt', 'w')


"""
try:
    可能发生错误的代码
except 异常类型:
    如果捕获到该异常类型执行的代码
"""

try:
    # print(1/0) 捕获不到还是报错
    print(num)
except NameError:
    print('有错误')


# 捕获多个异常
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('有错误')

try:
    print(1/0)
except NameError:
    print('有错误1')
except ZeroDivisionError:
    print('有错误2')


# 捕获异常信息
try:
    print(num)
except (NameError, ZeroDivisionError) as e:
    print(e)

# 捕获所有异常
# Exception是所有程序异常类的父类
try:
    print(1/0)
except Exception as e:
    print(e)

"""
如果需要返回结果给用户需要使用函数返回值
return返回结果给函数调用的地方
"""

# 定义一个函数，返回 烟
def buy():
    return '烟'
    print('OK')

goods = buy()
print(goods)

"""
return作用：
    1.负责函数返回值
    2.退出当前函数，导致函数体内return下方的所有代码不执行
"""

# 计算任意两个数字的加法
def sum(a, b):
    return a + b

result = sum(1, 2)
print(result)

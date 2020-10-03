"""
如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化
语法：
    lambda 参数列列表 ： 表达式
注意：
    lambda表达式的参数可有可无，函数的参数在lambda表达式中完全适用
    lambda函数能接收任何数量的参数但只能返回一个表达式的值
"""


# -----------
# 函数
def fn1():
    return 100


print(fn1)  # <function fn1 at 0x0000023793A2C268>
print(fn1())

# lambda表达式
fn2 = lambda: 200
print(fn2)  # <function <lambda> at 0x000002105579FA60>
print(fn2())


# ----------
# 计算a + b
def add(a, b):
    return a + b


result = add(1, 2)
print(result)


print((lambda a, b: a + b)(1, 2))

"""
把函数作为参数传⼊，这样的函数称为高阶函数，
高阶函数是函数式编程的体现
函数式编程就是指这种高度抽象的编程范式
"""

# abs()
print(abs(-10))

# round()
print(round(1.2))
print(round(1.9))


# 需求：一个函数完成计算任意两个数字的绝对值之和
# 普通方式
def add_num(a, b):
    return abs(a) + abs(b)

result = add_num(-1, 2)
print(result)


# 高阶函数
def add_num2(a, b, f):
    return f(a) + f(b)

result2 = add_num2(-1, 2, abs)
print(result2)

result3 = add_num2(-1, 2, round)
print(result3)


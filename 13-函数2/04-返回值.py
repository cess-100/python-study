# 只执行第⼀个return，原因是return退出当前函数，
# 导致return下方代码不执行
def return_num():
    return 1
    return 2


result = return_num()
print(result)  # 1


######################
def return_num2():
    return 1, 2


result = return_num2()
print(result)  # (1, 2)

"""
注意：
    1. return a, b写法，返回多个数据的时候，默认是元组类型
    2. return后⾯面可以连接列表、元组或字典，以返回多个值
"""


def return_num3():
    return [100, 200]


result = return_num3()
print(result)  # [100, 200]

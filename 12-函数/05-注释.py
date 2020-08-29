help(len) # help函数作用，查看函数的说明文档


# 定义函数的说明文档

# def 函数名(参数):
#     """说明文档的位置"""
#     代码
#     ...

def sum(a, b):
    """ 求和函数 """
    return a + b

help(sum)


# 函数说明文档的高级使用
def sum2(a, b):
    """
    求和函数
    :param a:参数1
    :param b:参数2
    :return:返回值
    """
    return a + b

help(sum2)

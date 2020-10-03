"""
递归的特点
    函数内部自己调用自己
    必须有出口
"""


# 回顾返回值
def return_num():
    return 100


result = return_num()
print(result)


# 计算1到n的数字累加和
def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n - 1)


sum = sum_numbers(3)
print(sum)

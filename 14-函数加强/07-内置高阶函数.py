import functools

# map(func, lst)
# 将传⼊的函数变量func作用到lst变量的每个元素中，
# 并将结果组成新的列表(Python2)/迭代器(Python3)返回

# 计算list1 序列中各个数字的2次⽅
list1 = [1, 2, 3, 4, 5]

def func1(x):
    return x ** 2

result = map(func1, list1)

print(result) # <map object at 0x00000173F6E97550>
print(list(result)) # [1, 4, 9, 16, 25]


# reduce(func(x,y)，lst)
# 其中func必须有两个参数
# 每次func计算的结果继续和序列的下一个元素做累计计算

# 计算list1 序列列中各个数字的累加和

list2  = [1, 2, 3, 4, 5]

def func2(a, b):
    return a + b

result = functools.reduce(func2, list2)
print(result) # 15


# filter(func, lst)
# 函数用于过滤序列, 过滤掉不符合条件的元素, 返回⼀个filter对象
# 如果要转换为列表,可以使⽤用 list() 来转换

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func3(x):
    return x % 2 == 0

result = filter(func3, list3)
print(result) # <filter object at 0x00000227F0DB9630>
print(list(result)) # [2, 4, 6, 8, 10]

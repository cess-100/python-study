# enumerate(可遍历对象, start=0)
# 返回结果是元组
# 元组第一个数据是原迭代对象的下表
# 第二个数据是原迭代对象的数据
# start参数⽤用来设置遍历数据的下标的起始值，默认为0

list1 = ['a', 'b', 'c', 'd', 'e']

# (0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e')
for i in enumerate(list1):
    print(i, end=' ')
print()

# (1, 'a') (2, 'b') (3, 'c') (4, 'd') (5, 'e')
for i in enumerate(list1, start=1):
    print(i, end=' ')
print()

for index, value in enumerate(list1, start=1):
    print("%d, %s" % (index, value))

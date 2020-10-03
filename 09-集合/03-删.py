s1 = {10, 20, 30, 40, 50}
print(s1)  # {40, 10, 50, 20, 30}


# remove() 删除集合中的指定数据，如果数据不存在则报错
s1.remove(10)
print(s1)  # {40, 50, 20, 30}
# s1.remove(10) KeyError: 10


# discard() 删除集合中的指定数据，如果数据不存在也不会报错
s1.discard(20)
print(s1)  # {40, 50, 30}
s1.discard(20)  # 不报错


# pop() 随机删除集合中的某个数据，并返回这个数据
del_num = s1.pop()
print(del_num)  # 40
print(s1)  # {50, 30}

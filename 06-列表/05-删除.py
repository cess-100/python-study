name_list = ['Tom', 'Lily', 'Rose', 'lucy']

# 1.del -- 删除列表 或 指定下表的数据
# del 列表名 或 del(列表名)
del name_list
# print(name_list)

name_list = ['Tom', 'Lily', 'Rose', 'lucy']
del name_list[1]
print(name_list) # ['Tom', 'Rose', 'lucy']


# 2.pop() -- 删除指定下标的数据，返回这个数据
# 如果不指定下表默认删除最后一个
name_list = ['Tom', 'Lily', 'Rose', 'lucy']

del_name = name_list.pop(0)
print(name_list) # ['Lily', 'Rose', 'lucy']
print(del_name) # Tom

del_name = name_list.pop()
print(name_list) # ['Lily', 'Rose']
print(del_name) # lucy


# 3.remove() -- 删除指定数据
name_list = ['Tom', 'Lily', 'Rose', 'lucy']
name_list.remove('Rose')
print(name_list) # ['Tom', 'Lily', 'lucy']

# 3.clear() -- 清空列表
name_list = ['Tom', 'Lily', 'Rose', 'lucy']
name_list.clear()
print(name_list) # []
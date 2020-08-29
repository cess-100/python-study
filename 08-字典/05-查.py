dict1 = {'name':'tom', 'age':20, 'gender':'男'}

# 如果当前查找的key存在，则返回对应的值；否则则报错
print(dict1['name']) # tom
# print(dict1['id']) # 报错 KeyError: 'id'

# 函数
# get() 不存在则返回默认值
# 字典序列列.get(key, 默认值)
print(dict1.get('name')) # tom
print(dict1.get('id')) # None
print(type(dict1.get('id'))) # <class 'NoneType'>
print(dict1.get('id', 110)) # 110

# keys() 查找字典中所有的key，返回可迭代对象
print(dict1.keys()) # dict_keys(['name', 'age', 'gender'])

# values() 查找字典中所有的value，返回可迭代对象
print(dict1.values()) # dict_values(['tom', 20, '男'])

# items() 查找字典中所有的键值对，返回可迭代对象，数据是元组
print(dict1.items()) # dict_items([('name', 'tom'), ('age', 20), ('gender', '男')])
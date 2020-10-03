name_list = ['tom', 'lily', 'rose']

# 1.index() 找不到报错
print(name_list.index('tom'))  # 0
print(name_list.index('lily', 0, 2))  # 1
# print(name_list.index('toms')) # 报错

# 2.count()
print(name_list.count('tom'))  # 1
print(name_list.count('ands'))  # 0

# 3.len() 访问列表长度，即列表中数据个数
print(len(name_list))  # 3

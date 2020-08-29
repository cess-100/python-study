name_list = ['tom', 'lily']
# 列表数据可改的 -- 列表可变类型

# 1.append(数据)
# append函数追加数据的时候如果数据是一个序列，追加整个序列到列表的结尾
name_list.append('big')
print(name_list) # ['tom', 'lily', 'big']
name_list.append(['xiaoming', 'xiaohong'])
print(name_list) # ['tom', 'lily', 'big', ['xiaoming', 'xiaohong']]


name_list = ['tom', 'lily']
# 2.extend(数据)
# append函数追加数据的时候如果数据是一个序列，将序列拆开追加到列表的结尾
name_list.extend('big')
print(name_list) # ['tom', 'lily', 'b', 'i', 'g']
name_list.extend(['xiaoming', 'xiaohong'])
print(name_list) # ['tom', 'lily', 'b', 'i', 'g', 'xiaoming', 'xiaohong']


name_list = ['tom', 'lily']
# 3.incert(位置下表, 数据)
name_list.insert(1, 'aaa')
print(name_list) # ['tom', 'aaa', 'lily']

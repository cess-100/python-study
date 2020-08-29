tuple1 = ('a', 'b', 'c', 'd', 'e')
list1 = [10, 20, 30, 40, 50, 20]
set1 = {100, 200, 300, 400, 500}

# tuple() 将序列转换为元组
print(tuple(list1)) # (10, 20, 30, 40, 50, 20)
print(tuple(set1)) # (100, 200, 300, 400, 500)

# list() 将序列转换为列表
print(list(tuple1)) # ['a', 'b', 'c', 'd', 'e']
print(list(set1)) # [100, 200, 300, 400, 500]

# set() 将序列转换为集合
print(set(tuple1)) # {'e', 'd', 'a', 'b', 'c'}
print(set(list1)) # {40, 10, 50, 20, 30}

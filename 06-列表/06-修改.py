name_list = ['Tom', 'Lily', 'Rose']

# 修改指定下表数据
name_list[0] = 'aaa'
print(name_list) # ['aaa', 'Lily', 'Rose']


# reverse() 逆序
list1 = [1, 3, 2, 5, 4, 6]
list1.reverse()
print(list1) # [6, 4, 5, 2, 3, 1]


# sort() 排序：升序 和 降序
# 列表序列.sort( key=None, reverse=False)
list1.sort()
print(list1) # [1, 2, 3, 4, 5, 6]默认升序

list1.sort(reverse=True)
print(list1) # [6, 5, 4, 3, 2, 1]
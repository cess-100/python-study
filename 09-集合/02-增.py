s1 = {10, 20}

# add() 增加单一数据
s1.add(100)
s1.add(10)
print(s1)  # {100, 10, 20}

# add不能追加序列
# s1.add([10, 20, 30]) TypeError: unhashable type: 'list'


s2 = {10, 20}
# update() 追加的数据是序列
s2.update([10, 20, 30, 40, 50])
print(s2)  # {40, 10, 50, 20, 30}

# update不能追加单一数据
# s2.update(100) TypeError: 'int' object is not iterable

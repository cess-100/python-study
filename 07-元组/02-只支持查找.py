tuple1 = ('aa', 'bb', 'cc', 'bb')

# 1.下标
print(tuple1[0]) # aa

# 2.index() 找不到报错
print(tuple1.index('bb')) # 1
print(tuple1.index('bb', 2, 4)) # 3

# 3.count()
print(tuple1.count('aa')) # 1
print(tuple1.count('aaa')) # 0

# 4.len()
print(len(tuple1)) # 4
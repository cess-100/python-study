mystr = "hello world and cess and success and Python"

# 1,find()
print(mystr.find('and'))  # 12
print(mystr.find('and', 15, 30))  # 21
print(mystr.find('ands'))  # -1  没找到

# 2.index()
print(mystr.index('and'))  # 12
print(mystr.index('and', 15, 30))  # 21
# print(mystr.index('ands', 15, 30)) # 报错

# 3.count()
print(mystr.count('and'))  # 3
print(mystr.count('and', 15, 30))  # 1
print(mystr.count('ands'))  # 0

# 4.rfind()
print(mystr.rfind('and'))  # 33
print(mystr.rfind('and', 15, 30))  # 21
print(mystr.rfind('ands'))  # -1  没找到

# 4.rindex()
print(mystr.rindex('and'))  # 33
print(mystr.rindex('and', 15, 30))  # 21
# print(mystr.rindex('ands') # 报错

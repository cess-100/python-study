# 没有顺序
s1 = {10, 20 , 30, 40, 50}
print(s1) # {40, 10, 50, 20, 30}

# 集合元素不能重复
s2 = {10, 20 , 30, 40, 50, 30, 20}
print(s2) # {40, 10, 50, 20, 30}

# 会将序列拆分
s3 = set('abcdefg')
print(s3) # {'e', 'c', 'f', 'd', 'g', 'a', 'b'}

# {}用来创建字典，要创建集合只能set()
s4 = set()
print(type(s4)) # <class 'set'>
s5 = {}
print(type(s5)) # <class 'dict'>
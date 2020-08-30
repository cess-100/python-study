# 方法⼀：借助第三变量存储数据
a = 10
b = 20

# c = 0
c = a
a = b
b = c
print(a)
print(b)


# ⽅法二
a, b = 1, 2
a, b = b, a
print(a)
print(b)

t1 = ('aa', 'bb', 'cc', 'bb')
# tuple1[0] = 'aaa'
# TypeError: 'tuple' object does not support item assignment

t2 = ('aa', 'bb', ['cc', 'dd'])
print(t2[2])  # ['cc', 'dd']
print(t2[2][0])  # cc
# 元组里放列表，列表内的数据可以改
t2[2][0] = 'tom'
print(t2)  # ('aa', 'bb', ['tom', 'dd'])

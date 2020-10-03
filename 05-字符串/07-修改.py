mystr = "hello world and cess and success and Python"

# 1.replace() 把and换成he
# 说明replace函数有返回值，返回修改后的字符串
new_str = mystr.replace('and', 'he')
print(mystr)
print(new_str)
# --- 说明字符串是不可变数据类型
# 数据是否可以改变划分为 可变类型 和 不可变类型

new_str = mystr.replace('and', 'he', 1)  # 只替换第一次出现的and
new_str = mystr.replace('and', 'he', 10)  # 替换次数超过就是替换所有


# 2.split() -- 分割，返回一个列表,会丢失分割字符
list1 = mystr.split('and')
list2 = mystr.split('and', 2)
print(list1)  # ['hello world ', ' cess ', ' success ', ' Python']
print(list2)  # ['hello world ', ' cess ', ' success and Python']


# 3.join() -- 合并列表里的字符串数据为一个大字符串
mylist = ['aa', 'bb', 'cc']
new_str = '...'.join(mylist)
print(new_str)  # aa...bb...cc

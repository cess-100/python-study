# 1. float() -- 转换成浮点型
num1 = 1
str1 = '10'

print(type(float(num1))) # float
print(float(num1)) # 1.0
print(float(str1)) # 10.0

# 2. str() -- 转换成字符串串类型
print(type(str(num1))) # str

# 3. tuple() -- 将⼀一个序列列转换成元组
list1 = [10, 20, 30]

print(tuple(list1)) # (10, 20, 30)

# 4. list() -- 将⼀一个序列列转换成列列表
t1 = (100, 200, 300)

print(list(t1)) # [100, 200, 300]

# 5. eval() -- 将字符串串中的数据转换成Python表达式原本类型
str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000, 3000)'
str5 = '[1000, 2000, 3000]'

print(eval(str2)) # 1
print(eval(str3)) # 1.1
print(eval(str4)) # (1000, 2000, 3000)
print(eval(str5)) # [1000, 2000, 3000]

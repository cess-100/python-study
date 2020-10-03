mystr = "hello world and itcast and itheima and Python"
mystr1 = '12345'
mystr2 = 'abc123'
mystr3 = '   '

# 1.startswith()
print(mystr.startswith('hello'))  # True
print(mystr.startswith('hello', 5, 20))  # False

# 2.endswith()
print(mystr.endswith('Python'))  # True
print(mystr.endswith('Python', 5, 20))  # False

# 3.isalpha() 全部由字母组成
print(mystr.isalpha())  # False

# 4.isdigit()
print(mystr.isdigit())  # False
print(mystr1.isdigit())  # True

# 5.isalnum() 数字或字母
print(mystr.isalnum())  # False
print(mystr1.isalnum())  # True
print(mystr2.isalnum())  # True

# 6.isspace() 字符串只包含空格
print(mystr.isspace())  # False
print(mystr3.isspace())  # True

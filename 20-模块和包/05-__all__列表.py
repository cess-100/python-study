from my_module2 import *

testA()

# 报错 NameError: name 'testB' is not defined
# 因为testB函数没有添加到all列表，只有all列表里面的功能才能导入
testB()
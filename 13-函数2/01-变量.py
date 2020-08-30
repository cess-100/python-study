"""
局部变量：定义在函数体内部的变量，即只在函数体内部生效
作用：在函数体内部临时保存数据，当函数调⽤用完成后，则销毁局部变量
"""
def testA():
    a = 100
    print(a) #

testA()
# print(a)  报错


"""
全局变量：指的是在函数体内、外都能生效的变量
"""
# 定义全局变量a
a = 100
print(a)

def testA():
    print(a)

def testB():
    a = 200 # 局部变量
    print(a)

def testC():
    global a # 声明a为全局变量
    a = 300
    print(a)

testA() # 100
testB() # 200
testC() # 300

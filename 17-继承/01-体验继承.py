"""
经典类
    class 类名:
        代码
        ......

新式类
    class 类名(object):
        代码
        ......
"""


# 父类A
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


# 子类B 继承父类A
class B(A):
    pass


result = B()
result.info_print() # 1

"""
继承指的是多个类之间的所属关系，即⼦子类默认继承父类的所有属性和方法
所有类默认继承object类，object类是顶级类或基类；其他子类叫做派生类
"""
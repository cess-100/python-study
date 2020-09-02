# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print('使用%s制作煎饼果子' % self.kongfu)


# 学校类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print('使用%s制作煎饼果子' % self.kongfu)


# 徒弟类
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'

    def make_cake(self):
        print('使用%s制作煎饼果子' % self.kongfu)


daqiu = Prentice()

# [独创煎饼果子配方]
print(daqiu.kongfu)

# 使用[独创煎饼果子配方]制作煎饼果子
daqiu.make_cake()

# 类名.__mro__  查看继承顺序
# (<class '__main__.Prentice'>, <class '__main__.School'>,
# <class '__main__.Master'>, <class 'object'>)
print(Prentice.__mro__)

"""
子类和父类具有同名属性和方法，默认使用子类的同名属性和方法
"""

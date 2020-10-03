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
    pass


daqiu = Prentice()
print(daqiu.kongfu)  # [黑马煎饼果子配方]
daqiu.make_cake()  # 使用[黑马煎饼果子配方]制作煎饼果子

"""
注意：当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法
"""

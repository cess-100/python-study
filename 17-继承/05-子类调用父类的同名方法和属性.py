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
        # 加初始化，是防止上次调用的init方法不是自己的，从而kongfu属性值不是自己的
        self.__init__()
        print('使用%s制作煎饼果子' % self.kongfu)

    # 子类调用父类的同名方法
    def make_master_cake(self):
        # 父类类名.函数()
        # 再次调用初始化方法的原因：这里想要调用父类的同名方法和属性，
        # 属性在init初始化位置，所以需要再次调用
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


daqiu = Prentice()
print(daqiu.kongfu)  # [独创煎饼果子配方]

daqiu.make_cake()
daqiu.make_master_cake()
daqiu.make_school_cake()
daqiu.make_cake()

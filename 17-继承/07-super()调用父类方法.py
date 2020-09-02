# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print('使用%s制作煎饼果子' % self.kongfu)


# 学校类
class School(Master):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print('使用%s制作煎饼果子' % self.kongfu)

        # 方法2.1 super(当前类名, self).函数()
        # super(School, self).__init__()
        # super(School, self).make_cake()

        # 方法2.2 super().函数()
        super().__init__()
        super().make_cake()


# 徒弟类
class Prentice(School):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'

    def make_cake(self):
        self.__init__()
        print('使用%s制作煎饼果子' % self.kongfu)

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    def make_old_cake(self):
        # 方法一：代码冗余，如果父类类名变化，这里代码需要频繁修改
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self)

        # 方法二：super()
        # 方法2.1 super(当前类名, self).函数()
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()

        # 方法2.2 super().函数()
        super().__init__()
        super().make_cake()


daqiu = Prentice()

daqiu.make_old_cake()

"""
使用super() 可以自动查找父类。调用顺序遵循 __mro__ 类属性的顺序
比较适合单继承使用
"""
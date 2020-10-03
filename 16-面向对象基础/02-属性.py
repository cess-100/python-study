class Washer(object):
    def wash(self):
        print('洗衣机洗衣服')

    def print_info(self):
        print('洗衣机的宽度是%d' % self.width)
        print('洗衣机的高度是%d' % self.height)


haier1 = Washer()

# 添加属性  对象名.属性名 = 值
haier1.width = 400
haier1.height = 500

# 获取属性  对象名.属性名
print('haier1洗衣机的宽度是%d' % haier1.width)
print('haier1洗衣机的高度是%d' % haier1.height)

# 类里⾯获取对象属性  self.属性名
haier1.print_info()

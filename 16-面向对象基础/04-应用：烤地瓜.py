"""
需求主线：
1. 被烤的时间和对应的地瓜状态：
    0-3分钟：生的
    3-5分钟：半生不熟
    5-8分钟：熟的
    超过8分钟：烤糊了
2. 添加的调料：
    用户可以按自己的意愿添加调料
"""


class SweetPotato:
    def __init__(self):
        # 烤地瓜的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_state = '生的'
        # 添加的佐料
        self.condiments = []

    def __str__(self):
        return f"地瓜烤了{self.cook_time}分钟，{self.cook_state},添加的调料有{self.condiments}"

    def cook(self, time):
        """烤地瓜方法"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        if 5 <= self.cook_time < 8:
            self.cook_state = '熟的'
        if self.cook_time > 3:
            self.cook_state = '烤糊了'

    def add_condiments(self, condiment):
        """添加调料方法"""
        self.condiments.append(condiment)


digua1 = SweetPotato()
print(digua1)

digua1.cook(2)
digua1.add_condiments('酱油')
print(digua1)

digua1.cook(1)
digua1.add_condiments('辣椒面')
print(digua1)

digua1.cook(2)
print(digua1)

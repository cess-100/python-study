"""
将小于房⼦子剩余面积的家具摆放到房子中
需求涉及两个事物：房子 和 家具，故被案例涉及两个类：房子类 和 家具类
"""


class Furniture:
    def __init__(self, name, area):
        # 家具名称
        self.name = name
        # 占地面积
        self.area = area


class Home:
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 空余面积
        self.free_area = area
        # 家具列表
        self.furnitures = []

    def __str__(self):
        return f"房屋位于{self.address}， 面积为{self.area}， 空余面积为{self.free_area}， 家具列表为{self.furnitures}"

    def add_furniture(self, furniture):
        """容纳家具"""
        if self.free_area >= furniture.area:
            self.free_area -= furniture.area
            self.furnitures.append(furniture.name)
        else:
            print("家具面积太大，房屋无法容纳")


home = Home('成都', 300)
print(home)

bed = Furniture('双人床', 4)
home.add_furniture(bed)
print(home)

sofa = Furniture('沙发', 8)
home.add_furniture(sofa)
print(home)

court = Furniture('篮球场', 600)
home.add_furniture(court)
print(home)

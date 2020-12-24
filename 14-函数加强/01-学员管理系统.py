# 存储所有学员信息
info = []


def print_info():
    print("请选择功能---------------")
    print("1.添加学员")
    print("2.删除学员")
    print("3.修改学员信息")
    print("4.查询学员信息")
    print("5.显示所有学员信息")
    print("6.退出系统")


def add_info():
    """添加学员函数"""
    new_id = input("请输入学号：")
    new_name = input("请输入姓名：")
    new_tel = input("请输入手机号：")

    global info

    # 检测输入姓名是否存在，存在则报错提示
    for i in info:
        if new_name == i['name']:
            print("用户已存在")
            # 退出当前函数，函数后续代码不执行
            return

    # 添加信息
    info_dict = {'id': new_id, 'name': new_name, 'tel': new_tel}
    info.append(info_dict)

    print(info)


def del_info():
    """删除学员"""
    del_name = input('请输入要删除学员的姓名：')

    global info

    for i in info:
        # 判断是否存在
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('该学员不存在')

    print(info)


def modify_info():
    pass
    """修改学员信息"""
    # 用户输入学员姓名
    modify_name = input('请输入要修改的学员姓名：')

    global info

    # 检查info中是否存在此学员
    for i in info:
        # 若存在则修改信息
        if modify_name == i['name']:
            i['tel'] = int(input("学员修改的新手机号"))
            break
    # 若不存在则提示
    else:
        print('该学员姓名不存在')

    print(info)


def search_info():
    pass
    """查询学员信息"""
    # 输入要查询的学员姓名
    search_name = input('请输入要查询学员的姓名')

    global info

    # 查询是否存在此学员
    for i in info:
        # 若存在则显示学员信息
        if search_name == i['name']:
            print('查询到的信息如下-----------')
            print(f'学员姓名是{i["name"]}，id是{i["id"]},手机号是{i["tel"]}')
            break
    # 若不存在则提示输入错误
    else:
        print('该学员姓名不存在')


def print_all():
    """显示所有学员信息"""
    print('id\tname\ttel')
    for i in info:
        print('%s\t%s\t%s' % (i['id'], i['name'], i['tel']))


# 系统功能需要循环使用，知道用户输入6，才推出系统
while True:
    # 1. 显示功能界⾯面
    print_info()

    # 2. ⽤用户输⼊入功能序号
    user_num = int(input("请输入功能序号："))

    # 3. 根据⽤用户输⼊入的功能序号，执⾏行行不不同的功能(函数)
    # 3.1 定义函数
    # 3.2 调⽤用函数
    if user_num == 1:
        # print("1.添加学员")
        add_info()
    elif user_num == 2:
        # print("2.删除学员")
        del_info()
    elif user_num == 3:
        # print("3.修改学员信息")
        modify_info()
    elif user_num == 4:
        # print("4.查询学员信息")
        search_info()
    elif user_num == 5:
        # print("5.显示所有学员信息")
        print_all()
    elif user_num == 6:
        # print("6.退出系统")
        exit_flag = input('确定要退出吗？yes or no')
        if exit_flag == 'yes':
            break
    else:
        print("输入序号有误，请重新输入")

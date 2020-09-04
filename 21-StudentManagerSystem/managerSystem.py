from student import *


class StudentManager(object):
    def __init__(self):
        # 存储学员数据 -- 列表
        self.student_list = []

    def run(self):
        self.load_student()

        while True:
            self.show_menu()

            menu_num = int(input('请输入你需要的功能序号'))

            if menu_num == 1:
                self.add_stuent()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modeify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break

    @staticmethod
    def show_menu():
        """显示菜单"""
        print('请选择如下功能')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')

    def add_stuent(self):
        """添加学员信息"""
        name = input("请输入姓名：")
        gender = input("请输入性别")
        tel = input("请输入手机号：")

        # 检测输入姓名是否存在，存在则报错提示
        for i in self.student_list:
            if name == i.name:
                print("用户已存在")
                # 退出当前函数，函数后续代码不执行
                return

        student = Student(name, gender, tel)
        self.student_list.append(student)

    def del_student(self):
        """删除学员信息"""
        del_name = input('请输入要删除学员的姓名：')

        for i in self.student_list:
            # 判断是否存在
            if del_name == i.name:
                self.student_list.remove(i)
                break
        else:
            print('该学员不存在')

    def modeify_student(self):
        """修改学员信息"""
        # 用户输入学员姓名
        modify_name = input('请输入要修改的学员姓名：')

        # 检查info中是否存在此学员
        for i in self.student_list:
            # 若存在则修改信息
            if modify_name == i.name:
                i.gender = input('请输⼊入学员性别：')
                i.tel = input('请输⼊入学员⼿手机号：')
                print(f'修学员信息成功，姓名{i.name},性别{i.gender}, 手机号{i.tel}')
                break
        # 若不存在则提示
        else:
            print('该学员姓名不存在')

        print(self.student_list)

    def search_student(self):
        """查询学员信息"""
        # 输入要查询的学员姓名
        search_name = input('请输入要查询学员的姓名')

        # 查询是否存在此学员
        for i in self.student_list:
            # 若存在则显示学员信息
            if search_name == i.name:
                print('-----查询到的信息如下-----')
                print(f'学员姓名是{i.name}，性别{i.gender},手机号是{i.tel}')
                break
        # 若不存在则提示输入错误
        else:
            print('该学员姓名不存在')

    def show_student(self):
        """显示所有学员信息"""
        print('姓名\t性别\t手机号')
        for i in self.student_list:
            print('%s\t%s\t%s' % (i.name, i.gender, i.tel))

    def save_student(self):
        """保存学员信息"""
        f = open('student.data', 'w')

        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)

        f.write(str(new_list))

        f.close()

    def load_student(self):
        """加载学员信息"""
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()
            # 将字符串转换为它本来的格式
            new_list = eval(data)

            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            f.close()

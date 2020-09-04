"""
工作中注意事项
1. 为了方便维护代码，一般一个角色一个程序文件；
2. 项目要有主程序入口，习惯为main.py
"""

from managerSystem import *

if __name__ == '__main__':
    student_manager = StudentManager()
    student_manager.run()

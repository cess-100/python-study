"""
import 包名.模块名
包名.模块名.功能
"""

# import mypackage.my_module1
# mypackage.mymodule1.info_print1()


"""
from 包名 import *
模块名.⽬目标
"""
# 此方式下需要设置__init__.py文件，添加__all__ = [],控制允许导入的模块列表
from mypackage import *

my_module1.info_print1()

# all列表未设置
# NameError: name 'my_module2' is not defined
# my_module2.info_print1()

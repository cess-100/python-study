"""
# 模块定义别名
    import 模块名 as 别名
# 功能定义别名
    from 模块名 import 功能 as 别名

定义了别名就只能使用别名，不能使用原名
"""

# 模块别名
import time as tt
tt.sleep(2)
print('hello')


# 功能别名
from time import sleep as sl
sl(2)
print('hello')

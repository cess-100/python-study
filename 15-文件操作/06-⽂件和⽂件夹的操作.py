import os

# os.rename(目标文件名, 新文件名) 文件重命名
# os.rename('000.txt', '111.txt')

# os.remove(目标文件名) 删除文件
# os.remove('111.txt')

# os.mkdir(文件夹名字) 创建文件夹
# 如果文件夹已存在，报错
os.mkdir('aa')

# os.rmdir(文件夹名字) 删除文件夹
# 目录不为空，无法删除
os.rmdir('aa')

# os.getcwd() 获取当前目录
print(os.getcwd()) # D:\develop\PycharmProjects\code\15-文件操作

# os.chdir(目录) 改变默认目录
# os.mkdir('aa')
# os.chdir('aa') # 切换至aa目录里面
# os.mkdir('bb') # bb为aa的子文件夹

# os.listdir(目录) 获取目录列表
print(os.listdir())
# ['01-文件基本操作步骤.py', '02-访问模式.py', '03-读.py', '03test.txt', '04-seek.py', '05-文件备份.py', '06-⽂件和⽂件夹的操作.py']



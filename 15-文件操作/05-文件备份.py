# 1. 接收用户输入的文件名
old_name = input('请输入要备份的文件名')

# 2. 规划备份文件名
index = old_name.rfind('.')
if index > 0:
    postfix = old_name[index:]
    new_name = old_name[:index] + '[备份]' + postfix

    # 3. 备份文件写入数据
    old_file = open(old_name, 'rb')
    new_file = open(new_name, 'wb')

    while True:
        content = old_file.read(1024)
        if len(content) == 0:
            break
        new_file.write(content)

    old_file.close()
    new_file.close()
else:
    print('输入文件名有误')

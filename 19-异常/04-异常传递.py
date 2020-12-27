import time

try:
    f = open('test.txt', 'r')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            # 休眠2秒
            time.sleep(2)
            print(content, end='')
    except:
        # 如果在读取文件的过程中，产生了了异常，那么就会捕获到
        # 比如 按下了了 ctrl+c
        print('意外终止了读取数据')
    finally:
        f.close()
        print('文件已关闭')
except:
    print('没有这个文件')

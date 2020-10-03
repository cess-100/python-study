# while实现 ------------
list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for实现 -------------
list2 = []
for i in range(10):
    list2.append(i)
print(list2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 推导式实现 ------------
list3 = [i for i in range(10)]
print(list3)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 带if的列表推导式
# 创建0-10的偶数列表推导式
# 方式一：
list4 = [i for i in range(0, 10, 2)]
print(list4)  # [0, 2, 4, 6, 8]
# 方式二：
list5 = []
for i in range(10):
    if i % 2 == 0:
        list5.append(i)
print(list5)

# 方式三：
list6 = [i for i in range(10) if i % 2 == 0]
print(list6)


# 多个for循环实现列表推导式
# 创建[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 方式一：
list7 = []
for i in range(1, 3):
    for j in range(3):
        list7.append((i, j))
print(list7)

# 方式二：
list8 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list8)

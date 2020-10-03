# 1 if控制 将奇偶判断交由程序
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1

print(sum)


# 2 计数器控制
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 2

print(sum)

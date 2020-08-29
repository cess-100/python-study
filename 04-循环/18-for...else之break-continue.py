str  = "success"
for i in str:
    if i == 'e':
        break
    print(i)
else:
    print("循环正常结束执行的代码")

print()
str  = "success"
for i in str:
    if i == 'e':
        continue
    print(i)
else:
    print("循环正常结束执行的代码")
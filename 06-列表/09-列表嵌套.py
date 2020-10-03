name_list = [['小明', '小红', '小绿'],
             ['Tom', 'Lily', 'Rose'],
             ['张三', '李李四', '王五']]

print(name_list[0])  # ['小明', '小红', '小绿']
print(name_list[1][1])  # Lily

i = 0
while i < len(name_list):
    for j in name_list[i]:
        print(j)
    i += 1

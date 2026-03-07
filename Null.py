#将 00 改为 0 (Python不支持 00 这种写法)，或者直接使用字符串列表
lst = [80, 89, 0, 98, 0, 99]
print(lst)
# 遍历列表,取出索引
for index in range(len(lst)):
    # 逻辑保持原样：判断转换为字符串后是否不等于 '0'
    # 注意：原列表中的 0 会变成 '0'，00 如果存在也会被当作 0 处理
    if str(lst[index]) != '0':
        lst[index] = '19' + str(lst[index])
    else:
        # 原题意图可能是想把 00 变成 2000，这里对应逻辑是 200 + '0' = '2000'
        lst[index] = '200' + str(lst[index])
print(lst)



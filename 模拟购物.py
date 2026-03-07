#存储入库的商品信息
goods_list = [] #商品列表
cart = []       #购物车

#录入5个商品信息
print("请录入5个商品信息（格式：编号-名称）：")
for i in range(5):
    while True:
        info = input(f"请输入第{i + 1}个商品：").strip()#strip移除输入字符串首尾的空白字符（包括空格、换行符、制表符等）
        if " " in info:#判断用户输入的字符串中是否包含至少一个空格，目的是确保用户按 “编号-名称” 的格式输入
            goods_id, goods_name = info.split(maxsplit=1)#按照编号-名称拆分用户输入的商品信息
            goods_list.append((goods_id, goods_name))#将商品信息以元组形式存入列表
            break
        else:
            print("格式错误，请按“编号 名称”的格式重新输入！")

#展示所有商品
print("\n当前商品列表：")
for idx, (goods_id, goods_name) in enumerate(goods_list, start=1):
    print(f"{idx}. {goods_id} {goods_name}")

#循环选择商品添加到购物车
while True:
    choice = input("\n请输入要添加到购物车的商品编号（输入q结束）：").strip()
    if choice.lower() == "q":
        break
    #查找商品
    found = False
    for goods in goods_list:
        if goods[0] == choice:
            cart.insert(0, goods)# 逆序添加到购物车
            print(f"已将商品 {goods[1]} 添加到购物车！")
            found = True
            break
    if not found:
        print("商品不存在，请重新输入！")
#显示购物车商品
print("\n购物车中的商品（逆序）：")
if cart:
    for idx, (goods_id, goods_name) in enumerate(cart, start=1):
        print(f"{idx}. {goods_id} {goods_name}")
else:
    print("购物车为空。")
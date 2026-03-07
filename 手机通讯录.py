def get_contact_info() -> tuple:
    """
    获取并解析联系人信息，返回(姓名, 电话)元组，处理空输入和手机号格式
    """
    while True:
        info = input().strip()
        if not info:
            print("输入不能为空，请重新输入：")
            continue

        Len=len(info)
        split_index = 0
        while split_index < Len and not info[split_index].isdigit():
            split_index += 1
        name = info[:split_index].strip()  #切片取字符串从开头到拆分索引的部分（姓名）
        phone = info[split_index:].strip() #切片取字符串从拆分索引到结尾的部分（电话）

        #校验手机号是11位数字
        if not name or not phone or not phone.isdigit() or len(phone) != 11:
            print("格式错误！请输入【姓名+11位手机号码】（例：张三13800138000），重新输入：")
            continue
        return (name, phone)

# 初始化空集合
contact_set = set()

# 录入5条不重复的联系人信息
while len(contact_set) < 5:
    current_count = len(contact_set) + 1
    print(f"请输入第{current_count}位好友的姓名与手机号码：", end="")
    contact = get_contact_info()
    if contact in contact_set:#in是成员运算符，核心功能是判断 “元素是否在容器中”，返回True/False
        print(f"【提示】{contact[0]}（{contact[1]}）已存在，无需重复录入！")
        continue
    contact_set.add(contact)
    print(f"成功录入第{current_count}位好友：{contact[0]}（{contact[1]}）")

print("\n最终通讯录：")
#转为列表按录入顺序打印
contact_list = list(contact_set)#若要严格有序，需用列表记录录入顺序
for idx, (name, phone) in enumerate(contact_list, 1):
    print(f"{idx}. {name} - {phone}")
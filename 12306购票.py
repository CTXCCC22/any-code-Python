def print_train_list(trains):
    """打印车次列表"""
    print("车次\t\t出发站-到达站\t出发时间\t到达时间\t历时时长")
    for train in trains.values():
        print(f"{train['车次']}\t{train['出发站-到达站']}\t{train['出发时间']}\t{train['到达时间']}\t{train['历时时长']}")

def select_train(trains):
    """选择车次"""
    while True:
        train_id = input("\n请输入要购买的车次：").strip()
        if train_id in trains:
            return trains[train_id]
        print("车次不存在，请重新输入！")

def get_passengers():
    """获取乘车人信息"""
    return input("请输入乘车人，如果是多位乘车人使用逗号分隔：").strip()

def print_ticket(train, passengers):
    """打印购票结果"""
    print(f"\n您已购买了 {train['车次']} {train['出发站-到达站']}  {train['出发时间']}开,请{passengers}尽快换取纸制车票。【铁路客服】")

# 车次信息字典（用车次号作为key，方便快速查找）
trains_dict = \
{
    "G1569": {"车次": "G1569", "出发站-到达站": "北京南-天津南", "出发时间": "18:06", "到达时间": "18:39", "历时时长": "00:33"},
    "G1567": {"车次": "G1567", "出发站-到达站": "北京南-天津南", "出发时间": "18:15", "到达时间": "18:49", "历时时长": "00:34"},
    "G8917": {"车次": "G8917", "出发站-到达站": "北京南-天津西", "出发时间": "18:20", "到达时间": "19:19", "历时时长": "00:59"},
    "G203":  {"车次": "G203",  "出发站-到达站": "北京南-天津南", "出发时间": "18:35", "到达时间": "19:09", "历时时长": "00:34"}
}

# 主流程
if __name__ == "__main__":
    print_train_list(trains_dict)
    selected = select_train(trains_dict)
    people = get_passengers()
    print_ticket(selected, people)
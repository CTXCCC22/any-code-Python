#定义全局变量money和name
money = 5000000
name = None

#输入客户姓名
name = input("请输入您的姓名：")

#定义查询余额函数
def check_money(show_money):
    if show_money:
        print("------查询余额------")
    print(f"{name},您的余额为：{money}元")

#定义存款函数
def saving_money(num):
    global money
    money += num
    print("------存款------")
    print(f"{name},您好，成功存款：{money}元")Microsoft.QuickAction.Bluetooth
    #调用check_money函数
    check_money(False)

#定义取款函数
def get_money(num):
    global money
    money -= num
    print("------取款------")
    print(f"{name},您好，成功取款：{money}元")
    # 调用check_money函数
    check_money(False)

#主函数
def main():
    print("------主菜单------")
    print(f"{name},欢迎来到CTX银行，很高兴为您服务")
    print("查询余额\t\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return (input("请输入您要办理的业务；"))

#设置循环
while True:
    kerboard_input = main()
    if kerboard_input == "1":
        check_money(True)
        continue   #
    elif kerboard_input == "2":
        num =int(input("您要存入多少钱："))
        saving_money(num)
        continue
    elif kerboard_input == "3":
        num = int(input("您要取出多少钱："))
        get_money(num)
        continue
    else:
        print("退出程序，谢谢光临")
        break;
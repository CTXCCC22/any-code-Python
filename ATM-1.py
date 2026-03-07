def atm_simulation():
    """
    ATM模拟系统 - 每次调用此函数都会创建全新的会话
    所有账户状态（余额等）都会重置，不保留任何历史记录
    """
    # 每次调用函数时都重置账户余额
    balance = 0.0

    print("\n===== 新会话已开始 =====")
    print("欢迎使用简易ATM系统 (所有记录已重置)")

    while True:
        print("\n请选择操作:")
        print("1. 查询余额")
        print("2. 存款")
        print("3. 取款")
        print("4. 退出系统")

        choice = input("\n请输入选项 (1-4): ").strip()

        if choice == '1':
            # 查询余额
            print(f"\n当前账户余额: ¥{balance:.2f}")

        elif choice == '2':# 存款功能
            try:
                amount_input = input("请输入存款金额: ").strip()
                if not amount_input:
                    print("输入不能为空")
                    continue

                amount = float(amount_input)
                if amount > 0:
                    balance += amount
                    print(f"\n✅ 存款成功！")
                    print(f"  存入金额: ¥{amount:.2f}")
                    print(f"  当前余额: ¥{balance:.2f}")
                else:
                    print("存款金额必须大于0!!!")
            except ValueError:
                print("无效输入，请输入有效的数字金额!!!")

        elif choice == '3':
            # 取款功能
            try:
                amount_input = input("请输入取款金额: ").strip()
                if not amount_input:
                    print("输入不能为空")
                    continue

                amount = float(amount_input)
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"\n✅ 取款成功！")
                        print(f"取出金额: ¥{amount:.2f}")
                        print(f"当前余额: ¥{balance:.2f}")
                    else:
                        print(f"余额不足！当前余额: ¥{balance:.2f}")
                        print(f"无法取出: ¥{amount:.2f}")
                else:
                    print("取款金额必须大于0")
            except ValueError:
                print("无效输入，请输入有效的数字金额")

        elif choice == '4':
            # 退出系统 - 自动清除所有状态
            print("\n" + "=" * 30)
            print("感谢使用ATM系统！")
            print("所有会话数据已清除")
            print("下次使用将创建全新账户")
            print("=" * 30)
            break

        else:
            print("❌ 无效选项，请输入1-4之间的数字")


# 启动ATM系统
if __name__ == "__main__":
    # 每次运行脚本都会创建全新会话
    atm_simulation()
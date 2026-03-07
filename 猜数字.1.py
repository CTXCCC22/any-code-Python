import random     #随机产生数字
num=random.randint(1,10)

#通过if判断数字猜测  三次机会
guess_num = int(input("请输入你要猜测的数字："))   #第一次猜测
if guess_num == num:
    print("恭喜，第一次就猜中了")
else:
    if guess_num > num:
        print("您猜测的数字大了")
    else:
        print("您猜测的数字小了")

    guess_num = int(input("第二次输入你要猜测的数字："))  #第二次猜测
    if guess_num == num:
        print("恭喜,第二次猜中了")
    else:
        if guess_num > num:
            print("您猜测的数字大了")
        else:
            print("您猜测的数字小了")

            guess_num = int(input("第三次输入你要猜测的数字："))  # 第三次猜测
            if guess_num == num:
                print("恭喜，第三次就猜中了")
            else:
                if guess_num > num:
                    print("您猜测的数字大了")
                else:
                    print("您猜测的数字小了")


import random
num = random.randint(1, 100)

count = 0
flag = True

while flag:
    guess_num = int(input("请输入数字："))
    count += 1
    if guess_num == num:
        print("您猜中了")
        flag = False
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")

print(f"你总共猜测了{count}次")
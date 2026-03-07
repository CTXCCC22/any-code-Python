import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3
def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

speed(1000)
bgcolor("black")
color("#f13487")  # 将颜色设置移到循环外，避免重复设置
penup()  # 先抬起画笔，移动到起始位置
goto(hearta(0)*20, heartb(0)*20)
pendown()  # 放下画笔开始绘制

for i in range(6000):
    goto(hearta(i)*20, heartb(i)*20)

done()

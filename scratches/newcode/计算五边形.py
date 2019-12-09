import  turtle
import math

data = float(input("请输入数据"))

Area = 5*data*data/math.tan(math.pi/5)/4

print(Area)


turtle.circle(data,steps = 5)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()

turtle.write(str(Area))

turtle.done()
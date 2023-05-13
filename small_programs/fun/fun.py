import math
import turtle


def xt(t):
	return 16 * math.sin(t) ** 3 


def yt(t):
	return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)


t = turtle.Turtle()

turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)

num = 371
for i in range(1, 25500):
	t.speed(num)
	t.goto((xt(i) * 15, yt(i) * 15))
	t.pencolor((255-i)%255, i%255, (255%i))
	t.goto(0, 0)
	num = num - 1
	if i % 360 == 0:
		t.clear()
		num = 371


t.hideturtle()
turtle.update()
turtle.mainloop()
import turtle

t = turtle.Turtle()

t.color("purple", "salmon")
t.width(5)

t.penup()
t.goto(-100, -125)
t.pendown()

t.begin_fill()
for i in range(2):
    t.forward(200)
    t.left(90)
    t.forward(250)
    t.left(90)
t.end_fill()

count_x = 0
count_y = 0

def window():
    t.color("brown", "cyan")
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()

for y in range(2):
    for x in range(2):
        t.penup()
        t.goto(-75+count_x, 50-count_y)
        t.pendown()

        window()

        count_x += 100

    count_x = 0
    count_y += 100
    t.penup()
    t.goto(-75, t.ycor()-count_y)
    t.pendown()

t.penup()
t.goto(-20, -125)
t.pendown()

t.color("black", "gold")

t.begin_fill()
for line in range(2):
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.left(90)

t.end_fill()
    
t.penup()
t.goto(100, 125)
t.pendown()

t.color("purple", "yellow")
t.begin_fill()
for i in range(3):
    t.left(120)
    t.forward(200)
t.end_fill()

turtle.exitonclick()
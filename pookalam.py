import turtle

SCALE = 1.4
turtle.speed(0)
turtle.hideturtle()
turtle.home()


def draw_circle(color, radius):
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.pencolor(color)   
    turtle.penup()
    turtle.right(90)
    turtle.forward(radius)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def draw_square(size, color=None):
    """Draw a square with optional color fill (no black border)."""
    if color:
        turtle.fillcolor(color)
        turtle.pencolor(color)
        turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    if color:
        turtle.end_fill()

def big_flower(color):
    """Draw the big flower pattern."""
    for _ in range(13):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.pencolor(color)
        turtle.begin_fill()
        turtle.circle(150 * SCALE, 70)
        turtle.left(110)
        turtle.circle(150 * SCALE, 70)
        turtle.end_fill()
        turtle.right(1)

def draw_kite(t, length, color):
    """Draws a diamond-shaped petal."""
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(length)
        t.right(30)
        t.forward(length)
        t.right(150)
    t.end_fill()

def draw_flower(color, size):
    """Draw a flower made of rotated diamond shapes."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    for _ in range(36):
        draw_kite(t, size, color)
        t.right(10)

def petal(t, radius, angle):
    """Single petal using circular arcs."""
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

def flower(t, petals, radius, angle, color=None):
    """Draw a full flower from petals."""
    if color:
        t.fillcolor(color)
        t.pencolor(color)
        t.begin_fill()
    for _ in range(petals):
        petal(t, radius, angle)
        t.left(360.0 / petals)
    if color:
        t.end_fill()

def connector_petals(t, n, r, angle, color):
    """Draw connecting petals around center."""
    t.color(color)
    t.fillcolor(color)
    t.pencolor(color)
    for _ in range(n):
        t.begin_fill()
        t.circle(r, angle)
        t.left(180 - angle)
        t.circle(r, angle)
        t.left(180 - angle)
        t.end_fill()
        t.left(360 / n)

def small_flower_in_bindi():
    """Draw the small flower at the center (bindi)."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("deeppink")
    t.fillcolor("deeppink")
    t.pencolor("deeppink")

    t.begin_fill()
    flower(t, 6, 12.0 * SCALE, 60.0)
    t.end_fill()

    t.penup()
    t.goto(0, -3 * SCALE)
    t.pendown()
    t.begin_fill()
    t.fillcolor("yellow")
    t.pencolor("yellow")
    t.circle(3 * SCALE)
    t.end_fill()

colorset = ["#ff9933", "#ffd11a", "#800080", "#cc0066",
            "#800080", "#804000", "#2E8B57"]

draw_circle("#800080", 220 * SCALE)
draw_circle("#2417D9", 210 * SCALE)
draw_circle(colorset[6], 200 * SCALE)

num_spots = 24
gap_radius = 205 * SCALE
flower_size = 12 * SCALE
for i in range(num_spots):
    if i % 2 == 0:
        turtle.penup()
        turtle.setheading(i * (360 / num_spots))
        turtle.forward(gap_radius)
        turtle.pendown()
        turtle.fillcolor("#ff66cc")
        turtle.pencolor("#ff66cc")
        turtle.begin_fill()
        flower(turtle, 6, flower_size, 60.0)
        turtle.end_fill()

        turtle.begin_fill()
        turtle.fillcolor("yellow")
        turtle.pencolor("yellow")
        turtle.circle(2.5 * SCALE)
        turtle.end_fill()
        turtle.penup()
        turtle.home()

draw_circle(colorset[5], 190 * SCALE)
draw_circle(colorset[0], 180 * SCALE)
draw_circle(colorset[1], 170 * SCALE)

big_flower(colorset[2])
turtle.right(60); big_flower(colorset[3])
turtle.right(60); big_flower(colorset[0])

draw_circle(colorset[4], 140 * SCALE)

for _ in range(12):
    draw_square(100 * SCALE, colorset[1])
    turtle.right(30)

draw_circle(colorset[0], 125 * SCALE)
draw_flower(colorset[3], 65 * SCALE)
draw_circle(colorset[6], 110 * SCALE)

turtle.begin_fill()
turtle.fillcolor(colorset[4])
turtle.pencolor(colorset[4])
for _ in range(9):
    for _ in range(6):
        turtle.forward(50 * SCALE)
        turtle.right(60)
    turtle.right(40)
turtle.end_fill()

draw_circle(colorset[2], 90 * SCALE)
draw_circle(colorset[1], 80 * SCALE)

for col, size in [(colorset[3], 70), (colorset[0], 60), (colorset[6], 50)]:
    turtle.fillcolor(col)
    turtle.pencolor(col)
    turtle.begin_fill()
    flower(turtle, 9, size * SCALE, 60.0)
    turtle.end_fill()
    turtle.left(30)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
connector_petals(t, 12, 30 * SCALE, 60, "#ff66cc")

draw_circle("blue", 15 * SCALE)
small_flower_in_bindi()

turtle.penup()
turtle.goto(-350 * SCALE, 0)
turtle.color("darkred")
turtle.write("HAPPY", align="center", font=("Times", int(24 * SCALE), "bold"))

turtle.goto(350 * SCALE, 0)
turtle.write("ONAM", align="center", font=("Times", int(24 * SCALE), "bold"))

turtle.done()

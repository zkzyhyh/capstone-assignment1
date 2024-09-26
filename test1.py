import turtle
import math


def draw_circle(pen, radius, color):
    pen.penup()
    pen.goto(0, -radius)
    pen.pendown()
    pen.color(color)
    pen.circle(radius)


def draw_orbit(pen, radius_x, radius_y, angle, color):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.color(color)
    

    angle_radians = math.radians(angle)
    
    for i in range(360):

        x = radius_x * math.cos(math.radians(i))
        y = radius_y * math.sin(math.radians(i))
        

        x_rotated = x * math.cos(angle_radians) - y * math.sin(angle_radians)
        y_rotated = x * math.sin(angle_radians) + y * math.cos(angle_radians)
        

        pen.goto(x_rotated, y_rotated)

def draw_text_on_circle(text, radius, start_angle):
    num_chars = len(text)
    angle_gap = 360 / num_chars
    pen.penup()
    
    for i, char in enumerate(text):
        angle = start_angle + i * angle_gap
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        pen.goto(x, y)
        pen.setheading(angle + 90)
        pen.pendown()
        pen.write(char, align="center", font=("Arial", 18, "normal"))
        pen.penup()



pen = turtle.Turtle()
pen.speed(5)
pen.hideturtle()


draw_circle(pen, 200, "blue")
draw_circle(pen, 140, "blue")

draw_text_on_circle("电子科技大学", 170, 60)


pen.width(2)
draw_orbit(pen, 100, 60, 45, "orange")
draw_orbit(pen, 100, 60, -45, "blue")


pen.penup()
pen.goto(-70, -20)
pen.pendown()
pen.color("blue")
pen.write("UESTC", font=("Arial", 36, "bold"))


pen.penup()
pen.goto(-30, -130)
pen.pendown()
pen.color("black")
pen.write("1956", font=("Arial", 24, "bold"))


turtle.done()

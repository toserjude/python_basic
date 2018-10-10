import turtle


def draw_squares(drawing_turtle, length):
    for i in range(4):
        drawing_turtle.forward(length)
        drawing_turtle.left(90)
        # print(i)


def draw_bigger_squares(drawing_turtle, size, part):
    for i in range(part):
        draw_squares(drawing_turtle, size)
        size = size + 20
        if i < part:
            drawing_turtle.penup()
            drawing_turtle.backward(10)
            drawing_turtle.left(90)
            drawing_turtle.backward(10)
            drawing_turtle.right(90)

            drawing_turtle.pendown()


def draw_angled_squares(drawing_turtle, size, part):
    for i in range(part):
        draw_squares(drawing_turtle, size)
        angle = 360 / part
        drawing_turtle.right(angle)

window = turtle.Screen()
window.bgcolor = "grey"
myturtle = turtle.Turtle()
myturtle.pensize(1)
myturtle.color("hotpink")
print("The first method draw you a simple square")
print("The second method draw you bigger and bigger squares")
print("The first method draw you a fancy circle from square")

chosen_method = int(input("What shape did you choose?"))

if chosen_method == 1:
    draw_squares(myturtle, 20)
elif chosen_method == 2:
    draw_bigger_squares(myturtle, 20, 10)
elif chosen_method == 3:
    draw_angled_squares(myturtle, 20, 10)
else:
    print("You choose is invalid!")
    window.bye()

myturtle.hideturtle()
window.mainloop()

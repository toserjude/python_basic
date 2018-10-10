import turtle


def graphics_start():
    new_window = turtle.Screen()
    return new_window


def add_a_turtle():
    new_turtle = turtle.Turtle()
    new_turtle.pensize(1)
    new_turtle.color("hotpink")
    return new_turtle


def graphics_end(hide_this_turtle, closing_window):
    hide_this_turtle.hideturtle()
    closing_window.mainloop()


def draw_squares(drawing_turtle, length):
    for i in range(4):
        drawing_turtle.forward(length)
        drawing_turtle.left(90)


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


print("The first method draw for you a simple square")
print("The second method draw for you bigger and bigger squares")
print("The third method draw for you a fancy circle from squares")

chosen_method = int(input("What shape did you choose? "))
my_turtle = add_a_turtle()
window = graphics_start()

if chosen_method == 1:
    draw_squares(my_turtle, 20)
    graphics_end(my_turtle, window)
elif chosen_method == 2:
    draw_bigger_squares(my_turtle, 20, 10)
    graphics_end(my_turtle, window)
elif chosen_method == 3:
    draw_angled_squares(my_turtle, 100, 100)
    graphics_end(my_turtle, window)
else:
    print("You choose is invalid!")

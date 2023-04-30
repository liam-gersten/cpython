import Lib.turtle as turtle
import math


def tic_tac_toe():
    pass


def init_turtle():
    print("\ninit turtle")
    yertle = turtle.Turtle()
    yertle.ht()
    yertle.speed(0)
    yertle.up()
    return yertle


def draw_grid():
    print("\ndrawing grid")
    for y in range(80, 200, 80):
        for x in range(80, 200, 80):
            yertle = init_turtle()
            yertle.setpos(0, y)
            yertle.down()
            yertle.setheading(0)
            yertle.forward(240)
            yertle.up()
            yertle.setpos(x, 0)
            yertle.down()
            yertle.setheading(90)
            yertle.forward(240)


def setup_board():
    print("\nsetup board")
    for y in range(40, 280, 80):
        for x in range(40, 280, 80):
            yertle = init_turtle()
            yertle.showturtle()
            yertle.shape("square")
            yertle.shapesize(4, 4, 4)
            yertle.color("#FFFFFF")
            yertle.goto(x, y)
            yertle.onclick(mark)
    draw_grid()


# def mark_win_row(i, c="pink"):
#     yertle = init_turtle()
#     yertle.setpos(0, i * 80 + 40)
#     yertle.setheading(0)
#     yertle.down()
#     yertle.fd(240)


# def mark_win_col(i, c="pink"):
#     yertle = init_turtle()
#     yertle.setpos(i * 80 + 40, 0)
#     yertle.down()
#     yertle.setheading(90)
#     yertle.fd(240)


# def mark_win_diag(i, c="pink"):
#     yertle = init_turtle()
#     yertle.setpos(0, 0)
#     yertle.setheading(45)
#     yertle.down()
#     yertle.forward(240 * math.sqrt(2))
#     yertle.up()
#     yertle.setpos(240, 0)
#     yertle.setheading(135)
#     yertle.down()
#     yertle.forward(240 * math.sqrt(2))


def draw_circle(x, y):
    print("\ndrawing circle")
    global count
    global circle
    radius = 80
    yertle = init_turtle()  # Creating the turtle with this function = error
    yertle.color("red")
    yertle.setpos(x, y-radius)
    yertle.down()
    yertle.showturtle()  # Remove this later, only used for demonstration
    yertle.circle(radius)  # Error occurs here, when the turtle should draw.
    circle = False
    count += 1


def draw_x(x, y):
    print("\ndraw x")
    for angle_heading in range(45, 405, 90):
            global count
            global circle
            mark_size = 70
            yertle = init_turtle()
            yertle.color("blue")
            yertle.showturtle()
            yertle.setpos(x,y)
            yertle.setheading(angle_heading)
            yertle.down()
            yertle.forward(mark_size/2)
            circle = True
            count += 1


def mark(x, y):
    global circle
    global occupied
    column = int(x // 80)
    row = int(y // 80)
    if circle and not occupied[row][column]:
        draw_circle(x, y)
        oh[row][column] = True
        occupied[row][column] = True
    elif not circle and not occupied[row][column]:
        draw_x(x, y)
        ecks[row][column] = True
        occupied[row][column] = True
    else:
        turtle.textinput("BAD CLICK!", "A SHAPE OCCUPIES THAT SPACE! CLICK CANCEL TO DISMISS")
    if count == 9:
        pass


def main():
    print("\nmain")
    turtle.setup(width=680, height=680)
    turtle.screensize(240, 240, "cyan")
    wn = turtle.Screen()
    wn.title('tic-tac-toe')
    setup_board()


circle = True

ecks = [[False, False, False], [False, False, False], [False, False, False]]

oh = [[False, False, False], [False, False, False], [False, False, False]]

occupied = [[False, False, False], [False, False, False], [False, False, False]]

count = 0

if __name__ == '__main__':
    main()
    turtle.TK.mainloop()

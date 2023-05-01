import time
import math


class TicTacToe():
    def __init__(self, turtle_module, name):
        self.turtle = turtle_module
        self.occupied = [[False, False, False] for _ in range(3)]
        self.ecks = [[False, False, False] for _ in range(3)]
        self.oh = [[False, False, False] for _ in range(3)]
        self.circle = True
        self.count = 0
        self.name = name


    def init_turtle(self):
        yertle = self.turtle.Turtle()
        yertle.ht()
        yertle.speed(0)
        yertle.up()
        return yertle


    def draw_grid(self):
        for y in range(80, 200, 80):
            for x in range(80, 200, 80):
                yertle = self.init_turtle()
                yertle.setpos(0, y)
                yertle.down()
                yertle.setheading(0)
                yertle.forward(240)
                yertle.up()
                yertle.setpos(x, 0)
                yertle.down()
                yertle.setheading(90)
                yertle.forward(240)


    def setup_board(self):
        for y in range(40, 280, 80):
            for x in range(40, 280, 80):
                yertle = self.init_turtle()
                yertle.showturtle()
                yertle.shape("square")
                yertle.shapesize(4, 4, 4)
                yertle.color("#FFFFFF")
                yertle.goto(x, y)
                yertle.onclick(self.mark)
        self.draw_grid()


    def draw_circle(self, x, y):
        radius = 20
        yertle = self.init_turtle()  # Creating the turtle with this function = error
        yertle.color("red")
        yertle.setpos(x, y-radius)
        yertle.down()
        yertle.showturtle()  # Remove this later, only used for demonstration
        yertle.circle(radius)  # Error occurs here, when the turtle should draw.
        self.circle = False
        self.count += 1


    def draw_x(self, x, y):
        for angle_heading in range(45, 405, 90):
            mark_size = 70
            yertle = self.init_turtle()
            yertle.color("blue")
            yertle.showturtle()
            yertle.setpos(x,y)
            yertle.setheading(angle_heading)
            yertle.down()
            yertle.forward(mark_size/2)
            self.circle = True
        self.count += 1


    def mark(self, x, y):
        column = int(x // 80)
        row = int(y // 80)
        if self.circle and not self.occupied[row][column]:
            self.draw_circle(x, y)
            self.oh[row][column] = True
            self.occupied[row][column] = True
        elif not self.circle and not self.occupied[row][column]:
            self.draw_x(x, y)
            self.ecks[row][column] = True
            self.occupied[row][column] = True
        else:
            self.turtle.textinput("BAD CLICK!", "A SHAPE OCCUPIES THAT SPACE! CLICK CANCEL TO DISMISS")
        if self.count == 5:
            self.turtle.exitonclick()
        if self.count == 9:
            pass


    def main(self):
        self.turtle.setup(width=680, height=680)
        self.turtle.screensize(240, 240, "cyan")
        wn = self.turtle.Screen()
        wn.title(self.name)
        self.setup_board()



def demo_teleport(teleport_func, turtle) -> None:

    def drawStar(left: int, color: str) -> None:
        turtle.color(color, "yellow")
        current_pos = turtle.pos()
        while True:
            turtle.forward(200)
            turtle.left(left)
            if abs(turtle.pos() - current_pos) < 1:
                break

    turtle.color("red", "yellow")
    turtle.begin_fill()
    turtle.speed(10)
    colors = ["red", "blue", "green"]
    lefts = [130, 170, 140]
    coords = [(-250, -150), (-250, 150)]
    for i in range(3):        
        drawStar(lefts[i], colors[i])
        if i != 2:
            x, y = coords[i]
            if teleport_func == "teleport":
                kwargs = {"x": x, "y": y}
                turtle.teleport(**kwargs)
            else:
                turtle.goto(x, y)
    turtle.end_fill()


if __name__ == "__main__":
    try:
        import Lib.turtle as turtle_mod
        turtle = turtle_mod.Turtle()
        wn = turtle_mod.Screen()
        wn.title('Using goto method')
        demo_teleport("goto", turtle)
        turtle_mod.exitonclick()
        turtle_mod.mainloop()
    except:
        pass
    try:
        import Lib.turtle as turtle_mod
        turtle = turtle_mod.Turtle()
        wn = turtle_mod.Screen()
        wn.title('Using teleport method')
        demo_teleport("teleport", turtle)
        turtle_mod.exitonclick()
        turtle_mod.mainloop()
    except:
        pass
    try:
        import Lib.old_turtle as turtle_mod
        ttt = TicTacToe(turtle_mod, 'tic-tac-toe with bug')
        ttt.main()
        turtle_mod.TK.mainloop()
    except:
        pass
    try:
        import Lib.turtle as turtle_mod
        ttt = TicTacToe(turtle_mod, 'tic-tac-toe without bug')
        ttt.main()
        turtle_mod.TK.mainloop()
    except:
        pass



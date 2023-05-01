import time


def drawStar(left: int, color: str, turtle_mod) -> None:
    turtle_mod.color(color, "yellow")
    current_pos = turtle_mod.pos()
    while True:
        turtle_mod.forward(200)
        turtle_mod.left(left)
        if abs(turtle_mod.pos() - current_pos) < 1:
            break


def demo_teleport(teleport_func) -> None:
    import Lib.turtle as turtle_mod_A
    turtle = turtle_mod_A.Turtle()
    turtle.color("red", "yellow")
    turtle.begin_fill()
    turtle.speed(10)
    colors = ["red", "blue", "green"]
    lefts = [130, 170, 140]
    coords = [(-250, -150), (-250, 150)]
    for i in range(3):        
        drawStar(lefts[i], colors[i], turtle)
        if i != 2:
            x, y = coords[i]
            if teleport_func == "teleport":
                kwargs = {"x": x, "y": y}
                turtle.teleport(**kwargs)
            else:
                turtle.goto(x, y)
    turtle.end_fill()
    turtle_mod_A.onclick(turtle_mod_A.done)
    turtle_mod_A.mainloop()


def show_teleport_before() -> None:
    try:
        demo_teleport("goto")
    except:
        pass


def show_teleport_after() -> None:
    demo_teleport("teleport")


def show_circle_before() -> None:
    import Lib.old_turtle as old_turtle
    from demo_tic_tac_toe import TicTacToe
    ttt = TicTacToe(old_turtle)
    ttt.main()
    old_turtle.TK.mainloop()


def show_circle_after() -> None:
    import Lib.turtle as turtle_mod_C
    from demo_tic_tac_toe import TicTacToe
    ttt = TicTacToe(turtle_mod_C)
    ttt.main()
    turtle_mod_C.TK.mainloop()


if __name__ == "__main__":
    show_teleport_before()
    show_teleport_after()
    show_circle_before()
    show_circle_after()


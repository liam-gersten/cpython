import Lib.turtle as turtle
import Lib.old_turtle as old_turtle


def drawStar(left: int, color: str) -> None:
    turtle.color(color, "yellow")
    current_pos = turtle.pos()
    while True:
        turtle.forward(200)
        turtle.left(left)
        if abs(turtle.pos() - current_pos) < 1:
            break


def demo_teleport(teleport_func) -> None:
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
            teleport_func(x, y)
    turtle.end_fill()
    turtle.done()


def show_teleport_before() -> None:
    demo_teleport(turtle.goto)


def show_teleport_after() -> None:
    demo_teleport(turtle.teleport)


def show_circle_before() -> None:
    global use_turtle
    use_turtle = old_turtle
    import demo_tic_tac_toe


def show_circle_after() -> None:
    global use_turtle
    use_turtle = old_turtle
    import demo_tic_tac_toe


if __name__ == "__main__":
    # show_teleport_before()
    # show_teleport_after()
    # show_circle_before()
    show_circle_after()


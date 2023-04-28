import Lib.turtle as turtle


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


if __name__ == "__main__":
    demo_teleport(turtle.goto)
    # demo_teleport(turtle.teleport)

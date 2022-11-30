"""Painting with python."""

import turtle as t

def tree(x: float, y: float) -> None:
    """Plant a happy little tree."""
    t.penup()
    t.goto(x,y)
    t.pendown()
    trunck_length: float = 45.0
    UP: float = 90.0
    branch(UP, trunck_length)
    t.update()

def branch(angle: float, length: float) -> None:
    """Draw a beautiful branch... recursively."""
    t.setheading(angle)
    t.color("green")
    t.forward(length)
    if length < 5.0:
        ...
    else:
        branch(angle + 25.0, length * 0.75)
        branch(angle - 23.0, length * 0.74)

    t.setheading(angle + 180.0)
    t.forward(length)

t.tracer(0, 0)
tree(0.0, 0.0)
t.getscreen().onclick(tree)
t.done()

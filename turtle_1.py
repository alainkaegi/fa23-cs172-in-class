import math
import stddraw
import sys

class Turtle:

    def __init__(self, x, y, angle):
        """Construct self at (x, y) facing angle degrees counterclockwise from the x-axis."""
        self._x = x
        self._y = y
        self._angle = angle

    def turn_left(self, delta):
        """Rotate self counterclockwise delta degrees."""
        self._angle += delta

    def go_forward(self, step):
        """Move self forward. `step` defines the distance traveled. Draw a line while moving."""
        oldx = self._x
        oldy = self._y
        self._x += step * math.cos(math.radians(self._angle))
        self._y += step * math.sin(math.radians(self._angle))
        stddraw.line(oldx, oldy, self._x, self._y)

def main():
    n = int(sys.argv[1])
    print(sys.argv[0])
    turtle = Turtle(0.5, 0.0, 180.0/n)
    step_size = math.sin(math.radians(180.0/n))
    stddraw.clear(stddraw.LIGHT_GRAY)
    for i in range(n):
        turtle.go_forward(step_size)
        turtle.turn_left(360.0/n)
    stddraw.show()

if __name__ == '__main__': main()

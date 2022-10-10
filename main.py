from shape import Circle, Shape
from point import Point

s = Circle(Point(1,2),10)
c2 = Circle(Point(10,20),20)

elements = [s,c2]
for s in elements:
    s.Draw()


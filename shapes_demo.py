import shapes


p = shapes.Point(2.0, 3.0)
# print(p.x, p.y)
# print(p.distance())
# print()
q = shapes.Point(5.0,0.0)
# print(q.x,q.y)
# print(p.distance_to(q))

c = shapes.Circle(5,p)
print(f"Radius = {c.radius}, Centre = {(c.centre.x, c.centre.y)}")
print(c.contains(q))

print()

w = shapes.Point(1,1)
t = shapes.Point(2,2)
d = shapes.Rectangle(5, 5, w)
print(d.contains(t))

import turtle
from gps import *
import geopy.distance

SMALL_DIS = 0.1

# add turns at current map
cities = {
    1: ((32.112883, 34.801427), "turn left"),
    2: ((32.112774, 34.793187), "turn right"),
    3: ((32.121807, 34.794367), "turn right"),
    4: ((32.121479, 34.801448), "turn right")
}

geoCarGps = gps

# Create screen
sc = turtle.Screen()
sc.title("Driving directions")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

# Writing on screen
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("green")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("welcome", align="center", font=("Courier", 24, "normal"))

sketch.clear()

while True:
    time.sleep(1)
    sc.update()
    x = 0
    for myGeo in cities.values():
        x = x + 1
        if geopy.distance.distance(geoCarGps, cities[x][0]).km < SMALL_DIS:
            sketch.goto(0, 260)
            sketch.write(cities[x][1], align="center", font=("Courier", 24, "normal"))
            sketch.goto(0, 230)
            sketch.write(align="center", font=("Courier", 24, "normal"))
            sketch.clear()

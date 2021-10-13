import turtle
from gps import *
import geopy.distance


egoCar_gps = (32.110966, 34.801622)
SMALL_DIS = 0.1

cities = {
    1: ((32.112883, 34.801427), "turn left"),
    2: ((32.112774, 34.793187), "turn right"),
    3: ((32.121807, 34.794367), "turn right"),
    4: ((32.121479, 34.801448), "turn right")
}

egoCar_gpsPLACES = {
    1: (32.110966, 34.801622),
    2: (32.111901, 34.801645),
    3: (32.113148, 34.801539),
    4: (32.113237, 34.800391),
    5: (32.113207, 34.799506),
    6: (32.113200, 34.799059),
    7: (32.113054, 34.797239),
    8: (32.112821, 34.794822),
    9: (32.112754, 34.793155),
    10: (32.113243, 34.792537),
    11: (32.114405, 34.793012),
    12: (32.114968, 34.792851),
    13: (32.116450, 34.793345),
    14: (32.119441, 34.793883),
    15: (32.122189, 34.794448),
    16: (32.122504, 34.795185),
    17: (32.122131, 34.797826),
    18: (32.121430, 34.801635),
    19: (32.120907, 34.802042),
    20: (32.120371, 34.801946),
    21: (32.119294, 34.801778),
    22: (32.118354, 34.801668)
}


# ?
geoCarGps = gps
minimum_distance = 0.5
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
time.sleep(3)
sketch.clear()

i = 1
while True:
    time.sleep(1)
    sc.update()
    x=0
    i=i+1
    for myGeo in cities.values():
        x=x+1
        if geopy.distance.distance(egoCar_gpsPLACES[i], cities[x][0]).km < SMALL_DIS:
            sketch.goto(0, 260)
            sketch.write(cities[x][1], align="center", font=("Courier", 24, "normal"))
            sketch.goto(0, 230)
            sketch.write(i, align="center", font=("Courier", 24, "normal"))
            time.sleep(2)
            sketch.clear()


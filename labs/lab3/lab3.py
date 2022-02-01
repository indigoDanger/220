"""
Name: <Indigo Dockery>
<lab3>.py

Problem: <This program uses nested loops to practice accumulations.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def traffic():
    total_roads = eval(input("How many roads were surveyed? "))
    total_cars = 0
    for road in range(total_roads):
        num_cars = 0
        print("How many days was road", road + 1, "surveyed?")
        days = eval(input(""))
        for day in range(days):
            print("How many cars traveled on day", day + 1, "?")
            cars = eval(input(""))
            total_cars = total_cars + cars
            num_cars = num_cars + cars
        day_avg = num_cars / days
        print("Road", road + 1, "average vehicles per day:", day_avg)
    print("Total number of vehicles traveled on all roads:", total_cars)
    avgcar_road = total_cars / total_roads
    print("Average number of vehicles per road:", avgcar_road)


traffic()

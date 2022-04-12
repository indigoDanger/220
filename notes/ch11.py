
def x_sort(circle):
    pass
def y_sort(circle):
    pass

def main():
    my_data = [(2, 3, 9), (20, 30, 29), (12, 230, 90), (200, 31, 2)]
    circles = []
    for data in my_data:
        circles.append(
            Circle(Point(data[0], data[1], data[2]))
        print_c(circles)
        circles.sort(key=x_sort)
        print_c(circles)
        circles.sort(key=y_sort)
        print_c(circles)
        circles.sort(key=Circle.getRadius)
        print_c(circles)
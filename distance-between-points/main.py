from math import sqrt


def get_input():
    p1x = int(input("p1x: "))
    p1y = int(input("p1y: "))
    p2x = int(input("p2x: "))
    p2y = int(input("p2y: "))
    return p1x, p1y, p2x, p2y


def distance_between_points(p1x, p1y, p2x, p2y):
    distance = sqrt((p2x - p1x) ** 2 + (p2y - p1y) ** 2)
    return distance


def main():
    while True:
        p1x, p1y, p2x, p2y = get_input()
        distance = distance_between_points(p1x, p1y, p2x, p2y)
        print(int(distance))


main()

from __future__ import annotations
from typing import Callable, Set


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.intersect = 1

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x+1000 + self.y

    @staticmethod
    def from_str(point_str: str) -> Point:
        vals = point_str.split(',')
        x = int(vals[0])
        y = int(vals[1])
        return Point(x,y)

    def __str__(self):
        return f"{self.x},{self.y}: {self.intersect}"


class Line:
    def __init__(self):
        self.points:  Set = set()
        self.point_count = 0
        self.start: Point = None
        self.end: Point = None

    def add_points(self, point_str: str) -> Line:
        coords = point_str.split(' -> ')
        start = Point.from_str(coords[0])
        end = Point.from_str(coords[1])
        self.start = start
        self.end = end
        self.points.add(start)
        self.points.add(end)
        # Need to increment or decrement based on order of points
        x_inc = 1
        if start.x > end.x:
            x_inc = -1
        start_y = start.y
        y_inc = 1
        if start.y > end.y:
            y_inc = -1
        points = []
        h_or_v = start.x == end.x or start.y == end.y
        for i in range(start.x, end.x+x_inc, x_inc):
            for j in range(start_y, end.y+y_inc, y_inc):
                points.append(Point(i, j))
                # force the 45 degree diagonal
                if not h_or_v:
                    start_y += y_inc
                    break
        self.points = set(points)
        return self

    def intersection(self, other: Line):
        intersections = self.points.intersection(other.points)
        self.point_count += len(intersections)
        for point in intersections:
            point.intersect += 1

    def get_intersected_points(self):
        return [point for point in self.points if point.intersect > 1]


def run(file_path: str, comparison: Callable[[Line], bool]):
    with open(file_path, 'r') as file:
        vents = [Line().add_points(line.replace('\n', '')) for line in file.readlines()]
        vents_to_check = [vent for vent in vents if comparison(vent)]
        for i in range(len(vents_to_check)):
            for j in range(i+1, len(vents_to_check)):
                vents_to_check[i].intersection(vents_to_check[j])

        total = []
        for vent in vents_to_check:
            total.extend(vent.get_intersected_points())
        tot = len(set(total))

        print(tot)



short_file = './resources/day5_short.txt'

long_file = './resources/day5_long.txt'


def first_compare(line: Line):
    return line.start.x == line.end.x or line.start.y == line.end.y


def second_compare(line: Line):
    return True

if __name__ == '__main__':
    run(short_file, first_compare)
    run(long_file, second_compare)
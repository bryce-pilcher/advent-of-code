from __future__ import annotations

from utils import get_file


class Point:
    x: int
    y: int
    visited: bool

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.visited = False

    def __str__(self):
        return f'{self.x},{self.y}'

    def __repr__(self):
        return str(self)

    def move(self, direction: str):
        match direction:
            case 'R':
                self.x += 1
            case 'U':
                self.y += 1
            case 'L':
                self.x -= 1
            case 'D':
                self.y -= 1

    def distance_to(self, other: Point):
        return self.x - other.x, self.y - other.y


if __name__ == '__main__':
    with get_file('day9.txt') as input:
        lines = input.readlines()

        places_visited = []

        part_2_visited = []

        head = Point(0, 0)

        tail = Point(0, 0)

        knots = [Point(0, 0) for _ in range(10)]

        for line in lines:
            cleaned_line = line.strip()
            instructions = line.split(' ')
            direction = instructions[0]
            for _ in range(int(instructions[1])):
                head.move(direction)
                x_dist, y_dist = head.distance_to(tail)
                if abs(x_dist) > 1:
                    if abs(y_dist) == 1:
                        tail.y += (1 * y_dist)
                    tail.x += (1 * (2/x_dist))
                if abs(y_dist) > 1:
                    if abs(x_dist) == 1:
                        tail.x += (1 * x_dist)
                    tail.y += (1 * (2/y_dist))
                places_visited.append(str(tail))

            # Part 2
            for _ in range(int(instructions[1])):
                knots[0].move(direction)
                prev_knot = knots[0]
                for i, knot in enumerate(knots):
                    x_dist, y_dist = prev_knot.distance_to(knot)
                    if abs(x_dist) > 1:
                        if abs(y_dist) == 1:
                            knot.y += (1 * y_dist)
                        knot.x += (1 * (2/x_dist))
                    if abs(y_dist) > 1:
                        if abs(x_dist) == 1:
                            knot.x += (1 * x_dist)
                        knot.y += (1 * (2/y_dist))
                    if i == 9:
                        part_2_visited.append(str(knot))
                    prev_knot = knot

        print(f'Visited: {len(set(places_visited))}')
        print(f'Visited: {len(set(part_2_visited))}')




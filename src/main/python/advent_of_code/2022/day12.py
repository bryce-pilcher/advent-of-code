from __future__ import annotations
import random
from typing import List

from utils import get_file


class Point:
    x: int
    y: int
    char: str
    direction: str
    neighbors: List[Point]
    visited: bool
    distance: int

    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char
        self.direction = '>'
        self.neighbors = []
        self.visited = False
        self.distance = 0

    def ord(self):
        return ord(self.char)

    def add_neighbor(self, other: Point) -> Point:
        if other.char == 'E' and (self.char != 'z' and self.char != 'y'):
            return self
        if self.char == 'E':
            return self
        self.neighbors.append(other)
        return self

    def __str__(self):
        return f'{self.x},{self.y}'

    def __lt__(self, other: Point):
        return self.distance < other.distance


class Path:
    visited: List
    current: Point
    complete = False
    steps = 0
    path: List

    def __init__(self, init_point):
        self.current = init_point
        self.visited = [init_point]
        self.path = [init_point]

    def copy(self, point):
        p = Path(point)
        p.visited = self.visited.copy()
        p.visited.append(point)
        return p

    def move_to(self, point: Point):
        self.current = point
        self.visited.append(point)
        self.path.append(point)

    def backtrack(self):
        self.path.pop()
        self.current = self.path[-1]

    def short_cut(self, point):
        index = self.path.index(point)
        self.path = self.path[:index+1]
        self.path.append(self.current)


directions = {
    'right': lambda p: (p.x+1, p.y),
    'down': lambda p: (p.x, p.y+1),
    'up': lambda p: (p.x, p.y-1),
    'left': lambda p: (p.x-1, p.y),
}

arrow = {
    'right': '>',
    'down': 'v',
    'up': '^',
    'left': '<',
}


def average(list: List[Point], name, char_ord):
    list = [point for row in list for point in row]
    if len(list) > 0:
        ords = [point.ord() for point in list if point.ord() - char_ord == 1]
        if len(ords) > 0:
            total = sum(ords)/len(ords)
            return total, name
    return 0, name


def get_location_avg_points(position: Point, grid, location_averages):
    next_char = chr(position.ord()+1) if position.char != 'z' else 'E'
    la_x = location_averages[next_char][0]
    la_y = location_averages[next_char][1]
    x = position.x - la_x
    y = position.y - la_y

    max_val = max(abs(x), abs(y))

    directions_vals = []

    for i in range(len(directions)):
        if max_val == abs(x):
            if x >= 0:
                directions_vals.append('left')
                x = -1
            else:
                directions_vals.append('right')
                x = 1
            max_val = 0
        else:
            if y >= 0:
                directions_vals.append('up')
                y = -1
            else:
                directions_vals.append('down')
                y = 1
            max_val = abs(x)

    points = []
    for direction in directions_vals:
        new_tuple = directions[direction](position)
        if 0 <= new_tuple[0] < len(grid[0]) and 0 <= new_tuple[1] < len(grid):
            new_pos = grid[new_tuple[1]][new_tuple[0]]
            points.append(new_pos)
    return points


def get_gradient_points(position, grid, reverse = True, adj = 80):

    x_adj = adj
    y_adj = int(x_adj/2)

    right_avg = average([grid[i][position.x+1:position.x+x_adj] for i in range(len(grid))], 'right', position.ord())
    left_avg = average([grid[i][position.x-x_adj:position.x] for i in range(len(grid))], 'left', position.ord())
    up_avg = average([grid[i][position.x-y_adj:position.x+y_adj] for i in range(position.y)], 'up', position.ord())
    down_avg = average([grid[i][position.x-y_adj:position.x+y_adj] for i in range(position.y+1, len(grid))], 'down', position.ord())

    gradient = [right_avg, left_avg, up_avg, down_avg]
    gradient.sort(key=lambda x: x[0], reverse=reverse)

    points = []
    while len(gradient) > 0:
        direction = gradient.pop(0)[1]
        new_tuple = directions[direction](position)
        if 0 <= new_tuple[0] < len(grid[0]) and 0 <= new_tuple[1] < len(grid):
            new_pos = grid[new_tuple[1]][new_tuple[0]]
            points.append(new_pos)
    return points


def get_points(position, grid):
    points = []
    for direction in directions.keys():
        new_tuple = directions[direction](position)
        if 0 <= new_tuple[0] < len(grid[0]) and 0 <= new_tuple[1] < len(grid):
            new_pos = grid[new_tuple[1]][new_tuple[0]]
            points.append(new_pos)
    return points


def bfs(grid, start_x, start_y):
    search_queue = [grid[start_y][start_x]]
    while len(search_queue) > 0:
        head = search_queue.pop(0)
        head.visited = True

        for neighbor in head.neighbors:
            if not neighbor.visited:
                search_queue.append(neighbor)
                neighbor.distance = head.distance + 1

    print('\n'.join([' '.join([str(col.distance) for col in row]) for row in grid]))


def dijkstra(grid, start_x, start_y):
    from heapq import heappush, heappop, heapify
    h = []
    for row in grid:
        for col in row:
            col.distance = 100000
    start = grid[start_y][start_x]
    start.distance = 0
    for row in grid:
        for col in row:
            heappush(h, col)

    while len(h) > 0:
        current = heappop(h)
        current.visited = True
        for neighbor in current.neighbors:
            new_len = current.distance + 1
            if new_len < neighbor.distance and not neighbor.visited:
                neighbor.distance = new_len
                heapify(h)

    print('\n'.join([' '.join([str(col.distance) for col in row]) for row in grid]))


if __name__ == '__main__':
    with get_file('day12.txt') as input:
        lines = input.readlines()
        grid = []
        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 0
        locations = {}
        location_avgs = {}
        for y, line in enumerate(lines):
            cleaned_line = line.strip()
            if 'S' in cleaned_line:
                start_x = cleaned_line.index('S')
                start_y = y
            if 'E' in cleaned_line:
                end_x = cleaned_line.index('E')
                end_y = y

            chars = [Point(x, y, l) for x, l in enumerate(cleaned_line)]
            for point in chars:
                if point.char not in locations:
                    locations[point.char] = []
                locations[point.char].append(point)
            grid.append(chars)

        import networkx as nx
        G = nx.DiGraph()

        for row in grid:
            G.add_nodes_from(row)

        def add_edge(u: Point, v: Point):
            if v.char == 'E' and (u.char != 'z' and u.char != 'y'):
                return
            if u.char == 'E':
                return
            G.add_edge(u, v)

        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                current = row[j]
                if current.char == 'S':
                    current.char = 'a'
                if j + 1 < len(row):
                    right = row[j+1]
                    if right.ord() - current.ord() <= 1:
                        add_edge(current, right)
                        current.add_neighbor(right)
                if i + 1 < len(grid):
                    below = grid[i+1][j]
                    if below.ord() - current.ord() <= 1:
                        add_edge(current, below)
                        current.add_neighbor(below)
                if i - 1 >= 0:
                    above = grid[i-1][j]
                    if above.ord() - current.ord() <= 1:
                        add_edge(current, above)
                        current.add_neighbor(above)
                if j - 1 >= 0:
                    left = row[j-1]
                    if left.ord() - current.ord() <= 1:
                        add_edge(current, left)
                        current.add_neighbor(left)

        # bfs(grid, start_x, start_y)
        dijkstra(grid, start_x, start_y)
        end = grid[end_y][end_x]
        print(f'{end.char}: {end.distance}')

        a_starts = []
        for row in grid:
            a_starts.append(row[0])

        for a in a_starts:
            distance, path = nx.single_source_dijkstra(G, a, grid[end_y][end_x], weight=lambda x,y,z: 1)
            print(distance)


        for char, points in locations.items():
            x_coords = [point.x for point in points]
            y_coords = [point.y for point in points]

            avg_x = sum(x_coords)/len(x_coords)
            avg_y = sum(y_coords)/len(y_coords)
            location_avgs[char] = avg_x, avg_y

        for loop in range(1):
            path = Path(grid[start_y][start_x])
            start = path.current
            start.char = 'a'
            position = path.current
            val = path.current.char
            while val != 'E':
                moves = []
                rand = 0
                new_positions = get_gradient_points(position, grid, adj=58)
                #new_positions = get_location_avg_points(position, grid, location_avgs)
                #new_positions = get_points(position, grid)
                for new_pos in new_positions:
                    if new_pos.ord() - position.ord() < 2:
                        if new_pos.char == 'E' and position.char != 'z':
                            continue
                        moves.append(new_pos)
                while len(moves) > 0:
                    moves.sort(key=lambda x: x.ord(), reverse=True)
                    next_pos = moves.pop(0)
                    if next_pos not in path.visited:
                        path.move_to(next_pos)
                        position = next_pos
                        val = position.char
                        break
                if position == start:
                    path.backtrack()
                    position = path.current
                    start = path.current
                else:
                    start = position

            print('\n'.join([' '.join([col.char if col not in path.path else '-' for col in row]) for row in grid]))
            print()
            path.path.reverse()
            run = len(path.path) - 2
            idx = 2
            while run > 0:
                position = path.path[idx]
                neighbors = get_points(position, grid)
                neighbors.sort(key=lambda x: path.path.index(x) if x in path.path else 0, reverse=True)
                for next_pos in neighbors:
                    if next_pos in path.path[idx+2:] and (position.ord() - next_pos.ord() <= 1):
                        new_idx = path.path.index(next_pos)
                        new_path = path.path[:idx+1]
                        new_path.extend(path.path[new_idx:])
                        path.path = new_path
                        run -= (new_idx - idx)
                        idx = new_path.index(next_pos)
                if path.path.index(position) == idx:
                    idx += 1
                    run -= 1

            print('\n'.join([' '.join([col.char if col not in path.path else '-' for col in row]) for row in grid]))

            print(f'Round {loop}: {len(path.path)}')

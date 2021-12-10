from __future__ import annotations
from typing import List

class Location:
    def __init__(self, val):
        self.val = val
        self.visited = False

    def __eq__(self, other: Location):
        return self.val == other.val

    def __ge__(self, other):
        return self.val >= other.val

    def __bool__(self):
        return self.visited

    def __add__(self, other):
        return self.val + other

    def visit(self):
        self.visited = True


def find_basin(x, y, grid: List[List[Location]]):
    if x >= len(grid[0]) or y >= len(grid) or x < 0 or y < 0 or grid[y][x].val == 9 or grid[y][x]:
        return 0
    else:
        grid[y][x].visit()
        return 1 + find_basin(x, y+1, grid) + find_basin(x, y-1, grid) + \
               find_basin(x+1, y, grid) + find_basin(x-1, y, grid)


def run(file_path: str):
    with open(file_path, 'r') as file:
        grid = []
        lines = file.readlines()
        for line in lines:
            line = line.replace('\n', '')
            l = [Location(int(v)) for v in list(line)]
            grid.append(l)

        low_places = []
        basins = []
        x = len(grid[0])
        y = len(grid)
        for i in range(y):
            for j in range(x):
                curr_loc_val = grid[i][j]
                if i > 0:
                    if curr_loc_val >= grid[i-1][j]:
                        continue
                if i < y-1:
                    if curr_loc_val >= grid[i+1][j]:
                        continue
                if j > 0:
                    if curr_loc_val >= grid[i][j-1]:
                        continue
                if j < x - 1:
                    if curr_loc_val >= grid[i][j+1]:
                        continue
                low_places.append(curr_loc_val)
                basins.append(find_basin(j,i, grid))

    tot = 0
    for low in low_places:
        tot = tot + low.val + 1
    basins.sort()
    b_tot = 1
    for basin in basins[-3:]:
        b_tot *= basin
    print(tot)
    print(b_tot)






short_file = './resources/day9_short.txt'

long_file = './resources/day9_long.txt'

if __name__ == '__main__':
    run(long_file)
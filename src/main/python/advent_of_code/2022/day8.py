from utils import get_file
from typing import List


class Tree:

    visited: bool
    height: int

    def __init__(self, height: str):
        self.height = int(height)
        self.visited = False

    def was_visited(self):
        return self.visited

    def __str__(self):
        return f'{self.visited}: {self.height}'


def walk_row(row:List[Tree], reverse = False):
    ret = 0
    if reverse:
        row.reverse()
    tallest = row[0].height
    for i in range(1, len(row)-1):
        if row[i].height > tallest:
            tallest = row[i].height
            if not row[i].was_visited():
                row[i].visited = True
                ret += 1
    if reverse:
        row.reverse()
    return ret


def find_tallest(grid, count):
    ret = 0
    for i in range(1, len(grid)-1):
        ret += walk_row(grid[i])
        ret += walk_row(grid[i], reverse=True)

    return ret


if __name__ == '__main__':
    with get_file('day8.txt') as input:
        lines = input.readlines()

        grid = []

        for line in lines:
            cleaned_line = line.strip()
            grid.append([Tree(v) for v in cleaned_line])

        width = len(grid[0])
        length = len(grid)

        grid_edge = (width * 2) + (2*(length - 2))

        search = 0

        if width % 2 == 0:
            search = int(width/2)
        else:
            search = int(width/2 + 1)

        total_viewable = grid_edge

        total_viewable += find_tallest(grid, total_viewable)

        rotated_grid = list(map(list, zip(*grid)))

        total_viewable += find_tallest(rotated_grid, total_viewable)

        print(f'Total: {total_viewable}')

        most_scenic = 0

        for row_idx, row in enumerate(grid):
            if row_idx == 0 or row_idx == len(grid) - 1:
                continue
            for i, tree in enumerate(row):
                if i == 0 or i == len(row) - 1:
                    continue
                ret = 1
                loc = i + 1
                num_to_see = 1
                while loc < len(row) - 1:
                    if tree.height > row[loc].height:
                        num_to_see += 1
                    else:
                        break
                    loc += 1
                ret = ret * num_to_see
                loc = i - 1
                num_to_see = 1
                while loc >= 1:
                    if tree.height > row[loc].height:
                        num_to_see += 1
                    else:
                        break
                    loc -= 1
                ret = ret * num_to_see
                loc = row_idx + 1
                num_to_see = 1
                while loc < len(grid) - 1:
                    if tree.height > grid[loc][i].height:
                        num_to_see += 1
                    else:
                        break
                    loc += 1
                ret = ret * num_to_see
                loc = row_idx - 1
                num_to_see = 1
                while loc >= 1:
                    if tree.height > grid[loc][i].height:
                        num_to_see += 1
                    else:
                        break
                    loc -= 1
                ret = ret * num_to_see
                if ret > most_scenic:
                    most_scenic = ret

        print(f'Most Scenic: {most_scenic}')








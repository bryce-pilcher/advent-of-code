from utils import get_file


class Point:
    x: int
    y: int
    char: str

    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char


if __name__ == "__main__":
    with get_file("day14.txt") as input_file:
        lines = input_file.readlines()

        cleaned_lines = [line.strip() for line in lines]

        processed_lines = []

        grid = {}
        rock = []

        for line in cleaned_lines:
            if line in processed_lines:
                continue
            processed_lines.append(line)
            commands = line.split(' -> ')
            for i in range(len(commands)-1):
                first = [int(c) for c in commands[i].split(',')]
                second = [int(c) for c in commands[i+1].split(',')]
                if first[0] == second [0]:
                    if first[1] > second[1]:
                        y_2 = first[1]
                        y_1 = second[1]
                    else:
                        y_1 = first[1]
                        y_2 = second[1]

                    for i in range(y_1, y_2+1):
                        grid[(first[0], i)] = '#'
                        rock.append(Point(first[0], i, '#'))
                else:
                    if first[0] > second[0]:
                        x_2 = first[0]
                        x_1 = second[0]
                    else:
                        x_1 = first[0]
                        x_2 = second[0]

                    for i in range(x_1, x_2 + 1):
                        grid[(i, first[1])] = '#'
                        rock.append(Point(i, first[1], '#'))

        rock.sort(key=lambda x: x.x)
        min_x = rock[0].x
        max_x = rock[-1].x
        rock.sort(key=lambda x: x.y)
        min_y = rock[0].y
        max_y = rock[-1].y

        rock.sort(key=lambda x: (x.x, x.y))

        for i in range(min_x-1000, max_x + 1000): # Do this for part 2
            grid[(i, max_y+2)] = '#'

        fell_off = False

        count_sand = 0

        while not fell_off:
            start_x = 500
            start_y = 0

            x = start_x
            y = start_y
            count = 0
            loc = (x,y)
            while True:
                x = loc[0]
                y = loc[1]
                down = (x, y+1)
                down_left = (x-1, y +1)
                down_right = (x+1, y+1)
                if down in grid:
                    if down_left not in grid:
                        loc = down_left
                    elif down_right not in grid:
                        loc = down_right
                    else:
                        grid[loc] = 'o'
                        count_sand += 1
                        if loc == (start_x, start_y):
                            fell_off = True
                        break
                else:
                    loc = (x, y + 1)
                    if y + 1 > max_y+2: # changed this for part 2
                        fell_off = True
                        break
        print(count_sand)

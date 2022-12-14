from __future__ import annotations

from utils import get_file


def check_cycle(cycle, cycle_check):
    if cycle == cycle_check:
        strength = (cycle_check * x)
        print(f'{cycle_check}: {strength}: {x} {cleaned_line}')
        return strength
    return None


def check_sprite(cycle, addx):
    if abs(addx - cycle) < 2:
        return True
    else:
        return False


if __name__ == '__main__':
    with get_file('day10.txt') as input:
        lines = input.readlines()

        x = 1
        cycle = 1
        cycle_check = 20
        power = 0
        grid = []
        row = []
        sprite_check = 40
        for line in lines:
            cleaned_line = line.strip()
            instructions = line.split(' ')
            cycles = 1
            if instructions[0] == 'addx':
                cycles = 2
            for i in range(cycles):
                cc = check_cycle(cycle, cycle_check)
                if check_sprite((cycle-1) % 40, x):
                    row.append('#')
                else:
                    row.append('.')
                if cycle == sprite_check:
                    sprite_check += 40
                    grid.append(row)
                    row = []
                if cc:
                    cycle_check += 40
                    power += cc
                cycle += 1
            if instructions[0] == 'addx':
                x += int(instructions[1])

        print(power)
        for row in grid:
            print(''.join(row))



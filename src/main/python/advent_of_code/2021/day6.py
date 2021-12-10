def new_fish(days_left):
    tot = 0
    while days_left >= 0:
        tot += 1
        days_left -= 7
        tot += new_fish(days_left-2)
    return tot


def run(file_path: str, days):
    with open(file_path, 'r') as file:
        values = [int(val) for line in file.readlines() for val in line.split(',')]
        tot = len(values)
        for value in values:
            tot += new_fish((days)-(value+1))

        print(tot)


short_file = './resources/day6_short.txt'

long_file = './resources/day6_long.txt'

if __name__ == '__main__':
    run(short_file, 18)
    run(long_file, 80)
    #run(long_file, 256)
def run(file_path: str, days_to_compute):
    with open(file_path, 'r') as file:
        values = [int(val) for line in file.readlines() for val in line.split(',')]
        tot = len(values)
        days = [0 for i in range(9)]
        for value in values:
            days[value] += 1
        for i in range(days_to_compute):
            first = days.pop(0)
            days[6] += first
            days.append(first)

        sum = 0
        for day in days:
            sum += day
        print(days)
        print(sum)


short_file = './resources/day6_short.txt'

long_file = './resources/day6_long.txt'

if __name__ == '__main__':
    run(long_file, 18)
    run(long_file, 80)
    run(long_file, 256)
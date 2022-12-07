import os
from utils import get_file


if __name__ == '__main__':
    with get_file('day1.txt') as input:
        lines = input.readlines()
        total = 0
        counts = []
        most = 0
        for line in lines:
            if line == '\n':
                if total > most:
                    most = total
                counts.append(total)
                total = 0
            else:
                total += int(line)
        print(most)
        counts.sort(reverse=True)
        top_three = 0
        for cal in counts[:3]:
            top_three += cal
        print(top_three)
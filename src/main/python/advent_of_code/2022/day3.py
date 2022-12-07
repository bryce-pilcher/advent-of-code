from utils import get_file


def get_priority(char) -> int:
    if overlap.isupper():
        priority = ord(overlap) + 1 - ord('A') + 26
    else:
        priority = ord(overlap) + 1 - ord('a')
    return priority


if __name__ == '__main__':
    with get_file('day3.txt') as input:
        total = 0
        lines = input.readlines()
        groupings = []
        group = []
        for i, line in enumerate(lines):
            line = line.replace('\r\n', '')
            total_item_count = len(line)
            split = int(total_item_count / 2)
            overlap: str = list(set(line[:split]).intersection(set(line[split:])))[0]

            total += get_priority(overlap)
            group.append(line)
            if (i+1) % 3 == 0:
                groupings.append(group)
                group = []

        group_total = 0
        for g in groupings:
            overlap = list(set(g[0]).intersection(g[1]).intersection(g[2]))[0]
            group_total += get_priority(overlap)

        print(total)
        print(group_total)

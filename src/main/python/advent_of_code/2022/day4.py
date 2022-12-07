from utils import get_file


if __name__ == '__main__':
    with get_file('day4.txt') as input:
        lines = input.readlines()

        fully_contains = 0
        overlap = 0
        for line in lines:
            assigments = line.replace('\r\n', '').split(',')
            elf1 = [int(a) for a in assigments[0].split('-')]
            elf2 = [int(a) for a in assigments[1].split('-')]

            if elf1[0] < elf2[0]:
                if elf1[1] >= elf2[1]:
                    fully_contains += 1
            elif elf2[1] >= elf1[1]:
                fully_contains += 1
            elif elf1[0] == elf2[0]:
                fully_contains += 1

            if elf1[0] < elf2[0]:
                if elf1[1] >= elf2[0]:
                    overlap += 1
            elif elf2[1] >= elf1[0]:
                overlap += 1
            elif elf1[0] == elf2[0]:
                overlap += 1

        print(fully_contains)
        print(overlap)

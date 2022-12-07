from utils import get_file


if __name__ == '__main__':
    with get_file('day6.txt') as input:
        lines = input.readlines()

        for line in lines:
            position = 1
            last_four_characters = []
            for char in line:
                if len(last_four_characters) == 14:
                    last_four_characters.pop(0)
                last_four_characters.append(char)

                if len(set(last_four_characters)) == 14:
                    break

                position += 1

            print(position)





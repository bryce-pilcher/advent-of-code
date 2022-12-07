from typing import List

from utils import get_file

rps = ['a', 'b', 'c']


def rotate(to_char):
    while True:
        if rps[0] == to_char:
            return
        rps.append(rps.pop(0))


if __name__ == "__main__":
    score_method = {'a': 1, 'b': 2, 'c': 3}
    a = ord('a')
    x = ord('x')
    score = 0
    decrypt_score = 0

    with get_file("day2.txt") as input:
        lines = input.readlines()
        for line in lines:
            play: List[str] = line.replace('\r\n', '').split(" ")
            opponent = play[0].lower()
            you_decrypt = play[1].lower()
            you = chr(a + (ord(you_decrypt) - x))  # convert to a, b, c
            score += score_method[you]
            rotate(opponent)  # rotate list so that opponents move is first.
            your_place = rps.index(you)
            if opponent == you:
                score += 3
            elif your_place == 1:
                score += 6

            move = ''
            match you_decrypt:
                case 'x':
                    move = rps[2]
                case 'y':
                    move = rps[0]
                    decrypt_score += 3
                case 'z':
                    move = rps[1]
                    decrypt_score += 6
            decrypt_score += score_method[move]

        print(f'First method: {score}')
        print(f'Second method: {decrypt_score}')

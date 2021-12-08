import math
import re


class Board:
    def __init__(self, board_size = 5):
        self.board = []
        self.board_size = board_size
        self.marked_numbers = []
        self.rows = [0 for i in range(board_size)]
        self.cols = [0 for i in range(board_size)]
        self.solved: bool = False

    def add_row(self, row):
        self.board.extend(row)

    def change_board_size(self, board_size):
        self.board_size = board_size
        self.rows = [0 for i in range(board_size)]
        self.cols = [0 for i in range(board_size)]

    def mark_number(self, number):
        if number in self.board:
            i = self.board.index(number)
            row = math.floor(i / self.board_size)
            col = i % self.board_size
            self.marked_numbers.append(number)
            self.rows[row] += 1
            self.cols[col] += 1
            if self.rows[row] == self.board_size or self.cols[col] == self.board_size:
                return True
        return False

    def __str__(self):
        return ' '.join(self.board)

    def calc_score(self, number):
        sum = 0
        for num in self.board:
            if num not in self.marked_numbers:
                sum += int(num)
        return int(number) * sum



def run(file_path: str, board_size):
    with open(file_path, 'r') as file:
        numbers = file.readline().replace('\n', '').split(',')
        file.readline()
        boards = []
        lines = file.readlines()
        b = Board(board_size)
        for line in lines:
            if line == '\n':
                boards.append(b)
                size = b.board_size
                b = Board(size)
                continue
            line = line.replace('\n', '').strip()
            b.add_row(re.split('\s+', line))
        boards.append(b)

        solved = False
        for number in numbers:
            boards_to_pop = []
            for i, board in enumerate(boards):
                if board.mark_number(number):
                    if not solved:
                        print(board)
                        print(number)
                        print(board.calc_score(number))
                        solved = True
                    elif len(boards) == 1:
                        print(board)
                        print(number)
                        print(board.calc_score(number))
                    boards_to_pop.append(i)
            boards_to_pop.sort()
            for i, idx in enumerate(boards_to_pop):
                boards.pop(idx-i)




short_file = './resources/day4_short.txt'

long_file = './resources/day4_long.txt'

if __name__ == '__main__':
    run(long_file, 5)
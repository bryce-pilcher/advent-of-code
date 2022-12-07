import math

syntax_score_lk = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

auto_score_lk = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

opposite = {
    '>': '<',
    ')': '(',
    '}': '{',
    ']': '['
}


def run(file_path: str):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        syntax_score = 0
        auto_scores = []
        for line in lines:
            auto_score = 0
            stack = []
            corrupt = False
            list_of_chars = list(line.replace('\n', ''))
            for char in list_of_chars:
                if char in ['[', '{', '(', '<']:
                    stack.append(char)
                else:
                    if stack[-1] == opposite[char]:
                        stack.pop()
                    else:
                        syntax_score += syntax_score_lk[char]
                        corrupt = True
                        break
            if not corrupt and len(stack) != 0:
                while len(stack) > 0:
                    auto_score *= 5
                    auto_score += auto_score_lk[stack.pop()]
            auto_scores.append(auto_score)
        sorted_scores = [score for score in auto_scores if score > 0]
        sorted_scores.sort()
        print(sorted_scores[math.floor(len(sorted_scores)/2)])
        print(syntax_score)




short_file = './resources/day10_short.txt'

long_file = './resources/day10_long.txt'

if __name__ == '__main__':
    run(short_file)
    run(long_file)
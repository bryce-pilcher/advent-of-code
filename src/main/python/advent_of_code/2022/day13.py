from typing import List

from functools import cmp_to_key

from utils import get_file


def compare(left, right):
    if isinstance(left, type(right)):
        if isinstance(left, List):
            smaller = compare_list(left, right)
        else:
            smaller = left - right
    else:
        if isinstance(left, int):
            smaller = compare_list([left], right)
        else:
            smaller = compare_list(left, [right])
    return smaller


def compare_list(left: List, right: List):
    iterations = max(len(left), len(right))
    smaller = 0
    for i in range(iterations):
        if i < len(left):
            lv = left[i]
        else:
            return -1
        if i < len(right):
            rv = right[i]
        else:
            return 1

        smaller = compare(lv, rv)
        if smaller != 0:
            return smaller
    return smaller


if __name__ == '__main__':
    with get_file('day13.txt') as input:
        lines = input.readlines()

        input_pairs = []

        left = ''
        right = ''
        for line in lines:
            cleaned_line = line.strip()
            if cleaned_line == '':
                input_pairs.append((left, right))
                left = ''
                right = ''
                continue
            elif left != '':
                right = eval(cleaned_line)
            else:
                left = eval(cleaned_line)
        input_pairs.append((left,right))

        sum = 0
        for idx, pair in enumerate(input_pairs):
            left = pair[0]
            right = pair[1]
            in_order = compare(left, right)
            if in_order < 1:
                sum += (idx+1)

        print(sum)

        list = [i for pair in input_pairs for i in pair]
        list.append([[2]])
        list.append([[6]])
        list.sort(key=cmp_to_key(compare))

        decoder_2 = list.index([[2]]) + 1
        decoder_6 = list.index([[6]]) + 1

        print(decoder_2 * decoder_6)

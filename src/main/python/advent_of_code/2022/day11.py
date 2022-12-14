from __future__ import annotations

import decimal
import math
from typing import Callable, List

item_id = 1


class Item:
    id: int
    val: int
    orig_val: int
    reductions: int
    se: int
    digits: int

    def __init__(self, val: int):
        self.val = val
        self.orig_val = val
        global item_id
        self.id = item_id
        item_id += 1
        self.reductions = 0
        self.se = 0
        self.path = []

    def copy_with_val(self, val):
        i = Item(val)
        i.id = self.id
        i.orig_val = self.orig_val
        i.path = self.path
        i.reductions = self.reductions
        i.se = self.reductions
        i.digits = self.digits
        return i


class Monkey:
    items: List[Item]
    operation: Callable[[int, int], int]
    test_val: int
    test_true: int
    test_false: int
    inspections: int
    orig_op_val: int

    def __init__(self, id: int, items: List[int], operation: Callable[[int, int], int], op_val, test_val: int, test_true: int, test_false: int):
        self.id = id
        # self.items = [Item(Decimal(str(i))) for i in items]
        self.items = [Item(i) for i in items]
        self.operation = operation
        self.op_val = op_val
        self.orig_op_val = op_val
        self.test_val = test_val
        self.test_true = test_true
        self.test_false = test_false
        self.inspections = 0

    def _test_value(self, value, monkeys, monkey_vals):
        for i, monkey in enumerate(monkeys):
            if value % monkey.test_val == monkey_vals[i]:
                continue
            else:
                return False
        return True

    def calc_mod(self, value):
        mod_val = value % self.test_val
        return (mod_val**2) % self.test_val

    def inspect(self, monkeys: List[Monkey], reduce_worry, worry):
        for item in self.items:
            self.inspections += 1

            calc_val = self.operation(item.val, self.op_val)

            val = calc_val

            if reduce_worry:
                val = math.floor(val/3)
            if not reduce_worry:
                val = val % worry

            to_monkey = self.test_false
            if self.id == 3:
                mod_val = self.calc_mod(item.val)
            else:
                mod_val = val % self.test_val
            if mod_val == 0:
                to_monkey = self.test_true

            #print(f'Monkey {self.id} looks at Item {item.id} {mod_val == 0}: {calc_val} % {self.test_val} = {mod_val} -> {val}')
            item.val = val
            monkeys[to_monkey].items.append(item)
        self.items = []


def add(num: int, by):
    val = num + by

    return val


def multiply(num, by):
    num *= by

    return num

short_monkeys = [
    Monkey(0, [79,98], lambda x, y: x*19, 19, 23,  2, 3),
    Monkey(1, [54, 65, 75, 74], add, 6, 19,  2, 0),
    Monkey(2, [79, 60, 97], lambda x, y: x**2, 2, 13,  1, 3),
    Monkey(3, [74], add, 3, 17,  0, 1)
]

monkeys = [
    Monkey(0, [89, 95, 92, 64, 87, 68], lambda x, y: x * 11, 11, 2, 7, 4),
    Monkey(1, [87, 67], add, 1, 13, 3, 6),
    Monkey(2, [95, 79, 92, 82, 60], add, 6, 3,  1, 6),
    Monkey(3, [67, 97, 56], lambda x,y: x**2, 2, 17,  7, 0),
    Monkey(4, [80, 68, 87, 94, 61, 59, 50, 68], lambda x,y: x * 7, 7, 19, 5, 2),
    Monkey(5, [73, 51, 76, 59], add, 8, 7,  2, 1),
    Monkey(6, [92], add, 5, 11,  3, 0),
    Monkey(7, [99, 76, 78, 76, 79, 90, 89], add, 7, 5, 4, 5)
]


def calculate_monkey_business(rounds: int, debug = False, reduce_worry = True, monkey_list=None):
    if monkey_list is None:
        monkey_list = short_monkeys

    worry = 1
    for monkey in monkeys:
        worry *= monkey.test_val

    for i in range(rounds):
        if debug or (i+1) % 10 == 0:
            print(f'Round {i+1}:')
        for monkey in monkey_list:
            monkey.inspect(monkey_list, reduce_worry=reduce_worry, worry=worry)
        if debug or (i+1) % 10 == 0:
            print('\n'.join([f'Monkey {i} has {", ".join([str(item.id) for item in monkey.items])}' for i, monkey in enumerate(monkey_list)]))
            print('\n'.join([f'Monkey {monkey.id} inspected {monkey.inspections}' for monkey in monkey_list]))

    monkey_list.sort(key=lambda x: x.inspections, reverse=True)
    print(monkey_list[0].inspections*monkey_list[1].inspections)


if __name__ == '__main__':
    #calculate_monkey_business(20, debug=True, monkey_list=monkeys)
    calculate_monkey_business(10000, debug=False, reduce_worry=False, monkey_list=monkeys)

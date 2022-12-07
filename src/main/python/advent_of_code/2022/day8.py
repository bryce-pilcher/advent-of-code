from __future__ import annotations

import os.path
from typing import List
from utils import get_file


class Directory:
    name: str
    parent: Directory
    size: int
    children: List

    def __init__(self, name, parent = None, size = 0):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []


if __name__ == '__main__':
    with get_file('day7.txt') as input:
        lines = input.readlines()
        directories = {}
        cur_dir = Directory('/')
        directories[cur_dir.name] = cur_dir

        for line in lines:
            cleaned_line = line.strip()
            info = cleaned_line.split(' ')
            if info[0] == 'dir':
                name = os.path.join(cur_dir.name, info[1])
                if name not in directories:
                    dir = Directory(name, cur_dir)
                    directories[dir.name] = dir
            elif info[1] == 'cd':
                if info[2] == '..':
                    cur_dir = cur_dir.parent
                else:
                    name = os.path.join(cur_dir.name, info[2])
                    cur_dir = directories[name]
            elif info[1] == 'ls':
                continue
            else:
                size = int(info[0])
                cur_dir.size += size
                cur_dir.children.append(info[1])
                par_dir = cur_dir.parent
                while par_dir:
                    if par_dir:
                        par_dir.size += size
                        par_dir = par_dir.parent

        total_size = 0
        for v in directories.values():
            if v.size <= 100000:
                total_size += v.size

        print(total_size)

        remaining = 70000000 - directories['/'].size
        size_needed = 30000000 - remaining

        val_list = [v.size for v in directories.values()]
        val_list.sort()
        for v in val_list:
            if v > size_needed:
                print(v)
                break




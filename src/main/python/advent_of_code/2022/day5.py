from utils import get_file

start_pos = [
    ['B Q C'],
    ['R Q W Z'],
    ['B M R L V'],
    ['C Z H V T W'],
    ['D Z H B N V G'],
    ['H N P C J F V Q'],
    ['D G T R W Z S'],
    ['C G M N B W Z P'],
    ['N J B M W Q F P']
]

start_pos_2 = [
    ['B Q C'],
    ['R Q W Z'],
    ['B M R L V'],
    ['C Z H V T W'],
    ['D Z H B N V G'],
    ['H N P C J F V Q'],
    ['D G T R W Z S'],
    ['C G M N B W Z P'],
    ['N J B M W Q F P']
]

start_pos = [s[0].split(' ') for s in start_pos]
start_pos_2 = [s[0].split(' ') for s in start_pos_2]

if __name__ == '__main__':
    with get_file('day5.txt') as input:
        lines = input.readlines()

        for line in lines:
            cleaned_line = line.replace('\r\n', '').split(' ')
            num_to_move = int(cleaned_line[1])
            from_idx = int(cleaned_line[3]) - 1
            to_idx = int(cleaned_line[5]) - 1
            start = max(0, len(start_pos_2[from_idx]) - num_to_move)
            tmp = start_pos_2[from_idx][start:]
            start_pos_2[to_idx].extend(tmp)
            for i in range(num_to_move):
                if len(start_pos[from_idx]) == 0:
                    break
                crate = start_pos[from_idx].pop()
                start_pos_2[from_idx].pop()
                start_pos[to_idx].append(crate)

        output = ''
        for s in start_pos:
            output += s[-1]
        print(output)

        output = ''
        for s in start_pos_2:
            output += s[-1]
        print(output)


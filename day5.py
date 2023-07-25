import argparse

from aocd.models import Puzzle


class Crane:
    stacks: list
    moves: list

    def process_move_line(self, line):
        print(f'process move line {line}')
        return

    def process_stack_line(self, line):
        if self.stacks is None:
            cols=int((len(line)+1)/4)
            self.stacks = list(list([None]) * cols)
            for i in range(0,cols):
                self.stacks[i]=list()
        print(f'process stack line {line}')
        self.printStacks()
        idx = 0
        stack_idx = 1
        col = 0
        for char in line:
            if idx % 4 == 1:
                print(f'{char}', end='')
                self.stacks[col].insert(0, char)
                col = col + 1
            idx = idx + 1
        return

    def printStacks(self):
        rows = max(map(len, self.stacks))
        cols = len(self.stacks)
        cur_row = rows - 1
        for col in self.stacks:
            if len(col) >= cur_row:
                print(f' [{col[cur_row]}]', end='')
            else:
                print('    ', end='')

    def __init__(self, lines: list):
        self.stacks = None
        self.moves = None
        process_moves = False
        for line in lines:
            line = line.rstrip('\n')
            if not line:
                print('blank line')
                process_moves = True
                continue

            if process_moves:
                self.process_move_line(line)
            else:
                self.process_stack_line(line)


def part1(input):
    result = 0
    input.printStacks()
    for line in input.moves:
        input.processMove(line)
    return result


def part2(input):
    result = 0
    for line in input:
        line = line.strip()
    return result


parser = argparse.ArgumentParser(description='AOC 2022')
parser.add_argument('-s', action='store_true', help='use the small input file')
parser.add_argument('-p', action='store_true', help='print the input data')
args = parser.parse_args()
puzzle = Puzzle(year=2022, day=5)
if (args.s):
    lines = puzzle.examples[0].input_data.split('\n')
else:
    lines = puzzle.input_data.split('\n')

if (args.p):
    for line in lines:
        print(line, end='\n')

crane = Crane(lines)
part1 = part1(crane)
print(f'part1: {part1}')
part2 = part2(crane)
print(f'part2: {part2}')

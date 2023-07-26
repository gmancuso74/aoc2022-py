import argparse
from Models import Solution
from aocd.models import Puzzle

class Day5(Solution):
    def __init__(self):
        super().__init__(day=5)

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

    def __init__(self):
        self.stacks = None
        self.moves = None
        process_moves = False
        for line in self.input():
            line = line.rstrip('\n')
            if not line:
                print('blank line')
                process_moves = True
                continue

            if process_moves:
                self.process_move_line(line)
            else:
                self.process_stack_line(line)

    def part1(self):
        result = 0
        self.printStacks()
        for line in input.moves:
            self.processMove(line)
        return result

    def part2(self):
        result = 0
        for line in input:
            line = line.strip()
        return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AOC 2022')
    parser.add_argument('-s', action='store_true', help='use the small input file')
    args = parser.parse_args()
    day=Day5()
    if args.s:
        day.useShort=True

    day.printResults()
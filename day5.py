from Models import Solution
from aocd.models import Puzzle


class Day5(Solution):
    
    def __init__(self):
        super().__init__(day=5)
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
        idx = 0
        stack_idx = 1
        col = 0
        for char in line:
            if idx % 4 == 1:
                self.stacks[col].insert(0, char)
                col = col + 1
            idx = idx + 1
        return

    def printStacks(self):
        rows = max(map(len, self.stacks))
        cols = len(self.stacks)
        for row in range(rows-1,-1,-1):
            for col in self.stacks:
                if len(col) >= row:
                    print(f' [{col[row]}]', end='')
                else:
                    print('    ', end='')
            print()
        print("===========================")


    def part1(self):
        result = 0
        input.printStacks()
        for line in input.moves:
            input.processMove(line)
        return result

    def part2(self):
        result = 0
        for line in input:
            line = line.strip()
        return result



if __name__ == '__main__':
    day=Day5()
    day.printResults()

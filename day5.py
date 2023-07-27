from Models import Solution
import re

class Move:
    regex=re.compile(r'move (\d+) from (\d+) to (\d+)')
    moveFrom: int
    moveTo: int
    count: int
    def __init__(self,line):
        matches=Move.regex.match(line)
        if not matches:
            raise Exception (f'No matches found on Move line {line}')
        groups=matches.groups()
        (self.count,self.moveFrom,self.moveTo)=map(int,groups)


class Day5(Solution):
    
    def __init__(self):
        super().__init__(day=5)
        self.stacks = list()
        self.moves = []
        self.load()

    stacks: list[list[str]]
    moves: list

    def load(self):
        self.stacks = list()
        self.moves = []
        process_moves = False
        for line in self.input():
            line = line.rstrip('\n')
            if not line:
                process_moves = True
                continue

            if process_moves:
                self.parse_move_line(line)
            else:
                self.parse_stack_line(line)

    def parse_move_line(self, line):
        move=Move(line)
        self.moves.append(move)
        return

    def parse_stack_line(self, line):
        if len(self.stacks) == 0:
            cols=int((len(line)+1)/4)
            #self.stacks.append(list([]) * cols)
            for i in range(0,cols):
                self.stacks.append(list())
        idx = 0
        stack_idx = 1
        col = 0
        for char in line:
            if idx % 4 == 1:
                if(char!=' '):
                    self.stacks[col].insert(0, char)
                col = col + 1
            idx = idx + 1
        return

    def printStacks(self):
        rows = max(map(len, self.stacks))
        cols = len(self.stacks)
        for row in range(rows-1,-1,-1):
            for col in self.stacks:
                if len(col) > row:
                    print(f' [{col[row]}]', end='')
                else:
                    print('    ', end='')
            print()
        print(f'{len(self.stacks)}===========================')

    def processMove(self,move):
        for i in range(move.count):
            val=self.stacks[move.moveFrom-1].pop()
            self.stacks[move.moveTo-1].append(val)
            #self.printStacks()

    def processMove2(self,move):
            rangeCount=-1*move.count
            subrange=self.stacks[move.moveFrom-1][rangeCount:]
            del self.stacks[move.moveFrom-1][rangeCount:]
            self.stacks[move.moveTo-1].extend(subrange)

    def tops(self):
        result=''
        for col in self.stacks:
            this_char=col[-1]
            if not this_char: raise Exception(f'No Top for column {col}')
            result = result + this_char
        return result

    def part1(self):
        result = ''
        for line in self.moves:
            self.processMove(line)
        return self.tops()

    def part2(self):
        self.load() #reset to input
        result = ''
        for line in self.moves:
            self.processMove2(line)
        return self.tops()

if __name__ == '__main__':
    day=Day5()
    day.printResults()

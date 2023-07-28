from Models import Solution
from enum import Enum

class Type(Enum):
    D = 0
    F = 1

class Node:
    name = str
    type = Type
    children = list
    size = int

    def __init__(self, name: str, type: Type):
        self.name = name
        self.type = type

class Day7(Solution):
    pwd = list[Node]
    root = Node('/',Type.D)

    def __init__(self):
        super().__init__(day=7)
        self.pwd=self.root

    def process(self,line:str):
        if line.startswith('$ ls'):
            print('ignore')
        elif line.startswith('$ cd'):
            print('cd')
        else:
            (left,right)=line.split(' ')
            if(left=='dir'):
                node=Node(right,Type.D)
                

    

    def part1(self):
        for line in self.input():
            print(line)
            self.process(line)
        return 0

    def part2(self):
        return 0


if __name__ == '__main__':
    day = Day7()
    day.printResults()

from Models import Solution
from enum import Enum
from math import copysign
#Vec=tuple[int,int]

class Dir(Enum):
    R=(1,0)
    L=(-1,0)
    U=(0,1)
    D=(0,-1)

def magnitude(input: tuple[int,int])->int:
    return abs(input[0]) if abs(input[0])>abs(input[1]) else abs(input[1])



def distance(first:tuple[int,int],second:tuple[int,int])->tuple[int,int]:
    return (first[0]-second[0],first[1]-second[1])

def get_moves(input:str)->list[tuple[int,int]]:
    (dir_str,cnt_str)=input.split(' ')
    dir=Dir[dir_str]
    cnt=int(cnt_str)
    return [dir.value]*cnt

def apply(p1:tuple[int,int], p2:tuple[int,int])->tuple[int,int]:
    return (p1[0]+p2[0], p1[1]+p2[1])

class Day9(Solution):
    visited:set[tuple[int,int]]
    minx:int
    miny:int
    maxx:int
    maxy:int
    head:tuple[int,int]
    tail:tuple[int,int]

    def __init__(self):
        super().__init__(day=9)
        self.visited=set()
        self.visted=(0,0)
        self.head=(0,0)
        self.tail=(0,0)
        self.minx=0
        self.maxx=5
        self.miny=0
        self.maxy=5

    def check_max(self):
        if(self.minx>self.head[0]): self.minx=self.head[0]
        if(self.maxx<self.head[0]): self.maxx=self.head[0]
        if(self.miny>self.head[1]): self.miny=self.head[1]
        if(self.maxy<self.head[1]): self.maxy=self.head[1]

    def part1_move(self,moves:list[tuple[int,int]]):
        for move in moves:
            self.head = apply(self.head,move)
            self.check_max()  #using head because tail will always be inside of head's bounds
            delta=distance(self.head,self.tail)
            if(magnitude(delta)>1):
                x=int(copysign(1,delta[0])) if delta[0] else 0
                y=int(copysign(1,delta[1])) if delta[1] else 0
                if(x==0): 
                    self.tail=apply(self.tail,(0,y))
                elif(y==0): 
                    self.tail=apply(self.tail,(x,0))
                else:
                    self.tail=apply(self.tail,(x,y))
            self.visited.add(self.tail)
            print(f'Head: {self.head}\tTail: {self.tail}')

    def printGrid(self):
        for y in range(self.maxy,self.miny-1,-1):
            for x in range(self.minx,self.maxx+1):
                cur_pnt=(x,y)
                if(self.head==cur_pnt):
                    print('H',end='')
                elif self.tail==cur_pnt:
                    print('T',end='')
                elif cur_pnt==(0,0):
                    print('s',end='')
                elif self.visited.issuperset(set([cur_pnt])):
                    print('#',end='')
                else:
                    print(f'.',end='')
            print()

    def part1(self):
        for line in self.input():
            print(line)
            self.part1_move(get_moves(line))
            self.printGrid()
        return 0

    def part2(self):
        return 0

if __name__ == '__main__':
    day=Day9()
    day.printResults()

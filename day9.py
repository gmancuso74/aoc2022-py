from Models import Solution
from enum import Enum
from math import copysign

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
    p1Rope:list[tuple[int,int]]
    p2Rope:list[tuple[int,int]]

    def __init__(self):
        super().__init__(day=9)
        self.visited=set()
        self.visited.add((0,0))
        self.visited2=set()
        self.visited2.add((0,0))
        self.p1Rope=[(0,0)]*2
        self.p2Rope=[(0,0)]*10
        self.minx=0
        self.maxx=5
        self.miny=0
        self.maxy=5

    def check_max(self,rope:list[tuple[int,int]]):
        for knot in rope:
            if(self.minx>knot[0]): self.minx=knot[0]
            if(self.maxx<knot[0]): self.maxx=knot[0]
            if(self.miny>knot[1]): self.miny=knot[1]
            if(self.maxy<knot[1]): self.maxy=knot[1]

    def part1_move(self,moves:list[tuple[int,int]]):
        self.do_move(self.p1Rope,moves, self.visited)
        # for move in moves:
        #     self.p1Rope[0] = apply(self.p1Rope[0],move)
        #     self.check_max(self.p1Rope)  #using head because tail will always be inside of head's bounds
        #     delta=distance(self.p1Rope[0],self.p1Rope[1])
        #     if(magnitude(delta)>1):
        #         x=int(copysign(1,delta[0])) if delta[0] else 0
        #         y=int(copysign(1,delta[1])) if delta[1] else 0
        #         if(x==0): 
        #             self.p1Rope[1]=apply(self.p1Rope[1],(0,y))
        #         elif(y==0): 
        #             self.p1Rope[1]=apply(self.p1Rope[1],(x,0))
        #         else:
        #             self.p1Rope[1]=apply(self.p1Rope[1],(x,y))
        #     self.visited.add(self.p1Rope[1])

    def do_move(self,rope:list[tuple[int,int]],moves:list[tuple[int,int]],visited:set[tuple[int,int]]):
        for move in moves:
            rope[0] = apply(rope[0],move)
            for i in range(1,len(rope)):
                delta=distance(rope[i-1],rope[i])
                if(magnitude(delta)>1):
                    x=int(copysign(1,delta[0])) if delta[0] else 0
                    y=int(copysign(1,delta[1])) if delta[1] else 0
                    if(x==0): 
                        rope[i]=apply(rope[i],(0,y))
                    elif(y==0): 
                        rope[i]=apply(rope[i],(x,0))
                    else:
                        rope[i]=apply(rope[i],(x,y))
            visited.add(rope[-1])

    def part2_move(self,moves:list[tuple[int,int]]):
        self.do_move(self.p2Rope,moves, self.visited2)

    def printGrid(self,part:int=1):
        if part==1:
            rope=self.p1Rope
            myvisited=self.visited
        else:
            rope=self.p2Rope
            myvisited=self.visited2

        for y in range(self.maxy,self.miny-1,-1):
            for x in range(self.minx,self.maxx+1):
                cur_pnt=(x,y)
                if(rope[0]==cur_pnt):
                    print('H',end='')
                elif rope[-1]==cur_pnt:
                    print('T',end='')
                elif cur_pnt in rope:
                    print(rope.index(cur_pnt),end='')
                elif cur_pnt==(0,0):
                    print('s',end='')
                elif myvisited.issuperset(set([cur_pnt])):
                    print('#',end='')
                else:
                    print(f'.',end='')
            print()

    def part1(self):
        for line in self.input():
            self.part1_move(get_moves(line))
            # self.printGrid()
        return len(self.visited)

    def part2(self):
        for line in self.input():
            # print(line)
            self.part2_move(get_moves(line))
            # self.printGrid(2)
        return len(self.visited2)

if __name__ == '__main__':
    day=Day9()
    day.printResults()

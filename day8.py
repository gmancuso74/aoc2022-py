from typing import Callable
from Models import Solution
class Node:
    visible:bool|None
    height: int

    def __init__(self,height:int=0):
        visible=None
        self.height=height

class Day8(Solution):
    Grid=list[list[Node]]
    grid: Grid
    visibleCount: int
    def __init__(self):
        super().__init__(day=8)
        self.grid=list[list[Node]]()
        self.visibleCount=0

    def calc_visible(self,row:int,col:int):
        height=self.grid[row][col].height
        (up,down,left,right)=range(4)
        visible=[True,True,True,True]#up down left right
        for _col in range(0,col):
            if(self.grid[row][_col].height>=height):
                visible[left]=False
        if(visible[left]): 
            self.grid[row][col].visible=True
            return
        for _col in range(col+1,len(self.grid[row])):
            if(self.grid[row][_col].height>=height):
                visible[right]=False
        if(visible[right]): 
            self.grid[row][col].visible=True
            return
        for _row in range(0,row):
            if(self.grid[_row][col].height>=height):
                visible[up]=False
        if(visible[up]):
            self.grid[row][col].visible=True
            return
        for _row in range(row+1,len(self.grid[col])):
            if(self.grid[_row][col].height>=height):
                visible[down]=False
        if(visible[down]):
            self.grid[row][col].visible=True
            return
        self.grid[row][col].visible=False
    
    def printVisible(self,row:int,col:int):
        char = 'Y' if self.grid[row][col].visible else 'N'
        tail= '\n' if(col==len(self.grid[row])-1) else ''
        print(f'{char}',end=tail)

    def countVisible(self,row:int,col:int):
        if(self.grid[row][col].visible):
            self.visibleCount=self.visibleCount+1

    def apply(self,func: Callable[[int, int], None]):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                func(row,col)

    def part1(self):
        input=self.input()
        rows=len(input)
        for row in range(rows):
            self.grid.append(list())
            for col in range(len(input[row])):
                self.grid[row].append(Node(int(input[row][col])))
        self.apply(self.calc_visible)
        # self.apply(self.printVisible)
        self.apply(self.countVisible)
        return self.visibleCount

    def part2(self):
        return 0

if __name__ == '__main__':
    day=Day8()
    day.printResults()

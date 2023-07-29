from typing import Callable
from Models import Solution
class Node:
    visible:bool|None
    height: int
    score: int

    def __init__(self,height:int=0):
        visible=None
        self.height=height
        self.score=0

class Day8(Solution):
    Grid=list[list[Node]]
    grid: Grid
    visibleCount: int
    maxScore: int
    def __init__(self):
        super().__init__(day=8)
        self.grid=list[list[Node]]()
        self.visibleCount=0
        self.maxScore=0

    def calc_score(self,row:int,col:int):
        views=[0,0,0,0]
        height=self.grid[row][col].height
        (up,down,left,right)=range(4)
        for _col in range(col-1,-1,-1):
            views[left]+=1
            if(self.grid[row][_col].height>=height):
                break
        for _col in range(col+1,len(self.grid[row])):
            views[right]+=1
            if(self.grid[row][_col].height>=height):
                break
        for _row in range(row-1,-1,-1):
            views[up]+=1
            if(self.grid[_row][col].height>=height):
                break
        for _row in range(row+1,len(self.grid[col])):
            views[down]+=1
            if(self.grid[_row][col].height>=height):
                break
        score=views[up]*views[down]*views[left]*views[right]
        self.grid[row][col].score=score
        if(self.maxScore<score): self.maxScore=score


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
    
    def print_score(self,row:int,col:int):
        tail= '\n' if(col==len(self.grid[row])-1) else ''
        print(f'{self.grid[row][col].score}',end=tail)

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
        self.apply(self.countVisible)
        return self.visibleCount

    def part2(self):
        self.apply(self.calc_score)
        return self.maxScore

if __name__ == '__main__':
    day=Day8()
    day.printResults()

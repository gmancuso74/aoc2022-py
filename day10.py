from Models import Solution
from enum import Enum

class Instruction(Enum):
    NOOP=0
    ADDX=1
    
class Command():
    start: int
    end: int
    instr: Instruction
    val: int
    instr_times={Instruction.NOOP:1,Instruction.ADDX:2}

    def __init__(self,instr:Instruction,val:int,start:int):
        self.start=start
        self.instr=instr
        self.val=val
        self.end=self.start+self.instr_times[instr]

    def exec(self, input:int)->int:
        return input+self.val


class Day10(Solution):
    reg: int
    counter: int
    commands: list[Command]
    cycles: list[int]

    def __init__(self):
        super().__init__(day=10)
        self.reg=1
        self.counter=1
        self.commands=list()
        self.cycles=list()
        for i in range(0,6):
            self.cycles.append(20+40*i)

    def strength_at(self,cycle:int,results:list)->int:
        for tuple in results:
            (cur_cmd,value)=tuple
            if(cur_cmd.end>cycle):
                return value
        raise(Exception("Not found"))

    def load(self,lines):
        for line in lines:
            curCommand=None
            if(line.startswith('noop')):
                curCommand=Command(Instruction.NOOP,0,self.counter)
            else:
                (instr_name,val)=line.split()
                curCommand=Command(Instruction.ADDX,int(val),self.counter)
            self.commands.append(curCommand)
            self.counter=curCommand.end

    def run(self)->list[tuple[Command,int]]:
        result=list()
        next_reg=1
        for curCommand in self.commands:
            self.reg=next_reg
            next_reg=curCommand.exec(self.reg)
            tuple=(curCommand,self.reg)
            result.append(tuple)
        return result

    def do_part1(self,lines):
        self.load(lines)
        result=self.run()
        # for cycle in range(1,221):
        total=0
        for cycle in self.cycles: 
            strength=self.strength_at(cycle,result)
            total=total+(strength*cycle)
        return total
        
    def part1(self):
        return self.do_part1(self.input())

    def part2(self):
        return 0

if __name__ == '__main__':
    day=Day10()
    day.printResults()

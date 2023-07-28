from Models import Solution

class Day6(Solution):

    def __init__(self):
        super().__init__(day=6)

    def do_part1(self,input:list,msg_len:int):
        for line in input:
            for i in range(msg_len,len(line)):
                chars=set(line[i-msg_len:i])# type: ignore
                if len(chars)==msg_len: 
                    return i
        return -1
    
    def part1(self):
        input=self.input()
        return self.do_part1(input,4)    


    def part2(self):
        input=self.input()
        return self.do_part1(input,14)    

if __name__ == '__main__':
    day=Day6()
    if(day.useShort):
        for i in range(0,len(day.puzzle.examples)):
            inputN=day.puzzle.examples[i].input_data.split('\n')
            print(f'Input:{inputN}\tOutput:{day.do_part1(inputN,4)}\t Part2:{day.do_part1(inputN,14)}')
    else:
        day.printResults()

from Models import Solution

class Day7(Solution):

    def __init__(self):
        super().__init__(day=7)

    def part1(self):
        for line in self.input():
            print(line)
        return 0


    def part2(self):
        return 0

if __name__ == '__main__':
    day=Day7()
    day.printResults()

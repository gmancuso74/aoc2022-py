from Models import Solution

class Day1(Solution):

    def __init__(self):
        super().__init__(day=1)

    def part1(self):
        biggest = 0
        current = 0
        for line in self.input():
            line = line.strip()
            if (line.isdecimal()):
                current += int(line)
                if (current > biggest):
                    biggest = current
            else:
                current = 0
        return biggest


    def part2(self):
        elves = []
        current = 0
        for line in self.input():
            line = line.strip()
            if (line.isdecimal()):
                current += int(line)
            else:
                elves.append(current)
                current = 0
        if current != 0:
            elves.append(current)
        elves.sort()
        return sum(elves[-3:])

if __name__ == '__main__':
    day=Day1()
    day.printResults()

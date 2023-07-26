from Models import Solution

class Day4(Solution):

  def __init__(self):
      super().__init__(day=4)


  def part1(self):
      result = 0
      for line in self.input():
          line = line.strip()
          (a, b) = line.split(',')
          l = self.mk_set(a)
          r = self.mk_set(b)
          if (l.issubset(r) or r.issubset(l)):
              result = result + 1
      return result


  def mk_set(self,input):
      (l, r) = input.split('-')
      result = range(int(l), int(r) + 1)
      return set(result)


  def part2(self):
      result = 0
      for line in self.input():
          line = line.strip()
          (a, b) = line.split(',')
          l = self.mk_set(a)
          r = self.mk_set(b)
          if (len(l.intersection(r)) > 0):
              result = result + 1
      return result


if __name__ == '__main__':
    day=Day4()
    day.printResults()

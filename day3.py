import argparse
from Models import Solution
from aocd.models import Puzzle
import string

class Day3(Solution):

  def __init__(self):
      super().__init__(day=3)


  priority={}
  i=1
  for char in string.ascii_lowercase:
    priority[char]=i
    i=i+1

  for char in string.ascii_uppercase:
    priority[char]=i
    i=i+1

  def part1(self):
    result=0
    for line in self.input():
      line=line.strip()
      split=int(len(line)/2)
      left=line[0:split]
      right=line[split:]
      common=set(left) & set(right)
      for char in common:
        result=result+self.priority[char]
    return result


  def part2(self):
    result=0
    cur_row=1;
    #[{a,b,c,d},{b,e,f,g},{h,i,j,b}]
    groups=[]#list< list<set> >
    cur_group=[] #list<set>
    for line in self.input():
      line=line.strip()
      cur_group.append(line)
      if(cur_row%3==0):
        groups.append(cur_group)
        char=list(set.intersection(*map(set,cur_group)))[0]
        result=result+self.priority[char]
        cur_group=[]
      cur_row=cur_row+1
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AOC 2022')
    parser.add_argument('-s', action='store_true', help='use the small input file')
    args = parser.parse_args()
    day=Day3()
    if (args.s):
        day.useShort=True

    day.printResults()

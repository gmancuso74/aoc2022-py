import argparse
from aocd.models import Puzzle

def part1(input):
  biggest=0
  current=0
  for line in input:
    line=line.strip()
    if(line.isdecimal()):
      current+=int(line)
      if(current>biggest):
        biggest=current
    else:
      current=0
  return biggest


def part2(input):
  elves=[]
  current=0
  for line in input:
    line=line.strip()
    if(line.isdecimal()):
      current+=int(line)
    else:
      elves.append(current)
      current=0
  elves.sort()
  return sum(elves[-3:])


parser = argparse.ArgumentParser(description='AOC 2022')
parser.add_argument('-s', action='store_true' , help='use the small input file')
args = parser.parse_args()
puzzle = Puzzle(year=2022, day=1)
if(args.s):
  lines=puzzle.example_data.split('\n')
else:
  lines=puzzle.input_data.split('\n')

biggest=part1(lines)
print(f'part1: {biggest}')
big3=part2(lines)
print(f'part2: {big3}')

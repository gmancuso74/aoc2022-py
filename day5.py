import argparse
from aocd.models import Puzzle

def part1(input):
  result=0
  for line in input:
    line=line.strip()
  return result


def part2(input):
  result=0
  for line in input:
    line=line.strip()
  return result


parser = argparse.ArgumentParser(description='AOC 2022')
parser.add_argument('-s', action='store_true' , help='use the small input file')
parser.add_argument('-p', action='store_true', help='print the input data')
args = parser.parse_args()
puzzle = Puzzle(year=2022, day=5)
if(args.s):
  lines = puzzle.examples[0].input_data.split('\n')
else:
  lines=puzzle.input_data.split('\n')

if(args.p):
  for line in lines:
    print(line, end='\n')

part1=part1(lines)
print(f'part1: {part1}')
part2=part2(lines)
print(f'part2: {part2}')
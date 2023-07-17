import argparse

def part1(filename):
  biggest=0
  with open(filename) as f:
    current=0
    for line in f:
      line=line.strip()
      if(line.isdecimal()):
        current+=int(line)
        if(current>biggest):
          biggest=current
      else:
        current=0
  return biggest


def part2(filename):
  elves=[]
  with open(filename) as f:
      current=0
      for line in f:
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
filename='data/day1'
if(args.s):
  filename=filename+'.small'
biggest=part1(filename)
print(f'biggest: {biggest}')
big3=part2(filename)
print(f'big3: {big3}')

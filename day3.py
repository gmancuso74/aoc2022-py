import argparse
from aocd.models import Puzzle
import string

priority={}
i=1
for char in string.ascii_lowercase:
	priority[char]=i
	i=i+1

for char in string.ascii_uppercase:
	priority[char]=i
	i=i+1

def part1(input):
  result=0
  for line in input:
    line=line.strip()
    split=int(len(line)/2)
    left=line[0:split]
    right=line[split:]
    common=set(left) & set(right)
    for char in common:
    	result=result+priority[char]
  return result


def part2(input):
  result=0
  cur_row=1;
  #[{a,b,c,d},{b,e,f,g},{h,i,j,b}]
  groups=[]#list< list<set> >
  cur_group=[] #list<set>
  for line in input:
    line=line.strip()
    cur_group.append(line)
    if(cur_row%3==0):
    	groups.append(cur_group)
    	char=list(set.intersection(*map(set,cur_group)))[0]
    	result=result+priority[char]
    	cur_group=[]
    cur_row=cur_row+1
  return result

parser = argparse.ArgumentParser(description='AOC 2022')
parser.add_argument('-s', action='store_true' , help='use the small input file')
args = parser.parse_args()
puzzle = Puzzle(year=2022, day=3)
if(args.s):
    lines = puzzle.examples[0].input_data.split('\n')
else:
    lines=puzzle.input_data.split('\n')

part1=part1(lines)
print(f'part1: {part1}')
part2=part2(lines)
print(f'part2: {part2}')

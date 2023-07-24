import argparse
from aocd.models import Puzzle

from enum import Enum
class RPS(Enum):
  Rock = 1
  Paper = 2
  Scissors = 3

def get_score(left,right):
	score=right.value
	match left:
		case RPS.Rock:
			match right:
				case RPS.Rock: return score+3
				case RPS.Paper: return score+6
				case RPS.Scissors: return score
		case RPS.Paper:
			match right:
				case RPS.Rock: return score
				case RPS.Paper: return score+3
				case RPS.Scissors: return score+6
		case RPS.Scissors:
			match right:
				case RPS.Rock: return score+6
				case RPS.Paper: return score+0
				case RPS.Scissors: return score+3

def get_play(value):
	match value:
		case 'X'|'A':
			return RPS.Rock
		case 'Y'|'B':
		  return RPS.Paper
		case 'Z'|'C':
		  return RPS.Scissors

def part1(lines):
	score=0
	current=0
	for line in lines:
		line=line.strip()
		(left,right)=line.split()
		score+=get_score(get_play(left),get_play(right))
	return score		

def get_part2_play(left_play,right):
	match left_play:
		case RPS.Rock:
			match right:
				case 'X': return RPS.Scissors #lose
				case 'Y': return RPS.Rock #draw
				case 'Z': return RPS.Paper #win
		case RPS.Paper:
			match right:
				case 'X': return RPS.Rock
				case 'Y': return RPS.Paper
				case 'Z': return RPS.Scissors
		case RPS.Scissors:
			match right:
				case 'X': return RPS.Paper
				case 'Y': return RPS.Scissors
				case 'Z': return RPS.Rock

def part2(lines):
	score=0
	for line in lines:
		line=line.strip()
		(left,right)=line.split()
		left_play=get_play(left)
		right_play=get_part2_play(left_play,right)
		round_score=get_score(left_play,right_play)
		score+=round_score
	return score

parser = argparse.ArgumentParser(description='AOC 2022')
parser.add_argument('-s', action='store_true' , help='use the small input file')
args = parser.parse_args()
puzzle = Puzzle(year=2022, day=2)
if(args.s):
  lines=puzzle.example_data.split('\n')
else:
  lines=puzzle.input_data.split('\n')

print(f'part1: {part1(lines)}')
print(f'part2: {part2(lines)}')

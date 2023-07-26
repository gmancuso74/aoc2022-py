from Models import Solution

from enum import Enum
class RPS(Enum):
  Rock = 1
  Paper = 2
  Scissors = 3
class Day2(Solution):
	def __init__(self):
		super().__init__(day=2)


	def get_score(self,left,right):
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

	def get_play(self,value):
		match value:
			case 'X'|'A':
				return RPS.Rock
			case 'Y'|'B':
				return RPS.Paper
			case 'Z'|'C':
				return RPS.Scissors

	def part1(self):
		score=0
		current=0
		for line in self.input():
			line=line.strip()
			(left,right)=line.split()
			score+=self.get_score(self.get_play(left),self.get_play(right))
		return score		

	def get_part2_play(self,left_play,right):
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

	def part2(self):
		score=0
		for line in self.input():
			line=line.strip()
			(left,right)=line.split()
			left_play=self.get_play(left)
			right_play=self.get_part2_play(left_play,right)
			round_score=self.get_score(left_play,right_play)
			score+=round_score
		return score


if __name__ == '__main__':
	day=Day2()
	day.printResults()


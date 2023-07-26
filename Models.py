import argparse
from aocd.models import Puzzle

class Solution(object):
	useShort: bool
	args:object

	def __init__(self,day):
		self.day=day
		self.useShort=False
		self.result1=None
		self.result2=None
		self.puzzle=Puzzle(year=2022, day=self.day)
		parser = argparse.ArgumentParser(description='AOC 2022')
		parser.add_argument('-s', action='store_true', help='use the small input file')
		args = parser.parse_args()
		if(args.s): self.useShort=True


	def input(self):
		if self.useShort:
			return self.puzzle.examples[0].input_data.split('\n')
		else:
			return self.puzzle.input_data.split('\n')

	def printResults(self):
		self.result1=str(self.part1())
		self.result2=str(self.part2())
		print(f'Day {self.day}:\t{self.result1}\t{self.result2}')


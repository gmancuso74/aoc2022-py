import argparse
from aocd.models import Puzzle

class Solution(object):
	useShort: bool
	printInput: bool
	args:object
	parser = argparse.ArgumentParser(description='AOC 2022')

	def __init__(self,day):
		self.day=day
		self.useShort=False
		self.printInput=False
		self.result1=None
		self.result2=None
		self.puzzle=Puzzle(year=2022, day=self.day)
		self.parser.add_argument('-short', action='store_true', help='use the small input file')
		self.parser.add_argument('-print', action='store_true', help='print the input')
		self.parser.add_argument('-write', action='store_true', help='Write input file to data/')
		self.args,unknown = self.parser.parse_known_args()
		if(self.args.short): self.useShort=True
		if(self.args.print): self.printInput=True
		if(self.args.write):
			filename=f'data/day{self.day}'
			if not self.args.s:
				with open(filename,'w') as datafile:
					datafile.write(self.puzzle.input_data)
			else:
				i=0
				for example in self.puzzle.examples:
					exampleFile=f'{filename}.small'
					if i>0:exampleFile=f'{exampleFile}.{i}'
					with open(exampleFile,'w') as datafile:
						datafile.write(example.input_data)
					i=i+1


	def input(self):
		if self.useShort:
			return self.puzzle.examples[0].input_data.split('\n')
		else:
			return self.puzzle.input_data.split('\n')

	def printResults(self):
		if(self.printInput):
			for line in self.input(): print(line)
		self.result1=str(self.part1()) # type: ignore
		self.result2=str(self.part2()) # type: ignore
		print(f'Day {self.day}:\t{self.result1}\t{self.result2}')


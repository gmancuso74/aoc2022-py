import argparse

parser = argparse.ArgumentParser(description='AOC solution template builder')
parser.add_argument('day', type=int , help='day number')
args = parser.parse_args()

with open('day.template') as template:
	with(open(f'day{args.day}.py','w')) as newday:
		newday.write(template.read().replace('___DAY___',str(args.day)))
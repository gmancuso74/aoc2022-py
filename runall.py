import subprocess
import argparse
import os.path

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='AOC 2022')
	parser.add_argument('-s', action='store_true', help='use the small input file')
	args = parser.parse_args()
	for i in range(1,26):
		file=f'day{i}.py'
		if(os.path.isfile(file)):
			proc=subprocess.run(["python", file], capture_output=True, encoding='UTF-8')
			if(proc.stderr): print(f'Day{i}:{proc.stderr}')
			print(proc.stdout,end='')

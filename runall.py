import subprocess
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AOC 2022')
    parser.add_argument('-s', action='store_true', help='use the small input file')
    args = parser.parse_args()
    for i in range(1,26):
    	file=f'day{i}.py'
    	proc=subprocess.run(["python", file], capture_output=True, encoding='UTF-8')
    	print(proc.stdout,end='')

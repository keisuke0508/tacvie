import os
import sys

def main():
    os.chdir('connector')
    if len(sys.argv) < 2:
        judge_raw_input()
    elif sys.argv[1] == 's':
        os.system('python sensing.py')
    elif sys.argv[1] == 'a':
        os.system('python actuation.py')
    else:
        judge_raw_input()

def start_func(func):
    if func == 's':
        os.system('python sensing.py')
    elif func == 'a':
        os.system('python actuation.py')
    else:
        judge_raw_input()

def judge_raw_input():
    print "input 's'(sensing) or 'a'(actuation)."
    func = raw_input()
    start_func(func)


if __name__ == '__main__':
    main()

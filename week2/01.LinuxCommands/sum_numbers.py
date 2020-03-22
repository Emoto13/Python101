# generate_numbers.py
import sys

def sum_numbers(filename):
    lst = []
    with open(filename, 'r') as f:
       lst = [int(i) for i in f.readlines()[0].strip().split()]
    return sum(lst) 

def main():
   print(sum_numbers(sys.argv[1]))

if __name__ == '__main__':
    main()
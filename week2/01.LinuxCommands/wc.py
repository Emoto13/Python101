import os
import sys

def count_by_requirement(requirement, filename):
    with open(filename, 'r') as f:
        string = f.read() 
        if requirement == 'lines' :
            return string.count("\n")

        elif requirement == 'chars':
            return len(string)

        elif requirement == 'words': 
            return len(string.split())   


def main():
    requirement = sys.argv[1]
    filename = sys.argv[2]
    print(requirement, filename)
    print(count_by_requirement(requirement, filename))

if __name__ == '__main__':
    main()
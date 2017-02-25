#!/home/hydrius/projects/Tamara/bin/python3

import sys
from Brain import Brain

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    Brain()


if __name__ == '__main__':
    main()


import sys

from . import lib


def usage():
    print("Usage: slice EXPRESSION")

def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    expr = sys.argv[1]

    args = [int(elm) if elm else None for elm in expr.split(':')]

    lib.slice_with_list(args)

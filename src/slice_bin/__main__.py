import itertools
import sys
from typing import Optional, TextIO

from . import lib


def usage():
    print("Usage: slice EXPRESSION")


def main1(inpt: TextIO, start: Optional[int]):
    if start is None:
        raise Exception("Unreachable")

    if lib.is_minus(start):
        itr = lib.tail(inpt, -start)
        print(next(itr), end='')
        return

    lib.consume(inpt, start)
    print(next(inpt), end='')


def main2(inpt: TextIO, start: Optional[int], end: Optional[int]):
    if lib.is_minus(start) or lib.is_minus(end):
        lib.slice_with_list(inpt, [start, end])
        return

    for line in itertools.islice(inpt, start, end):
        print(line, end='')


def main3(inpt: TextIO, start: Optional[int], end: Optional[int], step: Optional[int]):
    if lib.is_minus(start) or lib.is_minus(end) or lib.is_minus(step):
        lib.slice_with_list(inpt, [start, end, step])
        return

    for line in itertools.islice(inpt, start, end, step):
        print(line, end='')


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    expr = sys.argv[1]

    args = [int(elm) if elm else None for elm in expr.split(':')]
    len_args = len(args)

    if len_args == 1:
        main1(sys.stdin, args[0])
    else:
        lib.slice_with_list(sys.stdin, args)

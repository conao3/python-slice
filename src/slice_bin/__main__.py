import itertools
import sys
from typing import Optional, TextIO

from . import lib


def usage():
    print("Usage: slice EXPRESSION")


def main1(inpt: TextIO, args: list[Optional[int]]):
    start = args[0] or 0

    if start < 0:
        itr = lib.tail(inpt, -start)
        print(next(itr), end='')
        return

    lib.consume(inpt, start)
    print(next(inpt), end='')


def main2(inpt: TextIO, args: list[Optional[int]]):
    start = args[0] or 0
    end = args[1] or sys.maxsize

    if start < 0:
        itr = lib.tail(inpt, -start)
        islice_stop = start + end
        if islice_stop < 0:
            return

        for line in itertools.islice(itr, islice_stop):
            print(line, end='')
        return

    if end < 0:
        itr = itertools.islice(inpt, start, None)
        for line in list(itr)[:end]:
            print(line, end='')
        return

    for line in itertools.islice(inpt, start, end):
        print(line, end='')


def main3(inpt: TextIO, args: list[Optional[int]]):
    start = args[0] or 0
    end = args[1] or sys.maxsize
    step = args[2] or 1

    if start < 0 or end < 0 or step < 0:
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
        main1(sys.stdin, args)
    elif len_args == 2:
        main2(sys.stdin, args)
    elif len_args == 3:
        main3(sys.stdin, args)
    else:
        lib.slice_with_list(sys.stdin, args)

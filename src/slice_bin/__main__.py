import itertools
import sys
from typing import Iterator, Optional, TextIO

from . import lib


def usage():
    print("Usage: slice EXPRESSION")


def generator_start_stop(inpt: TextIO, start_: Optional[int], stop_: Optional[int]) -> Iterator[str]:
    start = start_ or 0
    stop = stop_ or sys.maxsize

    if start < 0:
        itr = lib.tail(inpt, -start)
        islice_stop = start + stop
        if islice_stop < 0:
            return iter(())

        return itertools.islice(itr, islice_stop)

    if stop < 0:
        itr = itertools.islice(inpt, start, None)
        return iter(list(itr)[:stop])

    return itertools.islice(inpt, start, stop)


def main1(inpt: TextIO, args: list[Optional[int]]):
    for line in generator_start_stop(inpt, args[0], None):
        print(line, end='')
        return


def main2(inpt: TextIO, args: list[Optional[int]]):
    for line in generator_start_stop(inpt, args[0], args[1]):
        print(line, end='')


def main3(inpt: TextIO, args: list[Optional[int]]):
    start = args[0] or 0
    end = args[1] or sys.maxsize
    step = args[2] or 1

    if step < 0:
        step = -step
        inpt: TextIO = iter(reversed(list(inpt)))

    itr = generator_start_stop(inpt, start, end)
    while (elm := next(itr, None)) is not None:
        print(elm, end='')
        lib.consume(itr, step - 1)


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

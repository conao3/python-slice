
import sys
from typing import Optional


def slice_with_list(args: list[Optional[int]]) -> None:
    len_args = len(args)

    if len_args == 1:
        start, = args
        print(list(sys.stdin)[start], end='')

    elif len_args == 2:
        start, stop = args
        for line in list(sys.stdin)[start:stop]:
            print(line, end='')

    elif len_args == 3:
        start, stop, step = args
        for line in list(sys.stdin)[start:stop:step]:
            print(line, end='')

    else:
        raise Exception("Invalid number of arguments")

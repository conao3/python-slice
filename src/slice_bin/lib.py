from typing import Any, Optional, TextIO
from collections.abc import Generator


def slice_with_list(inpt: TextIO, args: list[Optional[int]]) -> None:
    len_args = len(args)

    if len_args == 1:
        start, = args
        print(list(inpt)[start], end='')

    elif len_args == 2:
        start, stop = args
        for line in list(inpt)[start:stop]:
            print(line, end='')

    elif len_args == 3:
        start, stop, step = args
        for line in list(inpt)[start:stop:step]:
            print(line, end='')

    else:
        raise Exception("Invalid number of arguments")


def consume(iter: Generator[Any, Any, Any], n: int) -> None:
    for _ in range(n):
        next(iter)


def is_minus(n: Optional[int]) -> bool:
    return n is not None and n < 0

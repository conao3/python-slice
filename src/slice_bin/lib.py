import collections
import itertools
import typing
from typing import Any, Optional, TextIO
from collections.abc import Iterator


def slice_with_list(inpt: TextIO, args: list[Optional[int]]) -> None:
    print('slice_with_list')
    len_args = len(args)

    if len_args == 1:
        start, = args
        if start is None:
            raise Exception("Unreachable")

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


def consume(textio: Iterator[Any] | TextIO, n: int) -> None:
    for _ in range(n):
        next(textio, None)


def tail(textio: TextIO, n: int) -> Iterator[str]:
    return iter(collections.deque(textio, maxlen=n))


def nth(iterable, n, default=None):
    return next(itertools.islice(iterable, n, None), default)


def is_minus(n: Optional[int]) -> typing.TypeGuard[int]:
    return n is not None and n < 0


def minus(a: Optional[int], b: Optional[int]) -> Optional[int]:
    if a is None or b is None:
        return None
    return a - b

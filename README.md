# python-slice

## Install

Install `slice-bin` from PyPI, which will install `slice` as a command line tool.

```bash
pip install slice-bin
```

## Usage

Assuming stdin is split on a newline and put into an array,
the output can be filtered by Python's slice notation.


```bash
$ seq 10
1
2
3
4
5
6
7
8
9
10
```

```bash
$ seq 10 | slice 3
4
```

```bash
$ seq 10 | slice 3:
4
5
6
7
8
9
10
```

```bash
$ seq 10 | slice 3:5
4
5
```

```bash
$ seq 10 | slice -3:
8
9
10
```

```bash
$ seq 10 | slice :3
1
2
3
```

```bash
$ seq 10 | slice :-3
1
2
3
4
5
6
7
```

```bash
$ seq 10 | slice ::2
1
3
5
7
9
```

```bash
$ seq 10 | slice ::-2
10
8
6
4
2
```

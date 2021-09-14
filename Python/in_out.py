def read():
    lines = []
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines


def read_line():
    with open('input.txt') as f:
        return f.read()


def write(val):
    f = open('output.txt', 'a')
    f.write(val + "\n")

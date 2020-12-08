def make_filename(day):
    return f'../data/input{day:02}.txt'


def read(day):
    with open(make_filename(day)) as f:
        return f.read()


def readlines(day, converter=None):
    with open(make_filename(day)) as f:
        if converter:
            return [converter(line) for line in f.readlines()]
        return [line.strip() for line in f.readlines()]

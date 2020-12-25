SUBJECT_NUMBER = 7


def calc_loop_size(key, subject_number=SUBJECT_NUMBER):
    loop_size = 0
    value = 1

    while value != key:
        loop_size += 1
        value *= subject_number
        value %= 20201227

    return loop_size


def transform(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value %= 20201227

    return value


def calc_encryption_key(pk1, pk2):
    loop_size1 = calc_loop_size(pk1)
    loop_size2 = calc_loop_size(pk2)
    ekey1 = transform(pk1, loop_size2)
    ekey2 = transform(pk2, loop_size1)
    return ekey1, ekey2


if __name__ == '__main__':
    print(calc_encryption_key(3469259, 13170438))

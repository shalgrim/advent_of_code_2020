from itertools import combinations

from day14_1 import apply_mask
from file_ops import readlines


def apply_mask_version_2(mask, num):
    binstr = bin(num)[2:]
    newstr = '0' * (36 - len(binstr)) + binstr
    return ''.join([n if m == '0' else m for m, n in zip(mask, newstr)])


def apply_float(j, c, floating_bits):
    new_chars = []
    if c != 'X':
        new_chars.append(c)
    else:
        if j in floating_bits:
            new_chars.append('1')
        else:
            new_chars.append('0')

    return ''.join(new_chars)


def addresses_to_update(mask, address):
    floating_mask = apply_mask_version_2(mask, address)
    floating_bits = [i for i, c in enumerate(floating_mask) if c == 'X']
    addresses = set()
    for combo_len in range(len(floating_bits) + 1):
        for combo in combinations(floating_bits, combo_len):
            new_chars = []
            for j, c in enumerate(floating_mask):
                if c != 'X':
                    new_chars.append(c)
                elif j in combo:
                    new_chars.append('1')
                else:
                    new_chars.append('0')

            addresses.add(int(''.join(new_chars), 2))

    return addresses


def update_memory(mask, line, memory):
    address = int(line.split('[')[1].split(']')[0])
    num = int(line.split()[-1].strip())
    for address in addresses_to_update(mask, address):
        memory[address] = num


def main(lines):
    mask = ''
    memory = {}
    for line in lines:
        if line.startswith('mask'):
            mask = line.split()[-1].strip()
        else:
            update_memory(mask, line, memory)

    return sum(memory.values())


if __name__ == '__main__':
    lines = readlines(14)
    print(main(lines))

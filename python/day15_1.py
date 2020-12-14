from file_ops import readlines


def apply_mask(mask, num):
    binstr = bin(num)[2:]
    mask_dict ={i: val for i, val in enumerate(mask[::-1]) if val != 'X'}
    newstr = binstr[::-1] + '0' * (36 - len(binstr))
    applied = ''.join([mask_dict[i] if i in mask_dict else c for i, c in enumerate(newstr)])

    return int(applied[::-1], 2)


def main(lines):
    mask = ''
    memory = {}
    for line in lines:
        if line.startswith('mask'):
            mask = line.split()[-1].strip()
        else:
            address = int(line.split('[')[1].split(']')[0])
            num = int(line.split()[-1].strip())
            memory[address] = apply_mask(mask, num)
    return sum(memory.values())


if __name__ == '__main__':
    lines = readlines(15)
    print(main(lines))

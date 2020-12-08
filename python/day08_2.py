from file_ops import readlines

ACCUMULATOR = 0
EXECUTED = set()


def execute_instruction(instruction, value):
    global ACCUMULATOR
    if instruction == 'jmp':
        return int(value)
    elif instruction == 'acc':
        ACCUMULATOR += int(value)
    return 1


def run_until_exhaustion_or_repeat(instructions):
    global ACCUMULATOR, EXECUTED
    ACCUMULATOR = 0
    EXECUTED.clear()
    instruction_pointer = 0

    while instruction_pointer < len(instructions):
        if instruction_pointer in EXECUTED:
            return False
        EXECUTED.add(instruction_pointer)
        instruction_pointer += execute_instruction(*instructions[instruction_pointer])

    return True


if __name__ == '__main__':
    lines = readlines(8)
    split_lines = [line.split() for line in lines]
    for i, line in enumerate(split_lines):
        if line[0] == 'nop':
            instructions = split_lines[:i] + [['jmp', line[1]]] + split_lines[i + 1 :]
        elif line[0] == 'jmp':
            instructions = split_lines[:i] + [['nop', line[1]]] + split_lines[i + 1 :]
        else:
            instructions = split_lines
        if run_until_exhaustion_or_repeat(instructions):
            break
    print(ACCUMULATOR)

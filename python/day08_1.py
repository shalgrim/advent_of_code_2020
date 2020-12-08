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


def run_until_second_execution(instructions):
    global EXECUTED
    instruction_pointer = 0

    while instruction_pointer not in EXECUTED:
        EXECUTED.add(instruction_pointer)
        instruction_pointer += execute_instruction(*instructions[instruction_pointer])
        print(instruction_pointer)


if __name__ == '__main__':
    lines = readlines(8)
    run_until_second_execution([line.split() for line in lines])
    print(ACCUMULATOR)
from copy import copy

from day13_1 import LINE_TWO
import math
import datetime


def does_work(minutes_past, bus, t):
    if minutes_past == 0:
        return t % bus == 0
    return bus - minutes_past == t % bus


def parse_line(line):
    minutes_past_t = [
        (minute, int(bus)) for minute, bus in enumerate(line.split(',')) if bus != 'x'
    ]
    return minutes_past_t


def main(line):
    minutes_past_t = parse_line(line)
    lowest_bus = min([tup[1] for tup in minutes_past_t])
    minutes_past_for_lowest_bus = [t[0] for t in minutes_past_t if t[1] == lowest_bus][
        0
    ]
    print(lowest_bus, minutes_past_for_lowest_bus)
    highest_bus = max([tup[1] for tup in minutes_past_t])
    minutes_past_for_highest_bus = [
        t[0] for t in minutes_past_t if t[1] == highest_bus
    ][-1]

    t = highest_bus - minutes_past_for_highest_bus
    # t = minutes_past_for_lowest_bus
    log_len = 0
    start = datetime.datetime.now()

    while True:
        if all(does_work(*tup, t) for tup in minutes_past_t if tup[1] != highest_bus):
            break
        t += highest_bus

        if int(math.log10(t)) > log_len:
            td = datetime.datetime.now() - start
            log_len = int(math.log10(t))
            print(math.log10(t), t, td.seconds)

    return t


def reduce(modulos, remainders):
    lcm = math.prod(modulos[:2])
    larger = max(modulos[:2])
    number = remainders[0] if modulos[0] == larger else remainders[1]
    numbers_to_test = []

    while number < lcm:
        numbers_to_test.append(number)
        number += larger

    for num in numbers_to_test:
        if num % modulos[1] == remainders[1] and num % modulos[0] == remainders[0]:
            break
    else:
        raise Exception('should always break')

    return [lcm] + modulos[2:], [num] + remainders[2:]


def main_attempt_two(line):
    minutes_past_t_and_buses = parse_line(line)
    modulos = [bus for mins, bus in minutes_past_t_and_buses]
    remainders = [0 if mins == 0 else (bus - mins) % bus for mins, bus in minutes_past_t_and_buses]
    new_modulos = copy(modulos)
    new_remainders = copy(remainders)

    while len(new_modulos) > 1:
        new_modulos, new_remainders = reduce(new_modulos, new_remainders)

    return new_remainders[0]


if __name__ == '__main__':
    print(main_attempt_two(LINE_TWO))
    # print(main(LINE_TWO))  # 1068792 is too low

    # this seems promising http://mathforum.org/library/drmath/view/75030.html
    # build up a list of numbers that fit a smaller search space
